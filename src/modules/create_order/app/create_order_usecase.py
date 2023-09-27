import datetime
from typing import List
import uuid
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser


class CreateOrderUsecase:

    def __init__(self, repo_order: IOrderRepository, repo_user: IUserRepository, repo_product: IProductRepository):
        self.repo_order = repo_order
        self.repo_user = repo_user
        self.repo_product = repo_product

    def __call__(self, user_name: str, user_id: str, products: List[OrderProduct], restaurant: RESTAURANT,
                 obervation: str = None) -> Order:

        user = self.repo_user.get_user_by_id(user_id=user_id)

        if user is None:
            raise UnregisteredUser()

        price = 0

        product_val = self.repo_product.batch_get_product(products=products, restaurant=restaurant)

        if product_val is None or len(product_val) == 0:
            raise NoItemsFound("product")

        i = 0
        for product in product_val:
            price += product.price * products[i].quantity
            i += 1

        order_id = str(uuid.uuid4())
        creation_time_milliseconds = int(datetime.datetime.now().timestamp() * 1000)
        status = STATUS.PENDING
        total_price = float(price)

        order = Order(order_id=order_id, user_name=user_name, user_id=user_id, products=products,
                      creation_time_milliseconds=creation_time_milliseconds, restaurant=restaurant, status=status,
                      total_price=total_price, observation=obervation, aborted_reason=None,
                      last_status_update_milliseconds=creation_time_milliseconds)

        return self.repo_order.create_order(order=order)
