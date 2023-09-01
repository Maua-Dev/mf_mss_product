from src.shared.domain.entities.connection import Connection
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class ConnectionViewmodel:
    connection_id: str
    api_id: str
    expire_date_seconds: int
    creation_time_seconds: int
    user_id: str
    restaurant: RESTAURANT

    def __init__(self, connection: Connection):
        self.connection_id = connection.connection_id
        self.api_id = connection.api_id
        self.expire_date_seconds = connection.expire_date_seconds
        self.creation_time_seconds = connection.creation_time_seconds
        self.user_id = connection.user_id
        self.restaurant = connection.restaurant

    def to_dict(self) -> dict:
        return{
            "connection_id": self.connection_id,
            "api_id": self.api_id,
            "expire_date_seconds": self.expire_date_seconds,
            "creation_time_seconds": self.creation_time_seconds,
            "user_id": self.user_id,
            "restaurant": self.restaurant.value
        }

class CreateConnectionViewmodel:
    connection: ConnectionViewmodel

    def __init__(self, connection: Connection):
        self.connection = ConnectionViewmodel(connection)

    def to_dict(self):
        return{
            "connection": self.connection.to_dict(),
            "message": "the connection was created"
        }