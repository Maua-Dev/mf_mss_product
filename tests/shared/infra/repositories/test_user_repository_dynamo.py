import pytest
from src.shared.infra.repositories.user_repository_dynamo import UserRepositoryDynamo
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

class Test_UserRepositoryDynamo:

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_create_user(self):
        repo_dynamo = UserRepositoryDynamo()
        repo_mock = UserRepositoryMock()

        user = repo_mock.users_list[2]
        user.name = "Pimbas"

        new_user = repo_dynamo.create_user(new_user=user)

        assert new_user == repo_mock.users_list[2]

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_user_by_id(self):
        repo_dynamo = UserRepositoryDynamo()
        repo_mock = UserRepositoryMock()

        user = repo_mock.users_list[1]

        get_user = repo_dynamo.get_user_by_id(user_id=user.user_id)

        assert get_user.name == user.name
        assert get_user.email == user.email
        assert get_user.role == user.role
        assert get_user.user_id == user.user_id
        assert get_user.restaurant == user.restaurant

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_user_by_id(self):
        repo_dynamo = UserRepositoryDynamo()
        repo_mock = UserRepositoryMock()

        user = repo_mock.users_list[4]

        update_product = repo_dynamo.update_user_by_id(user_id=user.user_id, new_name="João Brancass", new_photo="https://www.google.com")

        assert update_product.name == "João Brancass"
        assert update_product.photo == "https://www.google.com"

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_delete_user_by_id(self):
        repo_dynamo = UserRepositoryDynamo()
        repo_mock = UserRepositoryMock()

        user = repo_mock.users_list[3]
        
        delete_user = repo_dynamo.delete_user_by_id(user_id=user.user_id)

        assert True