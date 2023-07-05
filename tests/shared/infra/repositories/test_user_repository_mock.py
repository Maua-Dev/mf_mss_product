from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UserRepositoryMock:

    def test_user_repository_mock(self):
        repo_mock = UserRepositoryMock()

    def test_create_user(self):
        repo_mock = UserRepositoryMock()

        length_before_creation = len(repo_mock.users_list)

        new_user = User(name="Tyrion Lenister", email="got@hbo.com", role=ROLE.ADMIN,
                        user_id="93bc6ada-c0d1-7054-66ab-e17414c48af5", restaurant=None),

        response = repo_mock.create_user(new_user)

        assert len(repo_mock.users_list) == length_before_creation + 1

    