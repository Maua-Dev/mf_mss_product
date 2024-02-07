import abc

from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterExcededMaximumValue, EntityParameterHaveMinValue
from typing import Optional


class Feedback(abc.ABC):
    order_id: str
    user_id: str
    restaurant: RESTAURANT
    value : int
    MIN_VALUE = 1
    MAX_VALUE = 5
    ID_LENGTH = 36

    def __init__(self,
                 order_id: str,
                 user_id: str,
                 restaurant: RESTAURANT,
                 value: int):

        if not Feedback.validate_id(id=order_id):
            raise EntityError("order_id")
        self.order_id = order_id

        if not Feedback.validate_id(id=user_id):
            raise EntityError("user_id")
        self.user_id = user_id

        if type(restaurant) != RESTAURANT:
            raise EntityError("restaurant")
        self.restaurant = restaurant

        if type(value) != int:
            raise EntityError("value")
        self.value = value

        if value > self.MAX_VALUE:
            raise EntityParameterExcededMaximumValue(field='value', maximum_value=str(self.MAX_VALUE))
        
        if value < self.MIN_VALUE:
            raise EntityParameterHaveMinValue(field='value', minimum_value=str(self.MIN_VALUE))

    @staticmethod
    def validate_id(id: str) -> bool:
        if type(id) != str:
            return False
        if len(id) != Feedback.ID_LENGTH:
            return False
        return True

    def __repr__(self):
        return f"Feedback(order_id={self.order_id}, user_id={self.user_id}, restaurant='{self.restaurant.value}', value={self.value})"
    
    def __eq__(self, other):
        return self.order_id == other.order_id and self.user_id == other.user_id and self.restaurant == other.restaurant and self.value == other.value