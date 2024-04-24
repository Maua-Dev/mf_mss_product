from enum import Enum
from typing import List, Optional
import abc
import pytest


class RESTAURANT(Enum):
    SOUZA_DE_ABREU = "SOUZA_DE_ABREU"
    HORA_H = "HORA_H"
    CANTINA_DO_MOLEZA = "CANTINA_DO_MOLEZA"


class EntityError(Exception):
    pass


class Scheduling(abc.ABC):
    initial_time: int
    end_time: int
    restaurant: RESTAURANT
    accepted_reservation: bool

    def __init__(self,
                 scheduling_id: str,
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

        self.scheduling_id = scheduling_id

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

    def update(self, initial_time: Optional[int] = None, end_time: Optional[int] = None,
           accepted_reservation: Optional[bool] = None):
        if initial_time is not None:
            self.validate_initial_time(initial_time, self.end_time)
            self.initial_time = initial_time
        if end_time is not None:
            self.validate_end_time(end_time, self.initial_time)
            self.end_time = end_time
        if accepted_reservation is not None:
            if type(accepted_reservation) != bool:
                raise EntityError("accepted_reservation")
            self.accepted_reservation = accepted_reservation


    def delete(self):
        self.is_deleted = True


class SchedulingRepositoryMock:
    schedulings: List[Scheduling]

    def __init__(self):
        self.schedulings = [
            Scheduling(scheduling_id="1", initial_time=100, end_time=200,
                       restaurant=RESTAURANT.SOUZA_DE_ABREU, accepted_reservation=True),
            Scheduling(scheduling_id="2", initial_time=300, end_time=400,
                       restaurant=RESTAURANT.HORA_H, accepted_reservation=False),
            Scheduling(scheduling_id="3", initial_time=500, end_time=600,
                       restaurant=RESTAURANT.CANTINA_DO_MOLEZA, accepted_reservation=True)
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


class TestScheduling:
    def test_scheduling(self):
        scheduling = Scheduling(
            scheduling_id="8a57336f-4177-4dbd-80d5-93b4bdfac4af",
            initial_time=100,
            end_time=200,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            accepted_reservation=True
        )

        assert type(scheduling) == Scheduling
        assert scheduling.scheduling_id == "8a57336f-4177-4dbd-80d5-93b4bdfac4af"
        assert scheduling.initial_time == 100
        assert scheduling.end_time == 200
        assert scheduling.restaurant == RESTAURANT.SOUZA_DE_ABREU
        assert scheduling.accepted_reservation is True

    def test_invalid_id(self):
        with pytest.raises(EntityError):
            scheduling = Scheduling(
                scheduling_id=123,
                initial_time=100,
                end_time=200,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                accepted_reservation=True
            )

    def test_negative_time(self):
        with pytest.raises(EntityError):
            scheduling = Scheduling(
                scheduling_id="8a57336f-4177-4dbd-80d5-93b4bdfac4af",
                initial_time=-100,
                end_time=200,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                accepted_reservation=True
            )

    def test_end_time_before_initial_time(self):
        with pytest.raises(EntityError):
            scheduling = Scheduling(
                scheduling_id="8a57336f-4177-4dbd-80d5-93b4bdfac4af",
                initial_time=300,
                end_time=200,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                accepted_reservation=True
            )

    def test_invalid_restaurant(self):
        with pytest.raises(EntityError):
            scheduling = Scheduling(
                scheduling_id="8a57336f-4177-4dbd-80d5-93b4bdfac4af",
                initial_time=100,
                end_time=200,
                restaurant="Invalid Restaurant",
                accepted_reservation=True
            )

    def test_invalid_accepted_reservation(self):
        with pytest.raises(EntityError):
            scheduling = Scheduling(
                scheduling_id="8a57336f-4177-4dbd-80d5-93b4bdfac4af",
                initial_time=100,
                end_time=200,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                accepted_reservation="True"
            )

    def test_update_scheduling(self):
        scheduling = Scheduling(
            scheduling_id="8a57336f-4177-4dbd-80d5-93b4bdfac4af",
            initial_time=100,
            end_time=200,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            accepted_reservation=True
        )

        scheduling.update(initial_time=150, end_time=250, accepted_reservation=False)

        assert scheduling.initial_time == 150
        assert scheduling.end_time == 250
        assert scheduling.accepted_reservation is False

    def test_invalid_update(self):
        scheduling = Scheduling(
            scheduling_id="8a57336f-4177-4dbd-80d5-93b4bdfac4af",
            initial_time=100,
            end_time=200,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            accepted_reservation=True
        )

        with pytest.raises(EntityError):
            scheduling.update(scheduling_id="invalid_id")

    def test_delete_scheduling(self):
        scheduling = Scheduling(
            scheduling_id="8a57336f-4177-4dbd-80d5-93b4bdfac4af",
            initial_time=100,
            end_time=200,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            accepted_reservation=True
        )

        scheduling.delete()

        assert scheduling.is_deleted is True
