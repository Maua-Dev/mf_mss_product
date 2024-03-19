from src.modules.get_average_feedback_by_restaurant.app.get_average_feedback_by_restaurant_usecase import GetAverageFeedbackByRestaurantUsecase
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock


class Test_GetAverageFeedbackByRestaurantUsecase:
    def test_get_average_feedback_by_restaurant_usecase(self):
        user_repo = UserRepositoryMock()
        user = user_repo.users_list[-2]
        usecase = GetAverageFeedbackByRestaurantUsecase(user_repo=UserRepositoryMock(), order_repo=OrderRepositoryMock())
        response = usecase(user_id=user.user_id)
        assert response["average_feedback"] == 3.0

    def test_get_average_feedback_by_restaurant_usecase_unregistered_user(self):
        user_repo = UserRepositoryMock()
        usecase = GetAverageFeedbackByRestaurantUsecase(user_repo=UserRepositoryMock(), order_repo=OrderRepositoryMock())
        try:
            usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48a00")
        except Exception as e:
            assert str(e) == "That user is not registered"

    def test_get_average_feedback_by_restaurant_usecase_user_not_allowed(self):
        user_repo = UserRepositoryMock()
        user = user_repo.users_list[-1]
        usecase = GetAverageFeedbackByRestaurantUsecase(user_repo=UserRepositoryMock(), order_repo=OrderRepositoryMock())
        try:
            usecase(user_id=user.user_id)
        except Exception as e:
            assert str(e) == "That type of user has no permission for that action"

    def test_get_average_feedback_by_restaurant_usecase_empty_feedback(self):
        user_repo = UserRepositoryMock()
        user = user_repo.users_list[1]
        usecase = GetAverageFeedbackByRestaurantUsecase(user_repo=UserRepositoryMock(), order_repo=OrderRepositoryMock())
        response = usecase(user_id=user.user_id)
        assert response["average_feedback"] == 0.0
