from datetime import time

from src.shared.domain.entities.schedule import Schedule
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class ScheduleDynamoDto:
    def __init__(self, schedule_id: str, initial_time: str, end_time: str, restaurant: RESTAURANT, accepted_reservation: bool):
        self.partition_key = schedule_id
        self.initial_time = initial_time
        self.end_time = end_time
        self.restaurant = restaurant
        self.accepted_reservation = accepted_reservation

    @staticmethod
    def from_entity(schedule: Schedule) -> "ScheduleDynamoDto":
        """
        Parse data from Schedule to ScheduleDynamoDto
        """
        return ScheduleDynamoDto(
            schedule_id=schedule.schedule_id,
            initial_time=schedule.initial_time.isoformat(),
            end_time=schedule.end_time.isoformat(),
            restaurant=schedule.restaurant,
            accepted_reservation=schedule.accepted_reservation
        )

    def to_dynamo(self) -> dict:
        """
        Convert ScheduleDynamoDto to DynamoDB format
        """
        return {
            "schedule_id": self.partition_key,
            "initial_time": self.initial_time,
            "end_time": self.end_time,
            "restaurant": self.restaurant.value,
            "accepted_reservation": self.accepted_reservation
        }

    @staticmethod
    def from_dynamo(data: dict) -> "ScheduleDynamoDto":
        """
        Parse data from DynamoDB to ScheduleDynamoDto
        """
        return ScheduleDynamoDto(
            schedule_id=data["schedule_id"],
            initial_time=data["initial_time"],
            end_time=data["end_time"],
            restaurant=RESTAURANT(data["restaurant"]),
            accepted_reservation=data["accepted_reservation"]
        )

    def to_entity(self) -> Schedule:
        """
        Convert ScheduleDynamoDto to Schedule
        """
        initial_time = time.fromisoformat(self.initial_time)
        end_time = time.fromisoformat(self.end_time)
        return Schedule(
            schedule_id=self.partition_key,
            initial_time=initial_time,
            end_time=end_time,
            restaurant=self.restaurant,
            accepted_reservation=self.accepted_reservation
        )

