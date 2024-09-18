from typing import List

from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository

from src.shared.helpers.errors.usecase_errors import UnregisteredEmployee, UnregisteredUser, UserNotAllowed

class GetScheduleByIdUsecase:
    def __init__(self, repo_schedule: IOrderRepository):
        self.repo_schedule = repo_schedule

    def __call__(self, schedule_id: str) -> List[Schedule]:
        
        schedule = self.repo_schedule.get_schedule_by_id(schedule_id = schedule_id)

        if schedule is None:
            raise UnregisteredUser()
        
        if schedule.restaurant is None:
            raise UnregisteredEmployee()

        return schedule