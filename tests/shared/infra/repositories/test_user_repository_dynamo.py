import pytest
from src.shared.infra.repositories.user_repository_dynamo import UserRepositoryDynamo
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

class Test_UserRepositoryDynamo:

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_create_user(self):
        repo_dynamo = UserRepositoryDynamo()
        repo_mock = UserRepositoryMock()

        user = repo_mock.users_list[2]

        new_user = repo_dynamo.create_user(new_user=user)

        assert new_user == repo_mock.users_list[2]