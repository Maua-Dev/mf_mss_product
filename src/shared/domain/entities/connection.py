import abc
from typing import Optional

from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError


class Connection(abc.ABC):
    connection_id: str
    api_id: str
    expire_date_seconds: int
    creation_time_seconds: int
    user_id: str
    restaurant: Optional[RESTAURANT] = None
    CONNECTION_ID_LENGTH = 16
    API_ID_LENGTH = 10
    USER_ID_LENGTH = 36

    def __init__(self,
                 connection_id: str,
                 api_id: str,
                 expire_date_seconds: int,
                 creation_time_seconds: int,
                 user_id: str,
                 restaurant: Optional[RESTAURANT] = None):
        
        if not Connection.validate_connection_id(connection_id=connection_id):
            raise EntityError("connection_id")
        self.connection_id = connection_id

        if not Connection.validate_api_id(api_id=api_id):
            raise EntityError("api_id")
        self.api_id = api_id

        if type(expire_date_seconds) != int:
            raise EntityError("expire_date_seconds")
        self.expire_date_seconds = expire_date_seconds

        if type(creation_time_seconds) != int:
            raise EntityError("creation_time_seconds")
        self.creation_time_seconds = creation_time_seconds

        if not Connection.validate_user_id(user_id=user_id):
            raise EntityError("user_id")
        self.user_id = user_id

        if restaurant is not None:
            if type(restaurant) != RESTAURANT:
                raise EntityError("restaurant")
        self.restaurant = restaurant
    
    @staticmethod
    def validate_connection_id(connection_id: str) -> bool:
        if type(connection_id) != str:
            return False
        if len(connection_id) != Connection.CONNECTION_ID_LENGTH:
            return False
        return True
    
    @staticmethod
    def validate_api_id(api_id: str) -> bool:
        if type(api_id) != str:
            return False
        if len(api_id) != Connection.API_ID_LENGTH:
            return False
        return True
    
    @staticmethod
    def validate_user_id(user_id: str) -> bool:
        if type(user_id) != str:
            return False
        if len(user_id) != Connection.USER_ID_LENGTH:
            return False
        return True
    
    def __repr__(self):
        return f"Connection(connection_id={self.connection_id}, api_id={self.api_id}, expire_date_seconds={self.expire_date_seconds}, creation_time_seconds={self.creation_time_seconds}, user_id={self.user_id}, restaurant={self.restaurant})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__ 