import pytest
from src.modules.get_all_schedules_by_restaurant.app.get_all_schedules_by_restaurant_usecase import GetAllSchedulesByRestaurantUseCase
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class Test_GetAllSchedulesByRestaurantUseCase:
    def test_get_all_schedules_by_restaurant_use_case(self):
        repo_user = UserRepositoryMock()
        repo_order = OrderRepositoryMock()
        usecase = GetAllSchedulesByRestaurantUseCase(repo_user, repo_order)

        get_all_schedules = usecase.execute(user_id = '93bc6ada-c0d1-7054-66ab-e17414c48ae5', restaurant=RESTAURANT.CANTINA_DO_MOLEZA )

        assert len(get_all_schedules) == 3
