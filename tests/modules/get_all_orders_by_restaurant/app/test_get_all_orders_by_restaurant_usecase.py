import pytest

from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.helpers.errors.usecase_errors import UnregisteredEmployee, UnregisteredUser, UserNotAllowed
from src.modules.get_all_orders_by_restaurant.app.get_all_orders_by_restaurant_usecase import \
    GetAllOrdersByRestaurantUsecase


class Test_GetAllOrdersByRestaurantUseCase:
    def test_get_all_orders_by_restaurant_usecase_with_order_id(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByRestaurantUsecase(repo_order, repo_user)
        orders = usecase(user_id=repo_user.users_list[3].user_id, exclusive_start_key=repo_order.orders[9].order_id)

        assert len(orders) == 3

    def test_get_all_orders_by_restaurant_usecase_without_order_id(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByRestaurantUsecase(repo_order, repo_user)
        orders = usecase(user_id=repo_user.users_list[3].user_id, exclusive_start_key=None)

        assert len(orders) == 7

    def test_get_all_orders_by_restaurant_unregisted_employee(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByRestaurantUsecase(repo_order, repo_user)

        with pytest.raises(UnregisteredEmployee):
            order = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", exclusive_start_key=None)

    def test_get_all_orders_by_restaurant_user_not_allowed(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByRestaurantUsecase(repo_order, repo_user)

        with pytest.raises(UserNotAllowed):
            order = usecase(user_id=repo_user.users_list[4].user_id, exclusive_start_key=None)

    def test_get_all_orders_by_restaurant_unregisted_user(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByRestaurantUsecase(repo_order, repo_user)

        with pytest.raises(UnregisteredUser):
            order = usecase(user_id="id", exclusive_start_key=None)
