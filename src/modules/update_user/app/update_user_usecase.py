from typing import Optional

from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, DuplicatedItem


class UpdateUserUsecase:
    def __init__(self, repo: IUserRepository):
        self.repository = repo

    def __call__(self, user_id: str, new_name: Optional[str] = None):
        if not User.validate_user_id(user_id):
            raise EntityError("user_id")

        user_to_update = self.repository.get_user_by_id(user_id)

        if user_to_update is None:
            raise NoItemsFound("user")

        new_user = User(
            user_id=user_to_update.user_id,
            name=user_to_update.name,
            email=user_to_update.email,
            role=user_to_update.role,
            restaurant=user_to_update.restaurant
        )

        if new_name is not None:
            if new_name == user_to_update.name:
                raise DuplicatedItem("user_name")

            if not User.validate_name(new_name):
                raise EntityError("user_name")

            new_user.name = new_name

        # if new_email is not None:
        #     if new_email == user_to_update.email:
        #         raise DuplicatedItem("user_email")
        #
        #     if not User.validate_email(new_email):
        #         raise EntityError("user_email")
        #
        #     new_user.email = new_email

        return self.repository.update_user_by_id(user_id=new_user.user_id, new_name=new_user.name)
