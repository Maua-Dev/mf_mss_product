import pytest
from src.modules.get_all_users_by_restaurant.app.get_all_users_by_restaurant_usecase import GetAllUsersByRestaurantUseCase
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser, UserNeedsRestaurant, UserNotAllowed
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class Test_GetAllUsersByRestaurantUseCase:
    def test_get_all_users_by_restaurant_use_case(self):
        repo_user = UserRepositoryMock()
        repo_order = OrderRepositoryMock()
        usecase = GetAllUsersByRestaurantUseCase(repo_user, repo_order)
        
        user = repo_user.users_list[3]
        user.role = ROLE.OWNER

        get_all_users_by_restaurant = usecase.__call__(user_id='93bc6ada-c0d1-7054-66ab-e17414c48af4')

        assert repo_user.users_list[3].user_id == get_all_users_by_restaurant[0].user_id
        assert repo_user.users_list[3].role == get_all_users_by_restaurant[0].role

    def test_get_all_users_by_restaurant_user_is_none(self):
        repo_user = UserRepositoryMock()
        repo_order = OrderRepositoryMock()
        usecase = GetAllUsersByRestaurantUseCase(repo_user, repo_order)

        user = repo_user.users_list[3]
        user.role = ROLE.OWNER

        with pytest.raises(UnregisteredUser):
            usecase.__call__(user_id=None)

    def test_get_all_users_by_restaurant_user_not_allowed(self):
        repo_user = UserRepositoryMock()
        repo_order = OrderRepositoryMock()
        usecase = GetAllUsersByRestaurantUseCase(repo_user, repo_order)

        user = repo_user.users_list[4]

        with pytest.raises(UserNotAllowed):
            usecase.__call__(user_id=user.user_id)

    def test_get_all_users_by_restaurant_user_restaurant_is_none(self):
        repo_user = UserRepositoryMock()
        repo_order = OrderRepositoryMock()
        usecase = GetAllUsersByRestaurantUseCase(repo_user, repo_order)

        user = repo_user.users_list[0]

        with pytest.raises(UserNeedsRestaurant):
            usecase.__call__(user_id=user.user_id)


        