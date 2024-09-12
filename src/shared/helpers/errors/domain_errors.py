from src.shared.helpers.errors.base_error import BaseError


class EntityError(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Field {message} is not valid')


class EntityParameterExcededMaximumValue(BaseError):
    def __init__(self, field: str, maximum_value: str):
        super().__init__(f'Field {field} must be equal or less than {maximum_value}')

class EntityParameterHaveMinValue(BaseError):
    def __init__(self, field: str, minimum_value: str):
        super().__init__(f'Field {field} must be equal or more than {minimum_value}')

class EntityParameterTypeError(EntityError):
    def __init__(self, message: str):
        super().__init__(message)
        self.__message = message

    @property
    def message(self):
        return self.__message
    
class EntityParameterTimeError(BaseError):
    def __init__(self, initial_time: str, end_time: str):
        super().__init__(f'Initial time {initial_time} must be less than or equal to end time {end_time}')

class EntityParameterError(EntityError):
    def __init__(self, message: str):
        super().__init__(message)
        self.__message = message

    @property
    def message(self):
        return self.__message
