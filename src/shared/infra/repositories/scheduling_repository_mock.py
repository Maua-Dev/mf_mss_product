from typing import List, Optional
from src.shared.domain.entities.scheduling import Scheduling
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.repositories.scheduling_repository_interface import ISchedulingRepository


class SchedulingRepositoryMock(ISchedulingRepository):
    schedulings: List[Scheduling]

    def __init__(self):
        self.schedulings = [
            Scheduling(initial_time=100, end_time=200, restaurant=RESTAURANT.RESTAURANT_A, accepted_reservation=True),
            Scheduling(initial_time=300, end_time=400, restaurant=RESTAURANT.RESTAURANT_B, accepted_reservation=False),
            Scheduling(initial_time=500, end_time=600, restaurant=RESTAURANT.RESTAURANT_C, accepted_reservation=True)
        ]

    def create_scheduling(self, scheduling: Scheduling) -> Scheduling:
        self.schedulings.append(scheduling)
        return scheduling

    def get_all_scheduling_by_restaurant(self, restaurant: RESTAURANT) -> List[Scheduling]:
        return [scheduling for scheduling in self.schedulings if scheduling.restaurant == restaurant]

    def get_scheduling_by_id(self, scheduling_id: str) -> Optional[Scheduling]:
        for scheduling in self.schedulings:
            if scheduling.scheduling_id == scheduling_id:
                return scheduling
        return None

    def update_scheduling(self, scheduling_id: str, new_initial_time: Optional[int] = None,
                          new_end_time: Optional[int] = None,
                          new_accepted_reservation: Optional[bool] = None):
        scheduling_to_update = self.get_scheduling_by_id(scheduling_id)
        if scheduling_to_update:
            if new_initial_time is not None:
                scheduling_to_update.initial_time = new_initial_time
            if new_end_time is not None:
                scheduling_to_update.end_time = new_end_time
            if new_accepted_reservation is not None:
                scheduling_to_update.accepted_reservation = new_accepted_reservation
            return scheduling_to_update
        return None

    def delete_scheduling(self, scheduling_id: str) -> Optional[Scheduling]:
        scheduling_to_delete = self.get_scheduling_by_id(scheduling_id)
        if scheduling_to_delete:
            self.schedulings.remove(scheduling_to_delete)
            return scheduling_to_delete
        return None