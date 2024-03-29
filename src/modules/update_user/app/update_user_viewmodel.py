from typing import Optional

from src.shared.domain.entities.user import User
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class UserViewmodel:
    user_name: str
    user_email: str
    role: str
    restaurant: Optional[str] = None
    user_id: str
    photo: str

    def __init__(self, user: User):
        self.user_name = user.name
        self.user_email = user.email
        self.role = user.role.value
        self.user_id = user.user_id
        self.restaurant = user.restaurant.value if user.restaurant is not None else None
        self.photo = user.photo

    def to_dict(self):
        return {
            "name": self.user_name,
            "email": self.user_email,
            "role": self.role,
            "user_id": self.user_id,
            "restaurant": self.restaurant,
            "photo": self.photo
        }


class UpdateUserViewmodel:
    user_viewmodel: UserViewmodel

    def __init__(self, user: User):
        self.user_viewmodel = UserViewmodel(user)

    def to_dict(self):
        return {
            "user": self.user_viewmodel.to_dict(),
            "message": "the user was updated"
        }
