import pytest

from src.modules.get_schedule_by_id.app.get_schedule_by_id_usecase import \
    GetScheduleByIdUsecase
from src.shared.domain.entities.schedule import Schedule 
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.status_enum import STATUS
from src.shared.helpers.errors.usecase_errors import UserNotOrderOwner, UnregisteredUser, NoItemsFound
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

def get_items_for_tests():
    user_repo = UserRepositoryMock()
    schedule_repo = OrderRepositoryMock()

    return user_repo, schedule_repo, schedule_repo.schedules[-1]

class Test_GetScheduleByIdUsecase:
    def test_get_current_state(self):
        user_repo, schedule_repo, schedule = get_items_for_tests()
        user = user_repo.users_list[-1]
        usecase = GetScheduleByIdUsecase(repo_user=user_repo, repo_schedule=schedule_repo)

        response = usecase(schedule_id=schedule_repo.schedules[-1].schedule_id, user_id=user.user_id)

        assert type(response) == Schedule
        assert response == schedule_repo.schedules[-1]

    def test_raise_exception_when_schedule_doesnt_exist(self):
        user_repo, schedule_repo, schedule = get_items_for_tests()

        with pytest.raises(NoItemsFound):
            usecase = GetScheduleByIdUsecase(repo_user=user_repo, repo_schedule=schedule_repo)
            response = usecase(schedule_id="um id que não existe", user_id=user_repo.users_list[-1])
