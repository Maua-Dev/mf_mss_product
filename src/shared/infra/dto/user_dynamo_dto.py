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

    def __init__(self, name: str, email: str, role: ROLE, user_id: str, restaurant: Optional[RESTAURANT] = None):
        self.name = name
        self.email = email
        self.role = role
        self.restaurant = restaurant
        self.user_id = user_id

    @staticmethod
    def from_entity(user: User) -> "UserDynamoDTO":
        """
        Parse data from User entity to UserDynamoDTO
        """
        return UserDynamoDTO(
            name=user.name,
            email=user.email,
            user_id=user.user_id,
            role=user.role,
            restaurant=user.restaurant,
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
            "restaurant": self.restaurant.value if self.restaurant is not None else None
        }
    
        data_without_none_values = {k: v for k, v in data.items() if v is not None}

        return data

    def __repr__(self):
        return f"UserDynamoDto(name={self.name}, email={self.email}, user_id={self.user_id}, role={self.role.value}, restaurant={self.restaurant.value})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__