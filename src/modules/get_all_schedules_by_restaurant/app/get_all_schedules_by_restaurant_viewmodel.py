from typing import List, Optional
from src.shared.domain.entities.schedule import Schedule
from datetime import time
from src.shared.domain.enums.restaurant_enum import RESTAURANT

class ScheduleViewmodel:
    schedule_id: str
    initial_time: time
    end_time: time
    restaurant: RESTAURANT
    accepted_reservation: bool

    def __init__(self, schedule: Schedule):
        self.schedule_id = schedule.schedule_id
        self.initial_time = schedule.initial_time
        self.end_time = schedule.end_time
        self.restaurant = schedule.restaurant
        self.accepted_reservation = schedule.accepted_reservation

    def to_dict(self):
        return {
            "schedule_id": self.schedule_id,
            "initial_time": self.initial_time,
            "end_time": self.end_time,
            "restaurant": self.restaurant.value,
            "accepted_reservation": self.accepted_reservation
        }
    
class GetAllSchedulesByRestaurantViewmodel:
    schedules: List[Schedule]

    def __init__(self, schedules: List[Schedule]):
        self.schedules = schedules
    
    def to_dict(self):
        return {
            'schedules': [ScheduleViewmodel(schedule).to_dict() for schedule in self.schedules],
            'message': "the schedules were retrieved"
        }