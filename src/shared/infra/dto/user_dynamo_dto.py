from typing import Optional
from src.shared.domain.entities.user import User
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE


class UserDynamoDTO:
    name: str
    email: str
    role: ROLE
    restaurant: Optional[RESTAURANT] = None
    user_id: str
    photo: Optional[str] = None

    def __init__(self, name: str, email: str, role: ROLE, user_id: str, restaurant: Optional[RESTAURANT] = None, photo: Optional[str] = None):
        self.name = name
        self.email = email
        self.role = role
        self.restaurant = restaurant
        self.user_id = user_id
        self.photo = photo

    @staticmethod
    def from_entity(user: User) -> "UserDynamoDTO":
        """
        Parse data from User to UserDynamoDTO
        """
        return UserDynamoDTO(
            name = user.name,
            email = user.email,    
            role = user.role,
            restaurant = user.restaurant,
            user_id = user.user_id,
            photo = user.photo
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from UserDynamoDTO to dict
        """
        data = {
            "entity": "user",
            "name": self.name,
            "email": self.email,
            "user_id": self.user_id,
            "role": self.role.value,
            "restaurant": self.restaurant.value if self.restaurant is not None else None,
            "photo": self.photo
        }

        data_without_none_values = {k: v for k, v in data.items() if v is not None}

        return data_without_none_values

    @staticmethod
    def from_dynamo(user_data: dict) -> "UserDynamoDTO":
        """
        Parse data from DynamoDB to UserDynamoDTO
        @param user_data: dict from DynamoDB
        """
        return UserDynamoDTO(
            name=str(user_data["name"]),
            email=str(user_data["email"]),
            user_id=str(user_data["user_id"]),
            role=ROLE(user_data["role"]),
            restaurant=RESTAURANT(user_data.get("restaurant")) if user_data.get("restaurant") is not None else None,
            photo=str(user_data.get("photo")) if user_data.get("photo") is not None else None
        )

    def to_entity(self) -> User:
        """
        Parse data from UserDynamoDTO to User
        """
        return User(
            name=self.name,
            email=self.email,
            user_id=self.user_id,
            role=self.role,
            restaurant=self.restaurant,
            photo=self.photo
        )

    def __repr__(self):
        return f"UserDynamoDto(name={self.name}, email={self.email}, user_id={self.user_id}, role={self.role}, restaurant={self.restaurant}, photo={self.photo})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__