from src.shared.domain.entities.user import User
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE


class UserViewmodel:
    user_id: str
    name: str
    email: str
    restaurant: RESTAURANT = None
    role: ROLE

    def __init__(self, user: User):
        self.user_id = user.user_id
        self.name = user.name
        self.email = user.email
        self.restaurant = user.restaurant
        self.role = user.role

    def to_dict(self) -> dict:
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'restaurant': self.restaurant,
            'role': self.role.value
        }
    
class DeleteUserViewmodel:
        
    def __init__(self, user: User):
            self.user = UserViewmodel(user=user)

    def to_dict(self):
        return {
            "user": self.user.to_dict(),
            "message": "the user was deleted"
        }