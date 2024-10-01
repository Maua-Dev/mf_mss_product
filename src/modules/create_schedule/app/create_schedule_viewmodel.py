from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.enums.restaurant_enum import RESTAURANT

class ScheduleViewModel:
    schedule: Schedule

    def __init__(self, schedule: Schedule):
        self.schedule = schedule

    def to_dict(self) -> Schedule:
        return {
            "schedule_id": self.schedule.schedule_id,
            "initial_time": self.schedule.initial_time.strftime("%H:%M:%S"),
            "end_time": self.schedule.end_time.strftime("%H:%M:%S"),
            "restaurant": self.schedule.restaurant,
            "accepted_reservation": self.schedule.accepted_reservation
        }

class CreateScheduleViewmodel:
    def __init__(self, schedule: Schedule):
        self.schedule = ScheduleViewModel(schedule)

    def to_dict(self) -> dict:
        return{
            "schedule": self.schedule.to_dict(),
            "message" : "Schedule created successfully"
        }