import abc
from datetime import time
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError


class Schedule(abc.ABC):
    def __init__(self,
                 schedule_id: str,
                 initial_time: time,
                 end_time: time,
                 restaurant: RESTAURANT,
                 accepted_reservation: bool = False
                 ):

        if not isinstance(initial_time, time):
            raise EntityError("initial_time")
        if not isinstance(end_time, time):
            raise EntityError("end_time")
        if initial_time > end_time:
            raise EntityError("initial_time")

        self.initial_time = initial_time
        self.end_time = end_time

        if not isinstance(restaurant, RESTAURANT):
            raise EntityError("restaurant")
        self.restaurant = restaurant

        if not isinstance(schedule_id, str):
            raise EntityError("schedule_id")
        self.schedule_id = schedule_id

        if not isinstance(accepted_reservation, bool):
            raise EntityError("accepted_reservation")
        self.accepted_reservation = accepted_reservation

    def to_dict(self) -> dict:
        return {
            "schedule_id": self.schedule_id,
            "initial_time": self.initial_time,
            "end_time": self.end_time,
            "restaurant": self.restaurant,
            "accepted_reservation": self.accepted_reservation
        }

    def __repr__(self):
        return f"Schedule(schedule_id={self.schedule_id}, initial_time={self.initial_time}, end_time={self.end_time}, restaurant={self.restaurant}, accepted_reservation={self.accepted_reservation})"
