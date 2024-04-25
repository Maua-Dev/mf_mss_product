import pytest

from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError


class TestSchedule:
    def test_schedule(self):
        schedule = Schedule(
            schedule_id="8a57336f-4177-4dbd-80d5-93b4bdfac4af",
            initial_time=7.0,
            end_time=20.0,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            accepted_reservation=True
        )

        assert type(schedule) == Schedule
        assert schedule.schedule_id == "8a57336f-4177-4dbd-80d5-93b4bdfac4af"
        assert schedule.initial_time == 7.0
        assert schedule.end_time == 20.0
        assert schedule.restaurant == RESTAURANT.SOUZA_DE_ABREU
        assert schedule.accepted_reservation is True

    def test_invalid_id(self):
        with pytest.raises(EntityError):
            schedule = Schedule(
                schedule_id=123,
                initial_time=7.0,
                end_time=20.0,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                accepted_reservation=True
            )

    def test_negative_time(self):
        with pytest.raises(EntityError):
            schedule = Schedule(
                schedule_id="8a57336f-4177-4dbd-80d5-93b4bdfac4af",
                initial_time=-7.0,
                end_time=20.0,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                accepted_reservation=True
            )

    def test_end_time_before_initial_time(self):
        with pytest.raises(EntityError):
            schedule = Schedule(
                schedule_id="8a57336f-4177-4dbd-80d5-93b4bdfac4af",
                initial_time=20.0,
                end_time=7.0,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                accepted_reservation=True
            )

    def test_invalid_restaurant(self):
        with pytest.raises(EntityError):
            schedule = Schedule(
                schedule_id="8a57336f-4177-4dbd-80d5-93b4bdfac4af",
                initial_time=7.0,
                end_time=20.0,
                restaurant="Invalid Restaurant",
                accepted_reservation=True
            )

    def test_invalid_accepted_reservation(self):
        with pytest.raises(EntityError):
            schedule = Schedule(
                schedule_id="8a57336f-4177-4dbd-80d5-93b4bdfac4af",
                initial_time=7.0,
                end_time=20.0,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                accepted_reservation="True"
            )

