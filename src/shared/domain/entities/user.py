import abc
import re
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError
from typing import Optional

class User(abc.ABC):
    name: str
    email: str
    role: ROLE
    restaurant: Optional[RESTAURANT]
    MIN_NAME_LENGTH = 2
    user_id: str
    USER_ID_LENGTH = 36

    def __init__(self, name: str, email: str, role: ROLE, user_id: str, restaurant: Optional[RESTAURANT]):
        if not User.validate_name(name):
            raise EntityError("name")
        self.name = name

        if not User.validate_email(email):
            raise EntityError("email")
        self.email = email

        if type(user_id) == str:
            raise EntityError("user_id")

        if type(restaurant) != Optional[RESTAURANT]:
            raise EntityError("restaurant")

        if not self.validate_user_id(user_id=user_id):
            raise EntityError("user_id")
        self.user_id = user_id

        if type(role) != ROLE:
            raise EntityError("state")
        self.role = role

    @staticmethod
    def validate_name(name: str) -> bool:
        if name is None:
            return False
        elif type(name) != str:
            return False
        elif len(name) < User.MIN_NAME_LENGTH:
            return False

        return True

    @staticmethod
    def validate_email(email: str) -> bool:
        if email is None:
            return False

        regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        return bool(re.fullmatch(regex, email))
    
    @staticmethod
    def validate_user_id(user_id: str) -> bool:
        if type(user_id) != str: return False
        if len(user_id) != User.USER_ID_LENGTH: return False
        return True

    def __repr__(self):
        return f"User(name={self.name}, email={self.email}, user_id={self.user_id}, state={self.role})"
