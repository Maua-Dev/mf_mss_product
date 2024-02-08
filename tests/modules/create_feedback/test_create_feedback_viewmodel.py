from src.modules.create_feedback.create_feedback_viewmodel import CreateFeedbackViewmodel
from src.shared.domain.entities.feedback import Feedback
from src.shared.domain.enums.restaurant_enum import RESTAURANT

class Test_CreateFeedbackViewmodel:

    def test_create_feedback_viewmodel(self):

        feedback = Feedback(
            order_id="d78a47cb-80db-4661-b810-8e7c9419d61b",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48af9",
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            value=4
        )

        feedback_viewmodel = CreateFeedbackViewmodel(feedback=feedback).to_dict()

        expected = {
            "feedback": {
            "order_id" :"d78a47cb-80db-4661-b810-8e7c9419d61b",
            "user_id":"93bc6ada-c0d1-7054-66ab-e17414c48af9",
            "restaurant":"SOUZA_DE_ABREU",
            "value":4,
            },
            "message":"the feedback was created"
            }
        
        
        assert expected == feedback_viewmodel