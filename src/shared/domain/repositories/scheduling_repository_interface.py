from abc import ABC, abstractmethod
from typing import List, Optional
from src.shared.domain.entities.scheduling import Scheduling
from src.shared.domain.enums.restaurant_enum import RESTAURANT

class ISchedulingRepository(ABC):

    @abstractmethod
    def create_scheduling(self, scheduling: Scheduling) -> Scheduling:
        pass

    @abstractmethod
    def get_all_scheduling_by_restaurant(self, restaurant: RESTAURANT) -> List[Scheduling]:
        pass

    @abstractmethod
    def get_scheduling_by_id(self, scheduling_id: str) -> Optional[Scheduling]:
        pass

    @abstractmethod
    def update_scheduling(self, scheduling_id: str, new_initial_time: Optional[int] = None,
                         new_end_time: Optional[int] = None,
                         new_accepted_reservation: Optional[bool] = None):
        pass
