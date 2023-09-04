import abc
import re
from typing import List, Optional
from src.shared.domain.entities.order_product import OrderProduct

from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterExcededMaximumValue


class Order(abc.ABC):
    order_id: str
    user_name: str
    user_id: str
    products: List[OrderProduct]
    creation_time_milliseconds: int
    restaurant: RESTAURANT
    observation: Optional[str] = None
    status: STATUS
    aborted_reason: Optional[str] = None
    total_price: float
    last_status_update_milliseconds: int
    ID_LENGTH = 36
    MIN_NAME_LENGTH = 2

    def __init__(self,
                 order_id: str,
                 user_name: str,
                 user_id: str,
                 products: List[OrderProduct],
                 creation_time_milliseconds: int,
                 restaurant: RESTAURANT,
                 status: STATUS,
                 total_price: float,
                 last_status_update_milliseconds: int,
                 observation: Optional[str] = None,
                 aborted_reason: Optional[str] = None
                 ):
        
        if not Order.validate_id(id=order_id):
            raise EntityError("order_id")
        self.order_id = order_id

        if not Order.validate_user_name(user_name=user_name):
            raise EntityError("user_name")
        self.user_name = user_name

        if not Order.validate_id(id=user_id):
            raise EntityError("user_id")
        self.user_id = user_id

        if not Order.validate_products(products=products):
            raise EntityError("products")
        self.products = products
        
        if type(creation_time_milliseconds) != int:
            raise EntityError("creation_time_milliseconds")
        self.creation_time_milliseconds = creation_time_milliseconds

        if type(last_status_update_milliseconds) != int:
            raise EntityError("last_status_update_milliseconds")
        if last_status_update_milliseconds < creation_time_milliseconds:
            raise EntityParameterExcededMaximumValue(field="last_status_update", maximum_value=str(creation_time_milliseconds))

        self.last_status_update_milliseconds = last_status_update_milliseconds

        if type(restaurant) != RESTAURANT:
            raise EntityError("restaurant")
        self.restaurant = restaurant

        if observation is not None:
            if type(observation) != str:
                raise EntityError("observation")
        self.observation = observation

        if type(status) != STATUS:
            raise EntityError("status")
        self.status = status

        if aborted_reason is not None:
            if type(aborted_reason) != str:
                raise EntityError("aborted_reason")
        self.aborted_reason = aborted_reason

        if type(total_price) != float:
            raise EntityError("total_price")
        self.total_price = total_price

    @staticmethod
    def validate_id(id: str) -> bool:
        if type(id) != str:
            return False
        if len(id) != Order.ID_LENGTH:
            return False
        return True
    
    @staticmethod
    def validate_user_name(user_name: str) -> bool:
        regex = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$")

        if user_name is None:
            return False
        elif type(user_name) != str:
            return False
        elif len(user_name) <= Order.MIN_NAME_LENGTH:
            return False
        
        return bool(re.fullmatch(regex, user_name))
    
    @staticmethod
    def validate_products(products: List[OrderProduct]) -> bool:
        if type(products) != list:
            return False
        for product in products:
            if not isinstance(product, OrderProduct):
                return False
        return True
    
    def __repr__(self):
        return f"Order(order_id={self.order_id}, user_name={self.user_name}, user_id={self.user_id}, products={self.products}, creation_time_milliseconds={self.creation_time_milliseconds}, restaurant={self.restaurant}, observation={self.observation}, status={self.status}, aborted_reason={self.aborted_reason}, total_price={self.total_price}, last_status_update={self.last_status_update_milliseconds})"