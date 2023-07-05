import abc
import re
from typing import Optional
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError

class User(abc.ABC):
    name: str
    email: str
    role: ROLE
    restaurant: Optional[RESTAURANT] = None
    MIN_NAME_LENGTH = 2
    user_id: str
    USER_ID_LENGTH = 36

    def __init__(self, name: str, email: str, role: ROLE, user_id: str, restaurant: Optional[RESTAURANT] = None):
        if not User.validate_name(name):
            raise EntityError("name")
        self.name = name

        if not User.validate_email(email):
            raise EntityError("email")
        self.email = email

        if restaurant is not None:
            if type(restaurant) != RESTAURANT:
                raise EntityError("restaurant")

        if role == ROLE.OWNER and restaurant is None:
            raise EntityError("restaurant")

        if role == ROLE.SELLER and restaurant is None:
            raise EntityError("restaurant")

        self.restaurant = restaurant

        if not self.validate_user_id(user_id=user_id):
            raise EntityError("user_id")
        self.user_id = user_id

        if type(role) != ROLE:
            raise EntityError("state")
        self.role = role

        if type(user_id) != str:
            raise EntityError("user_id")  

    @staticmethod
    def validate_name(name: str) -> bool:
        regex = re.compile(r"^[a-zA-Z\s]+$")

        if name is None:
            return False
        elif type(name) != str:
            return False
        elif len(name) <= User.MIN_NAME_LENGTH:
            return False
        
        return bool(re.fullmatch(regex, name))

    @staticmethod
    def validate_email(email: str) -> bool:
        if email is None:
            return False

        regex = re.compile(r"^(?!.*\.\.)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

        return bool(re.fullmatch(regex, email))
    
    @staticmethod
    def validate_user_id(user_id: str) -> bool:
        if type(user_id) != str: return False
        if len(user_id) != User.USER_ID_LENGTH: return False
        return True

    def __repr__(self):
        return f"User(name={self.name}, email={self.email}, user_id={self.user_id}, state={self.role}, restaurant={self.restaurant})"
