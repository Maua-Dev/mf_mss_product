import abc
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError


class Schedule(abc.ABC):
    def __init__(self,
                 schedule_id: str,
                 initial_time: float,
                 end_time: float,
                 restaurant: RESTAURANT,
                 accepted_reservation: bool
                 ):
        self.validate_initial_time(initial_time, end_time)
        self.initial_time = initial_time

        self.validate_end_time(end_time, initial_time)
        self.end_time = end_time

        if not isinstance(restaurant, RESTAURANT):
            raise EntityError("restaurant")
        self.restaurant = restaurant

        if type(accepted_reservation) != bool:
            raise EntityError("accepted_reservation")
        self.accepted_reservation = accepted_reservation

        if (type(schedule_id) != str):
            raise EntityError("schedule_id")
        self.schedule_id = schedule_id

    def validate_initial_time(self, initial_time: float, end_time: float):
        if type(initial_time) != float:
            raise EntityError("initial_time")
        if initial_time > 24:
            raise EntityError("initial_time")
        if initial_time < 0:
            raise EntityError("initial_time")
        if initial_time > end_time:
            raise EntityError("initial_time")

    def validate_end_time(self, end_time: float, initial_time: float):
        if type(end_time) != float:
            raise EntityError("end_time")
        if end_time > 24:
            raise EntityError("end_time")
        if end_time < 0:
            raise EntityError("end_time")
        if end_time < initial_time:
            raise EntityError("end_time")

    def __repr__(self):
        return f"Schedule(schedule_id={self.schedule_id}, initial_time={self.initial_time}, end_time={self.end_time}, restaurant={self.restaurant}, accepted_reservation={self.accepted_reservation})"
