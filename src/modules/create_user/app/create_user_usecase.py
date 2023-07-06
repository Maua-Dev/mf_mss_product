from typing import Any
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE

class CreateUserUsecase:

    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def __call__(self, name: str, email: str, role: ROLE, restaurant: None, user_id: str) -> User:
    
        if role is not ROLE.USER:
            raise EntityError("role")
        
        if restaurant is not None:
            raise EntityError("restaurant")

        user = User(name=name, email=email, role=ROLE.USER, restaurant=None, user_id=user_id)

        return self.repo.create_user(user)