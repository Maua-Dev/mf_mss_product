import abc
from datetime import time

from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterTimeError

class Restaurant(abc.ABC):
    name: str
    start_time: time
    end_time: time
    email: str

    def __init__(self, name: str, start_time: time, end_time: time, email: str):
        
        if type(name) != str:
            raise EntityError("name")
        self.name = name

        if not isinstance(start_time, time):
            raise EntityError("initial_time")

        if not isinstance(end_time, time):
            raise EntityError("end_time")
        
        self.start_time = start_time
        self.end_time = end_time

        if start_time > end_time:
            raise EntityParameterTimeError("end_time", "initial_time")
        
        if type(email) != str:
            raise EntityError("email")
        self.email = email
        
        def to_dict(self) -> dict:
            return {
                "name": self.name,
                "start_time": self.start_time,
                "end_time": self.end_time,
                "email": self.email
            }
        
        def __repr__(self) -> str:
            return f"name: {self.name}, start_time: {self.start_time},  end_time: {self.end_time}, email: {self.email}"
