from decimal import Decimal

from src.shared.domain.entities.feedback import Feedback
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.dto.feedback_dynamo_dto import FeedbackDynamoDTO
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock


class Test_FeedbackDynamoDto:
    def test_from_entity(self):
        repo = OrderRepositoryMock()

        feedback_dto = FeedbackDynamoDTO.from_entity(feedback=repo.feedbacks[0])

        expected_feedback_dto = FeedbackDynamoDTO(
            order_id=repo.feedbacks[0].order_id,
            user_id=repo.feedbacks[0].user_id,
            restaurant=repo.feedbacks[0].restaurant,
            value=repo.feedbacks[0].value
        )

        assert feedback_dto == expected_feedback_dto
        assert type(feedback_dto.value) == int
        
    def test_to_dynamo(self):
        repo = OrderRepositoryMock()

        feedback_dto = FeedbackDynamoDTO(
            order_id=repo.feedbacks[0].order_id,
            user_id=repo.feedbacks[0].user_id,
            restaurant=repo.feedbacks[0].restaurant,
            value=repo.feedbacks[0].value
        )

        feedback_dynamo = feedback_dto.to_dynamo()

        expected_dict = {
            "entity": "feedback",
            "order_id": repo.feedbacks[0].order_id,
            "user_id":repo.feedbacks[0].user_id,
            "restaurant": repo.feedbacks[0].restaurant.value,
            "value": Decimal(repo.feedbacks[0].value),
        }

        assert feedback_dto.to_dynamo() == expected_dict
        assert type(expected_dict['value']) == Decimal

    def test_from_dynamo(self):
        dynamo_dict = {'Item': {'order_id': '1eeef881-1b1f-4f38-a662-8ff7156e6c27',
                                'user_id':'93bc6ada-c0d1-7054-66ab-e17414c48ae3',
                                'restaurant': 'SOUZA_DE_ABREU',
                                'value': Decimal('5'),
                                'SK': '#8a705b91-c9e9-4353-a755-07f13afafed3',
                                'PK': 'feedback#8a705b91-c9e9-4353-a755-07f13afafed3',
                                'entity': 'feedback'},
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}

        feedback_dto = FeedbackDynamoDTO.from_dynamo(feedback_data=dynamo_dict["Item"])

        expected_feedback_dto = FeedbackDynamoDTO(
            order_id='1eeef881-1b1f-4f38-a662-8ff7156e6c27',
            user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3',
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            value=5
        )

        assert feedback_dto == expected_feedback_dto
        assert type(dynamo_dict['Item']['value']) == Decimal

    def test_to_entity(self):
        repo = OrderRepositoryMock()

        feedback_dto = FeedbackDynamoDTO(
            order_id=repo.feedbacks[0].order_id,
            user_id=repo.feedbacks[0].user_id,
            restaurant=repo.feedbacks[0].restaurant,
            value=repo.feedbacks[0].value
        )

        feedback = feedback_dto.to_entity()

        assert feedback.order_id == repo.feedbacks[0].order_id
        assert feedback.user_id == repo.feedbacks[0].user_id
        assert feedback.restaurant == repo.feedbacks[0].restaurant
        assert feedback.value == repo.feedbacks[0].value
        assert type(feedback.value) == int   

    def test_from_dynamo_to_entity(self):
        dynamo_dict = {'Item': {'order_id': '1eeef881-1b1f-4f38-a662-8ff7156e6c27',
                                'user_id':'93bc6ada-c0d1-7054-66ab-e17414c48ae3',
                                'restaurant': 'SOUZA_DE_ABREU',
                                'value': Decimal('5'),
                                'SK': '#8a705b91-c9e9-4353-a755-07f13afafed3',
                                'PK': 'feedback#8a705b91-c9e9-4353-a755-07f13afafed3',
                                'entity': 'feedback'},
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}

        feedback_dto = FeedbackDynamoDTO.from_dynamo(feedback_data=dynamo_dict["Item"])

        feedback = feedback_dto.to_entity()

        expected_feedback = Feedback(
            order_id='1eeef881-1b1f-4f38-a662-8ff7156e6c27',
            user_id='93bc6ada-c0d1-7054-66ab-e17414c48ae3',
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            value=5
        )

        assert feedback.order_id == expected_feedback.order_id
        assert feedback.user_id == expected_feedback.user_id
        assert feedback.restaurant == expected_feedback.restaurant
        assert feedback.value == expected_feedback.value

    def test_from_entity_to_dynamo(self):
        repo = OrderRepositoryMock()

        feedback_dto = FeedbackDynamoDTO.from_entity(feedback=repo.feedbacks[0])

        feedback_dynamo = feedback_dto.to_dynamo()

        expected_dict = {
            "entity": "feedback",
            "order_id": repo.feedbacks[0].order_id,
            "user_id": repo.feedbacks[0].user_id,
            "restaurant": repo.feedbacks[0].restaurant.value,
            "value": repo.feedbacks[0].value,
        }

        assert feedback_dynamo == expected_dict