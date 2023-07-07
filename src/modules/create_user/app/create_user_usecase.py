from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.usecase_errors import DuplicatedItem

class CreateUserUsecase:

    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def __call__(self, name: str, email: str, user_id: str) -> User:
    
        if self.repo.get_user_by_id(user_id=user_id) is not None:
            raise DuplicatedItem("user_id")
        
        user = User(name=name, email=email, role=ROLE.USER, restaurant=None, user_id=user_id)

        return self.repo.create_user(user)