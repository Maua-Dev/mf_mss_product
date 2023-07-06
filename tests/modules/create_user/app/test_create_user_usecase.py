import pytest

from src.modules.create_user.app.create_user_usecase import CreateUserUsecase
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_CreateUserUsecase:

    def test_create_user(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)

        user = usecase(name="Rodrigo", email="rodrigo.morales@gmail.com", role=ROLE.USER, restaurant=None, user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3")

        assert repo.users_list[-1] == user

    def test_create_user_invalid_role(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)

        with pytest.raises(EntityError):
            user = usecase(name="Rodrigo", email="rodrigo.morales@gmail.com", role=ROLE.ADMIN, restaurant=None, user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3")
        
    def test_create_user_restaurant_not_none(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo)

        with pytest.raises(EntityError):
            user = usecase(name="Rodrigo", email="rodrigo.morales@gmail.com", role=ROLE.USER, restaurant=RESTAURANT.CANTINA_DO_MOLEZA, user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3")