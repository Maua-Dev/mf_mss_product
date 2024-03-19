import pytest

from src.shared.domain.entities.feedback import Feedback
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterExcededMaximumValue, EntityParameterHaveMinValue


class Test_Feedback:
    def test_feedbacl(self):
        feedback = Feedback(
            order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            value=1
        )

        assert type(feedback) == Feedback
        assert feedback.order_id == "b3f6c5aa-80ad-4f95-ae16-455b4f87fb53"
        assert feedback.user_id == "f15d32eb-403f-46a4-8efc-804d9f8bed0f"
        assert feedback.restaurant == RESTAURANT.SOUZA_DE_ABREU
        assert feedback.value == 1

    def test_invalid_id(self):
        with pytest.raises(EntityError):
            feedback = Feedback(
                order_id=666,
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                value=1
            )

    def test_invalid_restaurant(self):
        with pytest.raises(EntityError):
            feedback = Feedback(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                restaurant="batata",
                value=1
            )

    def test_invalid_value(self):
        with pytest.raises(EntityError):
            feedback = Feedback(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                restaurant="batata",
                value=RESTAURANT.CANTINA_DO_MOLEZA
            )

    def test_invalid_value_min(self):
        with pytest.raises(EntityParameterHaveMinValue):
            feedback = Feedback(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                value=0
            )

    def test_invalid_value_max(self):
        with pytest.raises(EntityParameterExcededMaximumValue):
            feedback = Feedback(
                order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                user_id="f15d32eb-403f-46a4-8efc-804d9f8bed0f",
                restaurant=RESTAURANT.SOUZA_DE_ABREU,
                value=6
            )