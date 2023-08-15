import abc
from typing import Optional

from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError


class Connection(abc.ABC):
    connection_id: str
    client_id: str
    expire_date_seconds: int
    creation_time_seconds: int
    user_id: str
    restaurant: Optional[RESTAURANT] = None
    ID_LENGTH = 36

    def __init__(self,
                 connection_id: str,
                 client_id: str,
                 expire_date_seconds: int,
                 creation_time_seconds: int,
                 user_id: str,
                 restaurant: Optional[RESTAURANT] = None):
        
        if not Connection.validate_id(id=connection_id):
            raise EntityError("connection_id")
        self.connection_id = connection_id

        if not Connection.validate_id(id=client_id):
            raise EntityError("client_id")
        self.client_id = client_id

        if type(expire_date_seconds) != int:
            raise EntityError("expire_date_seconds")
        self.expire_date_seconds = expire_date_seconds

        if type(creation_time_seconds) != int:
            raise EntityError("creation_time_seconds")
        self.creation_time_seconds = creation_time_seconds

        if not Connection.validate_id(id=user_id):
            raise EntityError("user_id")
        self.user_id = user_id

        if restaurant is not None:
            if type(restaurant) != RESTAURANT:
                raise EntityError("restaurant")
        self.restaurant = restaurant
    
    @staticmethod
    def validate_id(id: str) -> bool:
        if type(id) != str:
            return False
        if len(id) != Connection.ID_LENGTH:
            return False
        return True