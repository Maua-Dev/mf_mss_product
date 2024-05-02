import uuid
from typing import List, Optional
from datetime import datetime, timedelta

from src.shared.domain.entities.order import Order
from src.shared.domain.enums.action_enum import ACTION
from src.shared.domain.enums.status_enum import STATUS
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser, \
    TimeReservedNeedsToBeAtLeastOneHourAhead, RestaurantDontPermitSchedule, TimeReservedNotAvailable, MinimumPriceForTimeReserved
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.domain.repositories.product_repository_interface import IProductRepository


class CreateOrderUsecase:

    def __init__(self, repo_order: IOrderRepository, repo_user: IUserRepository, repo_product: IProductRepository):
        self.repo_order = repo_order
        self.repo_user = repo_user
        self.repo_product = repo_product

    def __call__(self, user_name: str, user_id: str, products: List[OrderProduct],
                 restaurant: RESTAURANT, time_reserved: Optional[datetime] = None) -> Order:

        user = self.repo_user.get_user_by_id(user_id=user_id)

        if user is None:
            raise UnregisteredUser()

        if time_reserved:
            if time_reserved < datetime.now() + timedelta(hours=1):
                raise TimeReservedNeedsToBeAtLeastOneHourAhead()
            if time_reserved.date() != datetime.now().date():
                raise TimeReservedNotAvailable()
            shedule = self.repo_order.get_schedule_by_restaurant(restaurant=restaurant)
            if shedule is None:
                raise NoItemsFound("schedule")
            if not shedule.accepted_reservation:
                raise RestaurantDontPermitSchedule()
            if time_reserved.time() < shedule.initial_time or time_reserved.time() > shedule.end_time:
                raise TimeReservedNotAvailable()

        price = 0

        product_val = self.repo_product.batch_get_product(products=products, restaurant=restaurant)

        if product_val is None or len(product_val) == 0:
            raise NoItemsFound("product")

        i = 0
        for product in product_val:
            price += product.price * products[i].quantity
            i += 1

        if time_reserved and price < 15:
            raise MinimumPriceForTimeReserved(15)

        order_id = str(uuid.uuid4())
        creation_time_milliseconds = int(datetime.now().timestamp() * 1000)
        status = STATUS.PENDING
        total_price = float(price)
        time_reserved = int(time_reserved.timestamp() * 1000) if time_reserved else None

        order = Order(order_id=order_id, user_name=user_name, user_id=user_id, products=products,
                      creation_time_milliseconds=creation_time_milliseconds, restaurant=restaurant, status=status,
                      total_price=total_price, aborted_reason=None,
                      last_status_update_milliseconds=creation_time_milliseconds,
                      action=ACTION.NEW, time_reserved=time_reserved)

        return self.repo_order.create_order(order=order)
