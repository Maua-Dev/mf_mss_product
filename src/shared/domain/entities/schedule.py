import abc
from datetime import time
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError


class Schedule(abc.ABC):
    def __init__(self,
                 schedule_id: str,
                 hour_initial_time: int,
                 minute_initial_time: int,
                 hour_end_time: int,
                 minute_end_time: int,
                 restaurant: RESTAURANT,
                 accepted_reservation: bool
                 ):

        self.validate_hour(hour_initial_time)
        self.validate_hour(hour_end_time)
        self.validate_minute(minute_initial_time)
        self.validate_minute(minute_end_time)

        initial_time = time(hour=hour_initial_time, minute=minute_initial_time)
        end_time = time(hour=hour_end_time, minute=minute_end_time)

        if initial_time > end_time:
            raise EntityError("initial_time")

        self.initial_time = initial_time
        self.end_time = end_time

        if not isinstance(restaurant, RESTAURANT):
            raise EntityError("restaurant")
        self.restaurant = restaurant

        if type(accepted_reservation) != bool:
            raise EntityError("accepted_reservation")
        self.accepted_reservation = accepted_reservation

        if type(schedule_id) != str:
            raise EntityError("schedule_id")
        self.schedule_id = schedule_id

    def __repr__(self):
        return f"Schedule(schedule_id={self.schedule_id}, initial_time={self.initial_time}, end_time={self.end_time}, restaurant={self.restaurant}, accepted_reservation={self.accepted_reservation})"

    @staticmethod
    def validate_hour(hour: int):
        if type(hour) != int:
            raise EntityError("hour")
        if hour < 0:
            raise EntityError("hour")
        if hour > 23:
            raise EntityError("hour")

    @staticmethod
    def validate_minute(minute: int):
        if type(minute) != int:
            raise EntityError("minute")
        if minute < 0:
            raise EntityError("minute")
        if minute > 59:
            raise EntityError("minute")
