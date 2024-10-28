from typing import Optional
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class DeleteUserUsecase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def __call__(self, user_id: str, restaurant: Optional[RESTAURANT] = None, validate_user: bool = False) -> Optional[User]:
        if not User.validate_user_id(user_id=user_id):
            raise EntityError("user_id")
        
        user = self.repo.delete_user_by_id(user_id=user_id)

        if user is None:
            raise NoItemsFound("user_id")
        
        if not user.confirm_user:
            raise NoItemsFound("User not validated")
        
        return user