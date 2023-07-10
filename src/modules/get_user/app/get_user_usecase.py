from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetUserUseCase:
    repo: IUserRepository

    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def __call__(self, user_id: str):
        if not User.validate_user_id(user_id):
            raise EntityError("user_id")

        user = self.repo.get_user_by_id(user_id=user_id)

        if user is None:
            raise NoItemsFound("user")

        return user
