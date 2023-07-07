from src.shared.helpers.errors.usecase_errors import NoItemsFound
import pytest
from src.shared.helpers.errors.domain_errors import EntityError
from src.modules.delete_user.app.delete_user_usecase import DeleteUserUsecase
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_DeleteUserUsecase:
    def test_delete_user_usecase(self):
        repo = UserRepositoryMock()
        usecase = DeleteUserUsecase(repo=repo)
        lenBefore = len(repo.users_list)

        user_id = "93bc6ada-c0d1-7054-66ab-e17414c48ae3"

        user = usecase(user_id=user_id)

        assert len(repo.users_list) == lenBefore - 1

    def test_delete_user_invalid_type(self):
        repo = UserRepositoryMock()
        usecase = DeleteUserUsecase(repo=repo)

        with pytest.raises(EntityError):
            user = usecase(user_id=666)

    def test_delete_user_not_found(self):
        repo = UserRepositoryMock()
        usecase = DeleteUserUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            user = usecase(user_id="6d6b38c0-927d-4c43-93b7-b33ea9278cma")