from typing import List

from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository

from src.shared.helpers.errors.usecase_errors import UnregisteredEmployee, UnregisteredUser, UserNotAllowed, NoItemsFound

class GetScheduleByIdUsecase:
    def __init__(self, repo_schedule: IOrderRepository, repo_user: IUserRepository):
        self.repo_schedule = repo_schedule
        self.repo_user = repo_user

    def __call__(self, user_id: str, schedule_id: str):
        schedule = self.repo_schedule.get_schedule_by_id(schedule_id = schedule_id)
        user = self.repo_user.get_user_by_id(user_id = user_id)
        
        if user is None:
            raise UnregisteredUser()

        if schedule is None:
            raise NoItemsFound(f"schedule with id: {schedule_id}")
        

        
        return schedule