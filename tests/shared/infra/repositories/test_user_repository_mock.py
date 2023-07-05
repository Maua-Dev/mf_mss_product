from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

first_user_id = UserRepositoryMock().users_list[0].user_id


class Test_UserRepositoryMock:

    def test_user_repository_mock(self):
        repo_mock = UserRepositoryMock()

    def test_create_user(self):
        repo_mock = UserRepositoryMock()

        length_before_creation = len(repo_mock.users_list)

        new_user = User(name="Tyrion Lenister", email="got@hbo.com", role=ROLE.ADMIN,
                        user_id="93bc6ada-c0d1-7054-66ab-e17414c48af5", restaurant=None)

        response = repo_mock.create_user(new_user)

        assert len(repo_mock.users_list) == length_before_creation + 1
        assert repo_mock.users_list[-1] == new_user

    def test_get_user_by_id_with_valid_id(self):
        repo_mock = UserRepositoryMock()

        response = repo_mock.get_user_by_id(first_user_id)

        assert response == repo_mock.users_list[0]

    def test_get_user_by_id_with_invalid_id(self):
        repo_mock = UserRepositoryMock()

        response = repo_mock.get_user_by_id("Um id que não existe")

        assert response is None

    def test_update_user_name_with_valid_name(self):
        repo_mock = UserRepositoryMock()

        response = repo_mock.update_user_by_id(first_user_id, new_name="Sacul Zeud")

        assert repo_mock.users_list[0].name == "Sacul Zeud"
        assert repo_mock.users_list[0].email == response.email

    def test_update_user_name_with_invalid_name(self):
        repo_mock = UserRepositoryMock()

        first_user_name = repo_mock.users_list[0].name
        first_user_email = repo_mock.users_list[0].email

        response = repo_mock.update_user_by_id(first_user_id, new_name="Luc@as D3uz")

        assert repo_mock.users_list[0].name == first_user_name
        assert repo_mock.users_list[0].email == first_user_email

    def test_update_user_email_with_valid_email(self):
        repo_mock = UserRepositoryMock()

        response = repo_mock.update_user_by_id(first_user_id, new_email="meu.novo.email@gmail.com")

        assert repo_mock.users_list[0].name == response.name
        assert repo_mock.users_list[0].email == "meu.novo.email@gmail.com"

    def test_update_user_name_with_invalid_email(self):
        repo_mock = UserRepositoryMock()

        first_user_name = repo_mock.users_list[0].name
        first_user_email = repo_mock.users_list[0].email

        response = repo_mock.update_user_by_id(first_user_id, new_email="@gmail.com")

        assert repo_mock.users_list[0].name == first_user_name
        assert repo_mock.users_list[0].email == first_user_email

    def test_update_user_with_invalid_id(self):
        repo_mock = UserRepositoryMock()

        response = repo_mock.update_user_by_id("Um id que não existe", "novo nome", "novo email")

        assert response is None

    def test_delete_user_with_valid_id(self):
        repo_mock = UserRepositoryMock()

        length_before_delete = len(repo_mock.users_list)

        deleted_user = repo_mock.delete_user_by_id(first_user_id)

        assert len(repo_mock.users_list) == length_before_delete - 1
        assert repo_mock.users_list[0] != deleted_user

    def test_delete_user_by_id_with_invalid_id(self):
        repo_mock = UserRepositoryMock()

        length_before_delete = len(repo_mock.users_list)

        response = repo_mock.delete_user_by_id("Um id que não existe")

        assert response is None
        assert len(repo_mock.users_list) == length_before_delete
