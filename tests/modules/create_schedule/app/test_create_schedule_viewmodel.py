
from datetime import time

from src.modules.create_schedule.app.create_schedule_viewmodel import CreateScheduleViewmodel
from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class Test_CreateScheduleViewmodel:
    def test_create_schedule_viewmodel(self):

        schedule = Schedule(
            schedule_id="c78f7935-6cdd-48cf-af87-b6163bcd59a8",
            initial_time=time(hour=8, minute=0),
            end_time=time(hour=10, minute=0),
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            accepted_reservation=True
        )

        create_schedule_viewmodel = CreateScheduleViewmodel(schedule=schedule).to_dict()

        excepted = {
            "schedule": {
                "schedule_id": "c78f7935-6cdd-48cf-af87-b6163bcd59a8",
                "initial_time": "08:00:00",
                "end_time": "10:00:00",
                "restaurant": RESTAURANT.CANTINA_DO_MOLEZA,
                "accepted_reservation": True
            },
            "message": "Schedule created successfully"
        }
        
        assert excepted == create_schedule_viewmodel