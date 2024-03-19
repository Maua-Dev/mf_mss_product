from decimal import Decimal
from src.shared.domain.entities.feedback import Feedback
from src.shared.domain.enums.restaurant_enum import RESTAURANT


class FeedbackDynamoDTO:
    order_id: str
    user_id: str
    restaurant: RESTAURANT
    value : int

    def __init__(self, order_id: str, user_id: str, restaurant: RESTAURANT, value: int):
        self.order_id = order_id
        self.user_id = user_id
        self.restaurant = restaurant
        self.value = value

    @staticmethod
    def from_entity(feedback: Feedback) -> "FeedbackDynamoDTO":
        """
        Parse data from Feedback to FeedbackDynamoDTO
        """
        return FeedbackDynamoDTO(
            order_id = feedback.order_id,    
            user_id = feedback.user_id,
            restaurant = feedback.restaurant,
            value = feedback.value
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from FeedbackDynamoDTO to dict
        """
        data = {
            "entity": "feedback",
            "order_id": self.order_id,
            "user_id": self.user_id,
            "restaurant": self.restaurant.value,
            "value": Decimal(str(self.value))
        }

        data_without_none_values = {k: v for k, v in data.items() if v is not None}

        return data_without_none_values

    @staticmethod
    def from_dynamo(feedback_data: dict) -> "FeedbackDynamoDTO":
        """
        Parse data from DynamoDB to FeedbackDynamoDTO
        @param feedback_data: dict from DynamoDB
        """
        return FeedbackDynamoDTO(
            order_id=str(feedback_data["order_id"]),
            user_id=str(feedback_data["user_id"]),
            restaurant=RESTAURANT(feedback_data.get("restaurant")),
            value=int(feedback_data.get("value"))
        )

    def to_entity(self) -> Feedback:
        """
        Parse data from FeedbackDynamoDTO to Feedback
        """
        return Feedback(
            order_id=self.order_id,
            user_id=self.user_id,
            restaurant=self.restaurant,
            value=self.value
        )

    def __repr__(self):
        return f"FeedbackDynamoDto(order_id={self.order_id}, user_id={self.user_id}, restaurant={self.restaurant}, value={self.value})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__