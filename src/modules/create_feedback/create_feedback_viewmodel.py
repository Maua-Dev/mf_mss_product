from src.shared.domain.entities.feedback import Feedback
from src.shared.domain.enums.restaurant_enum import RESTAURANT

class FeedbackViewmodel:
    order_id: str
    user_id: str
    restaurant: RESTAURANT
    value: int

    def __init__(self, feedback: Feedback):
        self.order_id = feedback.order_id
        self.user_id = feedback.user_id
        self.restaurant = feedback.restaurant
        self.value = feedback.value

    def to_dict(self) -> dict:
        return{
            "order_id": self.order_id,
            "user_id": self.user_id,
            "restaurant": self.restaurant.value,
            "value": self.value,
        }

class CreateFeedbackViewmodel:

    def __init__(self, feedback: Feedback):
        self.feedback = FeedbackViewmodel(feedback)

    def to_dict(self) -> dict:
        return {
            "feedback": self.feedback.to_dict(),
            "message": "the feedback was created"
        }