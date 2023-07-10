import pytest

from src.modules.get_user.app.get_user_usecase import GetUserUseCase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

repo_mock: UserRepositoryMock = UserRepositoryMock()
first_user_id = repo_mock.users_list[0].user_id

class Test_GetUserUseCase:

    def test_use_case_with_valid_id(self):
        usecase = GetUserUseCase(repo_mock)
        response = usecase(first_user_id)

        assert response is repo_mock.users_list[0]

    def test_use_case_with_invalid_id(self):
        with pytest.raises(EntityError):
            usecase = GetUserUseCase(repo_mock)
            response = usecase("Um id inválido")


    def test_use_case_with_unexistent_id(self):
        with pytest.raises(NoItemsFound):
            usecase = GetUserUseCase(repo_mock)
            response = usecase("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
