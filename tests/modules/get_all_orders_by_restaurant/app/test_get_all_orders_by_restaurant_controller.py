from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.modules.get_all_orders_by_restaurant.app.get_all_orders_by_restaurant_usecase import GetAllOrdersByRestaurantUsecase
from src.modules.get_all_orders_by_restaurant.app.get_all_orders_by_restaurant_controller import GetAllOrdersByRestaurantController


class Test_GetAllOrdersByRestaurantController:
    def test_get_all_orders_by_restaurant_controller_without_exclusive_start_key(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByRestaurantUsecase(repo_order, repo_user)
        controller = GetAllOrdersByRestaurantController(usecase=usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[2].user_id,
                "name": repo_user.users_list[2].name,
                "email": repo_user.users_list[2].email,
                "custom:isMaua": True
            }
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.data["message"] == "the orders were retrieved"

    def test_get_all_orders_by_restaurant_controller_with_exclusive_start_key(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByRestaurantUsecase(repo_order, repo_user)
        controller = GetAllOrdersByRestaurantController(usecase=usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[2].user_id,
                "name": repo_user.users_list[2].name,
                "email": repo_user.users_list[2].email,
                "custom:isMaua": True},
            'exclusive_start_key': repo_order.orders[0].order_id
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.data["message"] == "the orders were retrieved"

    def test_get_all_orders_by_restaurant_controller_unregistered_user(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByRestaurantUsecase(repo_order, repo_user)
        controller = GetAllOrdersByRestaurantController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": 'id',
            "name": repo_user.users_list[2].name,
            "email": repo_user.users_list[2].email,
            "custom:isMaua": True}
        },)

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "That user is not registered"

    def test_get_all_orders_by_restaurant_controller_user_not_allowed(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByRestaurantUsecase(repo_order, repo_user)
        controller = GetAllOrdersByRestaurantController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[4].user_id,
            "name": repo_user.users_list[2].name,
            "email": repo_user.users_list[2].email,
            "custom:isMaua": True}
        }, )

        response = controller(request=request)

        assert response.status_code == 403
        assert response.body == "That type of user has no permission for that action"

    def test_get_all_orders_by_restaurant_controller_unregisted_employee(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByRestaurantUsecase(repo_order, repo_user)
        controller = GetAllOrdersByRestaurantController(usecase=usecase)

        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[2].name,
            "email": repo_user.users_list[2].email,
            "custom:isMaua": True}
        }, )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "This employee is unregistered."

