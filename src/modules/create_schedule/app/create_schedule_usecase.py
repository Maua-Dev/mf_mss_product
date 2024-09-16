from datetime import time

from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.repositories.order_repository_interface import IOrderRepository
from src.shared.domain.enums.restaurant_enum import RESTAURANT

from src.shared.helpers.errors.usecase_errors import DuplicatedItem


class CreateScheduleUsecase:
    def __init__(self, repo: IOrderRepository):
        self.repo = repo

    def __call__(self, schedule_id: str, initial_time: time, end_time: time, restaurant: RESTAURANT, accepted_reservation: bool) -> Schedule:

        #!necessario fazer get_schedule_by_id
        # if(self.repo.get_schedule_by_id(schedule_id)):
        #     raise Exception("Schedule already exists")

        #!verificar se existe objeto schedule criado, no mesmo restaurante, no mesmo intervalo de tempo
        #? caso exista erro, levantar erro de duplicata - DuplicatedItem

        schedule = Schedule(
            schedule_id=schedule_id,
            initial_time=initial_time,
            end_time=end_time,
            restaurant=restaurant,
            accepted_reservation=accepted_reservation
        )

        return self.repo.create_schedule(schedule)