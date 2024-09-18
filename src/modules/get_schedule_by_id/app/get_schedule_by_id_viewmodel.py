from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.entities.order_product import OrderProduct
from typing import List, Optional
from datetime import datetime, time

from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS
from src.shared.domain.enums.action_enum import ACTION


class ScheduleByIdViewmodel:
    schedule_id : str
    initial_time : time
    end_time : time
    restaurant : RESTAURANT
    accepted_reservation : bool

    def __init__(self, schedule: Schedule):
        self.schedule_id = schedule.schedule_id
        self.initial_time = schedule.initial_time
        self.end_time = schedule.end_time
        self.restaurant = schedule.restaurant
        self.accepted_reservation = schedule.accepted_reservation

    def to_dict(self) -> dict:
        return {
            "schedule_id": self.schedule_id,
            "initial_time": self.initial_time,
            "end_time": self.end_time,
            "restaurant": self.restaurant,
            "accepted_reservation":self.accepted_reservation
        }

