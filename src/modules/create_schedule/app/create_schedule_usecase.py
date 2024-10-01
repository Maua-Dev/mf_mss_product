from datetime import time

from src.shared.domain.entities.schedule import Schedule

from src.shared.domain.enums.role_enum import ROLE

from src.shared.domain.enums.restaurant_enum import RESTAURANT

from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository

from src.shared.helpers.errors.usecase_errors import DuplicatedItem, UnregisteredUser, UserNotAllowed

class CreateScheduleUsecase:
    def __init__(self, repo_schedule: IOrderRepository, repo_user: IUserRepository):
        self.repo_schedule = repo_schedule
        self.repo_user = repo_user

    def __call__(self, schedule_id: str, initial_time: time, end_time: time, restaurant: RESTAURANT, accepted_reservation: bool, user_id: str) -> Schedule:

        user = self.repo_user.get_user_by_id(user_id)

        if not user:
            raise UnregisteredUser()

        if user.role not in [ROLE.OWNER, ROLE.ADMIN, ROLE.SELLER]:
            raise UserNotAllowed()
        
        if user.restaurant is None:
            raise UserNotAllowed()

        schedules = self.repo_schedule.get_all_schedules_by_restaurant(restaurant)
        for schedule in schedules:
            if schedule.initial_time == initial_time and schedule.end_time == end_time: #verifica se agendamento atual tem o mesmo intervalo de tempo do novo agendamento
                raise DuplicatedItem(f'Schedule already exists for the given time interval in restaurant {restaurant}')
            
        if self.repo_schedule.get_schedule_by_id(schedule_id) is not None:
                raise DuplicatedItem(f'Schedule with id {schedule_id} already exists')
        
        schedule = Schedule(
            schedule_id=schedule_id,
            initial_time=initial_time,
            end_time=end_time,
            restaurant=restaurant,
            accepted_reservation=accepted_reservation
        )

        return self.repo_schedule.create_schedule(schedule)