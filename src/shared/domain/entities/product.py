import abc

from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterExcededMaximumValue
from typing import Optional


class Product(abc.ABC):
    available: bool
    _price: float
    name: str
    description: str
    meal_type: MEAL_TYPE
    photo: Optional[str] = None
    product_id: str
    last_update: int  # miliseconds
    restaurant: RESTAURANT
    prepare_time: int = None  # min
    PRODUCT_ID_LENGTH = 36
    MAXIMUM_PRICE = 10000.00

    def __init__(self,
                 available: bool,
                 input_price: float,
                 name: str,
                 description: str,
                 meal_type: MEAL_TYPE,
                 product_id: str,
                 last_update: int,
                 restaurant: RESTAURANT,
                 prepare_time: int = None,
                 photo: str = None):

        if type(available) != bool:
            raise EntityError("available")
        self.available = available

        if type(input_price) != float or input_price < 0:
            raise EntityError("price")
        if input_price > self.MAXIMUM_PRICE:
            raise EntityParameterExcededMaximumValue(field='price', maximum_value=str(self.MAXIMUM_PRICE))

        self._price = input_price

        if type(name) != str:
            raise EntityError("name")
        self.name = name

        if type(description) != str:
            raise EntityError("description")
        self.description = description

        if type(meal_type) != MEAL_TYPE:
            raise EntityError("meal_type")
        self.meal_type = meal_type

        if photo is not None:
            if type(photo) != str:
                raise EntityError("photo")
        self.photo = photo

        if not self.validate_product_id(product_id=product_id):
            raise EntityError("product_id")
        self.product_id = product_id

        if type(last_update) != int:
            raise EntityError("last_update")
        self.last_update = last_update

        if type(restaurant) != RESTAURANT:
            raise EntityError("restaurant")
        self.restaurant = restaurant

        if prepare_time is not None:
            if type(prepare_time) != int:
                raise EntityError("prepare_time")
        self.prepare_time = prepare_time

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value is None or value < 0:
            raise EntityError('price')
        if value > self.MAXIMUM_PRICE:
            raise EntityParameterExcededMaximumValue(field='price', maximum_value=str(self.MAXIMUM_PRICE))
        self._price = value

    @staticmethod
    def validate_product_id(product_id: str) -> bool:
        if type(product_id) != str: return False
        if len(product_id) != Product.PRODUCT_ID_LENGTH: return False
        return True

    def __repr__(self):
        return f"Product(available={self.available}, _price={self.price}, name='{self.name}', description='{self.description}', meal_type='{self.meal_type.value}', photo='{self.photo}', product_id={self.product_id}, last_update={self.last_update}, restaurant='{self.restaurant.value}', prepare_time={self.prepare_time})"
