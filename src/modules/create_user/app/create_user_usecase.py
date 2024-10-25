from typing import Optional
from src.shared.domain.entities.user import User
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.usecase_errors import DuplicatedItem

class CreateUserUsecase:

    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def __call__(self, name: str, email: str, user_id: str, role: ROLE, restaurant: Optional[RESTAURANT] = None) -> User:
    
        if self.repo.get_user_by_id(user_id=user_id) is not None:
            raise DuplicatedItem("user_id")
                
        if role in [ROLE.OWNER, ROLE.SELLER]:
            confirm_user = False
        else:
            confirm_user = True
        
        user = User(name=name, email=email, role=role, user_id=user_id, photo=None, confirm_user=confirm_user, restaurant=restaurant)

        return self.repo.create_user(user)