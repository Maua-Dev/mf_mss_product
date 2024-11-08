from typing import List, Optional
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.entities.user import User

class UserViewModel:
    user_id: str
    name: str
    email: str
    role: ROLE
    restaurant: Optional[RESTAURANT] = None
    photo: Optional[str] = None
    confirm_user: bool
    new_confirm_user: bool

    def __init__(self, user: User):
        self.user_id = user.user_id
        self.name = user.name
        self.email = user.email
        self.role = user.role
        self.restaurant = user.restaurant
        self.photo = user.photo
        self.confirm_user = user.confirm_user

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'role': self.role.value,
            'photo': self.photo,
            'confirm_user': self.confirm_user,
            'restaurant': self.restaurant.value
        }
    
class GetAllUsersByRestaurantViewModel:
    users: List[User]

    def __init__(self, users: List[UserViewModel]):
        self.users = users
    
    def to_dict(self):
        return {
            'users': [UserViewModel(user).to_dict() for user in self.users],
            'message': "the users with restaurant were retrieved"
        }