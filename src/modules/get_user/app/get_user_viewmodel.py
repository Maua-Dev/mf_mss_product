from typing import Optional
from src.shared.domain.entities.user import User
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE

class UserViewmodel:
    user_name: str
    user_email: str
    role: ROLE
    restaurant: Optional[RESTAURANT] = None
    user_id: str
    photo: str = None

    def __init__(self, user: User):
        self.user_name = user.name
        self.user_email = user.email
        self.role = user.role
        self.user_id = user.user_id
        self.restaurant = user.restaurant
        self.photo = user.photo

    def to_dict(self):
        return {
            "name": self.user_name,
            "email": self.user_email,
            "role": self.role.value,
            "user_id": self.user_id,
            "restaurant": self.restaurant.value if self.restaurant is not None else None,
            "photo": self.photo
        }


class GetUserViewmodel:
    user_viewmodel: UserViewmodel

    def __init__(self, user: User):
        self.user_viewmodel = UserViewmodel(user)

    def to_dict(self):
        return {
            "user": self.user_viewmodel.to_dict(),
            "message": "the user was retrieved"
        }
