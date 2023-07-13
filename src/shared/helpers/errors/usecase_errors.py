
from src.shared.helpers.errors.base_error import BaseError

class NoItemsFound(BaseError):
    def __init__(self, message: str):
        super().__init__(f'No items found for {message}')

class DuplicatedItem(BaseError):
    def __init__(self, message: str):
        super().__init__(f'The item alredy exists for this {message}')

class UnecessaryUpdate(BaseError):
    def __init__(self, message: str):
        super().__init__(f'The value for {message} is already the new one')

class UserNotAllowed(BaseError):
    def __init__(self):
        super().__init__(f'That type of user has no permission for that action')       

class ForbiddenAction(BaseError):
    def __init__(self, message: str):
        super().__init__(f'That action is forbidden for this {message}')

