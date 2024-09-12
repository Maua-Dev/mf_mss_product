import pytest

from datetime import time
from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterTimeError 

class Test_Schedule:
    def test_schedule(self):
        schedule = Schedule(
            schedule_id="1efc0e1a-24ed-4041-a4a0-fe5633711a3f",
            initial_time=time(7, 0),
            end_time=time(8, 0),
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            accepted_reservation=True,
        )

        assert type(schedule) == Schedule
        assert schedule.schedule_id == "1efc0e1a-24ed-4041-a4a0-fe5633711a3f"
        assert schedule.initial_time == time(7, 0)
        assert schedule.end_time == time(8, 0)
        assert schedule.restaurant == RESTAURANT.SOUZA_DE_ABREU
        assert schedule.accepted_reservation == True

    def test_accepted_reservation_is_false(self):
        schedule = Schedule(
            schedule_id="1efc0e1a-24ed-4041-a4a0-fe5633711a3f",
            initial_time=time(7, 0),
            end_time=time(8, 0),
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            accepted_reservation=False
        )

        assert type(schedule) == Schedule
        assert schedule.schedule_id =="1efc0e1a-24ed-4041-a4a0-fe5633711a3f"
        assert schedule.initial_time ==time(7,0)
        assert schedule.end_time == time(8,0)
        assert schedule.restaurant == RESTAURANT.SOUZA_DE_ABREU
        assert schedule.accepted_reservation == False

    def test_invalid_schedule_id(self):
        try:        
            schedule = Schedule(
                schedule_id=111,
                initial_time=time(7, 0),
                end_time=time(8, 0),
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                accepted_reservation=True
            )
        except EntityError as error:
            assert str(error)
        
    def test_invalid_initial_time(self):
        try:
            schedule = Schedule(
                schedule_id="1efc0e1a-24ed-4041-a4a0-fe5633711a3f",
                initial_time=111,
                end_time=time(8, 0),
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                accepted_reservation=True
            )
        except EntityError as error:
            assert str(error)

    def test_invalid_negative_inital_time(self):
        with pytest.raises(ValueError):
            schedule = Schedule(
                schedule_id="1efc0e1a-24ed-4041-a4a0-fe563371a3f",
                initial_time=time(-1, 0),
                end_time=time(8, 0),
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                accepted_reservation=True
            )

    def test_invalid_end_time(self):
        try:
            schedule = Schedule(
                schedule_id="1efc0e1a-24ed-4041-a4a0-fe563371a3f",
                initial_time=time(7, 0),
                end_time=111,
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                accepted_reservation=True
            )
        except EntityError as error:
            assert str(error)

    def test_invalid_negative_end_time(self):
        with pytest.raises(ValueError):
            schedule = Schedule(
                schedule_id="1efc0e1a-24ed-4041-a4a0-fe563371a3f",
                initial_time=time(7, 0),
                end_time=time(-1, 0),
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                accepted_reservation=True
            )

    def test_end_time_before_initial_time(self):
        with pytest.raises(EntityParameterTimeError):        
            schedule = Schedule(
                schedule_id="1efc0e1a-24ed-4041-a4a0-fe563371a3f",
                initial_time=time(8, 0),
                end_time=time(7, 0),
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                accepted_reservation=True
            )
        
    def test_invalid_restaurant(self):
        try:
            schedule = Schedule(
                schedule_id="1efc0e1a-24ed-4041-a4a0-fe563371a3f",
                initial_time=time(7, 0),
                end_time=time(8, 0),
                restaurant="Restaurant", 
                accepted_reservation=True
            )
        except EntityError as error:
            assert str(error)

    def test_invalid_accepted_reservation(self):
        try:
            schedule = Schedule(
                schedule_id="1efc0e1a-24ed-4041-a4a0-fe563371a3f",
                initial_time=time(7, 0),
                end_time=time(8, 0),
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                accepted_reservation="True"
            )
        except EntityError as error:
            assert str(error)

