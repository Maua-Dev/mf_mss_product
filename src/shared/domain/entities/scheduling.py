import abc
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError


class Scheduling(abc.ABC):
    initial_time: int
    end_time: int
    restaurant: RESTAURANT
    accepted_reservation: bool

    def __init__(self,
                 initial_time: int,
                 end_time: int,
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

    def validate_initial_time(self, initial_time: int, end_time: int):
        if type(initial_time) != int:
            raise EntityError("initial_time")
        if initial_time > end_time:
            raise EntityError("initial_time")

    def validate_end_time(self, end_time: int, initial_time: int):
        if type(end_time) != int:
            raise EntityError("end_time")
        if end_time < initial_time:
            raise EntityError("end_time")

    def __repr__(self):
        return f"Scheduling(initial_time={self.initial_time}, end_time={self.end_time}, restaurant={self.restaurant}, accepted_reservation={self.accepted_reservation})"