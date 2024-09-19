from typing import List, Optional
from src.shared.domain.entities.schedule import Schedule
from datetime import time
from src.shared.domain.enums.restaurant_enum import RESTAURANT

class ScheduleViewModel:
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
            "schedule_id": self.get_all_schedules.schedule_id,
            "initial_time": self.get_all_schedules.initial_time,
            "end_time": self.get_all_schedules.end_time,
            "restaurant": self.get_all_schedules.restaurant,
            "accepted_reservation": self.get_all_schedules.accepted_reservation
        }

class GetScheduleViewModel:
    schedule: ScheduleViewModel

    def __init__(self, schedule: Schedule):
        self.schedule = ScheduleViewModel(schedule)

    def to_dict(self):
        return {
            'schedule': self.schedule.to_dict()
        }
    
class GetAllSchedulesViewmodel:
    schedules: List[GetScheduleViewModel]
    #cria uma variavel schedule que recebe uma lista de Schedules

    def __init__(self, schedules: List[tuple[Schedule]]):
        #inicia um metodo que vai receber uma lista de tuplas da classe schedule
        self.schedules = [GetScheduleViewModel(schedule) for schedule in schedules]
        #a cada item da minha variavel declara incialmente no metodo vai chamar o metodo GetScheduleViewModel 
    
    def to_dict(self):
        return {
            'schedules': [schedule.to_dict() for schedule in self.schedules]
        }

    #def to_dict(self) -> dict:
        return {
            "schedule_id": self.get_all_schedules.schedule_id,
            "initial_time": self.get_all_schedules.initial_time,
            "end_time": self.get_all_schedules.end_time,
            "restaurant": self.get_all_schedules.restaurant,
            "accepted_reservation": self.get_all_schedules.accepted_reservation
        }