import pytest
from src.modules.get_all_active_orders_by_restaurant.app.get_all_active_orders_by_restaurant_usecase import GetAllActiveOrdersByRestaurantUsecase
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.usecase_errors import UnregisteredEmployee, UnregisteredUser, UserNotAllowed
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllProductsGroupByRestaurantUsecase:
    def test_get_all_active_orders_by_restaurant_usecase(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllActiveOrdersByRestaurantUsecase(repo_order, repo_user)
        orders = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48af4")
        
        assert len(orders) == 4

    def test_get_all_active_orders_by_restaurant_unregisted_employee(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllActiveOrdersByRestaurantUsecase(repo_order, repo_user)

        with pytest.raises(UnregisteredEmployee):
            order = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3")
            
    def test_get_all_active_orders_by_restaurant_user_not_allowed(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllActiveOrdersByRestaurantUsecase(repo_order, repo_user)

        with pytest.raises(UserNotAllowed):
            order = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf")

    def test_get_all_active_orders_by_restaurant_unregisted_user(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllActiveOrdersByRestaurantUsecase(repo_order, repo_user)

        with pytest.raises(UnregisteredUser):
            order = usecase(user_id="id")