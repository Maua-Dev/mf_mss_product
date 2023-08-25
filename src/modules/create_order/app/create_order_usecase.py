import datetime
from typing import List, Optional
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

    def __call__(self, user_name: str, user_id: str, products: List[OrderProduct], restaurant: RESTAURANT, obervation: str = None) -> Order:
        
        user = self.repo_user.get_user_by_id(user_id=user_id)

        if user is None:
            raise UnregisteredUser()
        
        price = 0
        for product in products:
            product_val = self.repo_product.get_product(product_id=product.product_id, restaurant=restaurant)

            if product_val is None:
                raise NoItemsFound("product_id or restaurant")
            
            price += product_val.price * product.quantity
        
        

        order_id = str(uuid.uuid4())
        creation_time_milliseconds = int(datetime.datetime.now().timestamp() * 1000)
        status = STATUS.PENDING
        total_price = price

        order = Order(order_id=order_id, user_name=user_name, user_id=user_id, products=products, creation_time_milliseconds=creation_time_milliseconds, restaurant=restaurant, status=status, total_price=total_price, observation=obervation, aborted_reason=None)

        return self.repo_order.create_order(order=order)