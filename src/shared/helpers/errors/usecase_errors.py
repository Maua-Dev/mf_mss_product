from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.base_error import BaseError

class OrderCantBeUpdated(BaseError):
    def __init__(self):
        super().__init__(f"You can't update a order after it's preparing has started")


class ProducutsListCantBeEmpty(BaseError):
    def __init__(self):
        super().__init__(f"Products list can't be empty")
        
class NoItemsFound(BaseError):
    def __init__(self, message: str):
        super().__init__(f'No items found for {message}')

class OrderAlreadyPreparing(BaseError):
    def __init__(self):
        super().__init__(f'The order is already preparing')


class DuplicatedItem(BaseError):
    def __init__(self, message: str):
        super().__init__(f'The item alredy exists for this {message}')


class UnecessaryUpdate(BaseError):
    def __init__(self, message: str):
        super().__init__(f'The value for {message} is already the new one')


class UserNotAllowed(BaseError):
    def __init__(self):
        super().__init__(f'That type of user has no permission for that action')


class UserNotRelatedToRestaurant(BaseError):
    def __init__(self, restaurant: RESTAURANT):
        super().__init__(f'User has no permission in {restaurant.value} restaurant')


class UnregisteredUser(BaseError):
    def __init__(self):
        super().__init__(f'That user is not registered')


class ForbiddenAction(BaseError):
    def __init__(self, message: str):
        super().__init__(f'That action is forbidden for this {message}')


class UnregisteredEmployee(BaseError):
    def __init__(self):
        """This error appears when there is a user which role is OWNER or SELLER and still doesn't have a restaurant assigned."""
        super().__init__(f'This employee is unregistered.')


class UserNotOrderOwner(BaseError):
    def __init__(self):
        super().__init__(f'This user is not the owner of this order.')


class WrongTypeRouteKey(BaseError):
    def __init__(self, message: str):
        super().__init__(f"Field {message} is not a acceptable route_key value, must be $connect or $disconnect")


class UserNotOrderOwner(BaseError):
    def __init__(self):
        super().__init__("The user_id does not match with the inserted order_id")

class OrderAlreadyHaveFeedback(BaseError):
    def __init__(self):
        super().__init__("This order have already been evaluated")

class FeedbackNotAllowed(BaseError):
    def __init__(self):
        super().__init__("Evaluate the order of its same restaurant")

