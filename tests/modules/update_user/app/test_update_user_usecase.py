import pytest

from src.modules.update_user.app.update_user_usecase import UpdateUserUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateUserUsecase:
    def test_update_user_name(self):
        repo_mock = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo_mock)
        first_user = repo_mock.users_list[0]

        user_email_before = first_user.email

        updated_user = usecase(user_id=first_user.user_id, new_name="Sacul Zeud")

        assert first_user.name == "Sacul Zeud"
        assert first_user.email == user_email_before

    def test_update_user_name_with_same_name(self):
        with pytest.raises(DuplicatedItem):
            repo_mock = UserRepositoryMock()
            usecase = UpdateUserUsecase(repo_mock)
            first_user = repo_mock.users_list[0]

            user_name_before = first_user.name

            updated_user = usecase(user_id=first_user.user_id, new_name=user_name_before)

    def test_update_user_name_with_invalid_name(self):
        with pytest.raises(EntityError):
            repo_mock = UserRepositoryMock()
            usecase = UpdateUserUsecase(repo_mock)
            first_user = repo_mock.users_list[0]

            updated_user = usecase(user_id=first_user.user_id, new_name="L")

    # def test_update_user_email(self):
    #     repo_mock = UserRepositoryMock()
    #     usecase = UpdateUserUsecase(repo_mock)
    #     first_user = repo_mock.users_list[0]
    #
    #     user_name_before = first_user.name
    #
    #     updated_user = usecase(user_id=first_user.user_id, new_email="jao.brancas@maua.br")
    #
    #     assert first_user.name == user_name_before
    #     assert first_user.email == "jao.brancas@maua.br"

    # def test_update_user_email_with_same_email(self):
    #     with pytest.raises(DuplicatedItem):
    #         repo_mock = UserRepositoryMock()
    #         usecase = UpdateUserUsecase(repo_mock)
    #         first_user = repo_mock.users_list[0]
    #
    #         user_email_before = first_user.email
    #
    #         updated_user = usecase(user_id=first_user.user_id, new_email=user_email_before)

    # def test_update_user_email_with_invalid_email(self):
    #     with pytest.raises(EntityError):
    #         repo_mock = UserRepositoryMock()
    #         usecase = UpdateUserUsecase(repo_mock)
    #         first_user = repo_mock.users_list[0]
    #
    #         updated_user = usecase(user_id=first_user.user_id, new_email="@gmail.com")


