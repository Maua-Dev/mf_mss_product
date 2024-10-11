from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.modules.get_average_feedback_by_restaurant.app.get_average_feedback_by_restaurant_usecase import GetAverageFeedbackByRestaurantUsecase
from src.modules.get_average_feedback_by_restaurant.app.get_average_feedback_by_restaurant_controller import GetAverageFeedbackByRestaurantController


class Test_GetAverageFeedbackByRestaurantController:
    def test_get_average_feedback_by_restaurant_controller(self):
        repo_user = UserRepositoryMock()
        repo_order = OrderRepositoryMock()
        usecase = GetAverageFeedbackByRestaurantUsecase(repo_user, repo_order)
        controller = GetAverageFeedbackByRestaurantController(usecase=usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[2].user_id,
                "name": repo_user.users_list[2].name,
                "email": repo_user.users_list[2].email,
                "custom:isMaua": True}
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.data["average_feedback"] == 3.0
        assert response.data["message"] == "the average feedback was retrieved"

    def test_get_average_feedback_by_restaurant_controller_requester_user_none(self):
        repo_user = UserRepositoryMock()
        repo_order = OrderRepositoryMock()
        usecase = GetAverageFeedbackByRestaurantUsecase(repo_user, repo_order)
        controller = GetAverageFeedbackByRestaurantController(usecase=usecase)

        request = HttpRequest(body={})

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"

    def test_get_average_feedback_by_restaurant_controller_requester_user_not_admin_owner_seller(self):
        repo_user = UserRepositoryMock()
        repo_order = OrderRepositoryMock()
        usecase = GetAverageFeedbackByRestaurantUsecase(repo_user, repo_order)
        controller = GetAverageFeedbackByRestaurantController(usecase=usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[-1].user_id,
                "name": repo_user.users_list[-1].name,
                "email": repo_user.users_list[-1].email,
                "custom:isMaua": True}
        })

        response = controller(request=request)

        assert response.status_code == 403
        assert response.body == "That type of user has no permission for that action"

    def test_get_average_feedback_by_restaurant_controller_user_not_registered(self):
        repo_user = UserRepositoryMock()
        repo_order = OrderRepositoryMock()
        usecase = GetAverageFeedbackByRestaurantUsecase(repo_user, repo_order)
        controller = GetAverageFeedbackByRestaurantController(usecase=usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": "123",
                "name": "name",
                "email": "email",
                "custom:isMaua": True}
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "That user is not registered"