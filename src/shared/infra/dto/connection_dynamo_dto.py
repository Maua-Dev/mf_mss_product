from decimal import Decimal
from typing import Optional
from src.shared.domain.entities.connection import Connection
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS

class ConnectionDynamoDTO:
    connection_id: str
    api_id: str
    expire_date_seconds: int
    creation_time_seconds: int
    user_id: str
    restaurant: Optional[RESTAURANT] = None

    def __init__(self, connection_id:str, api_id: str, expire_date_seconds:int, creation_time_seconds:int, user_id:str, restaurant: Optional[RESTAURANT] = None):
        self.connection_id = connection_id
        self.api_id = api_id
        self.expire_date_seconds = expire_date_seconds
        self.creation_time_seconds = creation_time_seconds
        self.user_id = user_id
        self.restaurant = restaurant
        
    @staticmethod
    def from_entity(connection:Connection) -> "ConnectionDynamoDTO":
        """
        Parse data from Connection to ConnectionDynamoDTO
        """
        return ConnectionDynamoDTO(
            connection_id=connection.connection_id,
            api_id=connection.api_id,
            expire_date_seconds=connection.expire_date_seconds,
            creation_time_seconds=connection.creation_time_seconds,
            user_id=connection.user_id,
            restaurant=connection.restaurant
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from ConnectionDynamoDTO to dict
        """
        data = {
            "entity": "connection",
            "connection_id": self.connection_id,
            "api_id": self.api_id,
            "expire_date_seconds": Decimal(str(self.expire_date_seconds)),
            "creation_time_seconds": Decimal(str(self.creation_time_seconds)),
            "user_id": self.user_id,
            "restaurant":self.restaurant.value if self.restaurant is not None else None
        }

        data_without_none_values = {k: v for k, v in data.items() if v is not None}

        return data_without_none_values
    
    @staticmethod
    def from_dynamo(connection_data: dict) -> "ConnectionDynamoDTO":
        """
        Parse data from DynamoDB to ConnectionDynamoDTO
        @param connection_data: dict from DynamoDB
        """
        return ConnectionDynamoDTO(
            connection_id=str(connection_data["connection_id"]),
            api_id=str(connection_data["api_id"]),
            expire_date_seconds=int(connection_data["expire_date_seconds"]),
            creation_time_seconds=int(connection_data["creation_time_seconds"]),
            user_id=str(connection_data["user_id"]),
            restaurant=RESTAURANT(connection_data.get("restaurant")) if connection_data.get("restaurant") is not None else None
        )

    def to_entity(self) -> Connection:
        """
        Parse data from ConnectionDynamoDTO to Connection
        """
        return Connection(
            connection_id=self.connection_id,
            api_id=self.api_id,
            expire_date_seconds=self.expire_date_seconds,
            creation_time_seconds=self.creation_time_seconds,
            user_id=self.user_id,
            restaurant=self.restaurant
        )

    def __eq__(self, other):
        return self.connection_id == other.connection_id and self.api_id == other.api_id and self.expire_date_seconds == other.expire_date_seconds and self.creation_time_seconds == other.creation_time_seconds and self.user_id == other.user_id and self.restaurant == other.restaurant