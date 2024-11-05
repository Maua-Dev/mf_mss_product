from typing import List
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.entities.user import User


class UserRestaurantViewModel:
    user_id: str
    restaurant: RESTAURANT
    role: ROLE

    def __init__(self, user: User):
        self.user = user.name
        self.restaurant = user.restaurant
        self.role = user.role

    def to_dict(self):
        return {
            "user": self.user,
            "restaurant": self.restaurant.value,
            "role": self.role.value
        }
    
class GetAllUsersByRestaurantViewModel:
    users: List[User]

    def __init__(self, users: List[UserRestaurantViewModel]):
        self.users = users
    
    def to_dict(self):
        return {
            'users': [UserRestaurantViewModel(user).to_dict() for user in self.users],
            'message': "the users with restaurant were retrieved"
        }