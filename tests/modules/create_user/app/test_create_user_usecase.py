import pytest

from src.modules.create_user.app.create_user_usecase import CreateUserUsecase
from src.shared.helpers.errors.usecase_errors import DuplicatedItem
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_CreateUserUsecase:

    def test_create_user(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)

        user = usecase(name="Rodas Morales", email="rodrigo.morales@gmail.com", user_id="93bc6ada-c0d1-7054-66ab-e17414c48ag7")

        assert repo.users_list[-1] == user
        assert user.photo == None

    def test_create_user_duplicated_user_id(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)

        with pytest.raises(DuplicatedItem):
            user = usecase(name="Rodrigo", email="rodrigo.morales@gmail.com", user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3")
        