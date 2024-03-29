from src.modules.get_all_active_orders_by_restaurant.app.get_all_active_orders_by_restaurant_controller import GetAllActiveOrdersByRestaurantController
from src.modules.get_all_active_orders_by_restaurant.app.get_all_active_orders_by_restaurant_usecase import GetAllActiveOrdersByRestaurantUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllActiveOrdersByRestaurantController:
    def test_get_all_products_group_by_restaurant_controller(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllActiveOrdersByRestaurantUsecase(repo_order, repo_user)
        controller = GetAllActiveOrdersByRestaurantController(usecase=usecase)
        
        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[2].user_id,
            "name": repo_user.users_list[2].name,
            "email": repo_user.users_list[2].email,
            "custom:isMaua": True}
        },)

        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.data["message"] == "the active orders were retrieved"

    def test_get_all_products_group_by_restaurant_controller_unregistered_user(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllActiveOrdersByRestaurantUsecase(repo_order, repo_user)
        controller = GetAllActiveOrdersByRestaurantController(usecase=usecase)
        
        request = HttpRequest(body={'requester_user': {
            "sub": 'id',
            "name": repo_user.users_list[2].name,
            "email": repo_user.users_list[2].email,
            "custom:isMaua": True}
        },)

        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "That user is not registered"

    def test_get_all_products_group_by_restaurant_controller_user_not_allowed(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllActiveOrdersByRestaurantUsecase(repo_order, repo_user)
        controller = GetAllActiveOrdersByRestaurantController(usecase=usecase)
        
        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[4].user_id,
            "name": repo_user.users_list[2].name,
            "email": repo_user.users_list[2].email,
            "custom:isMaua": True}
        },)

        response = controller(request=request)
        
        assert response.status_code == 403
        assert response.body == "That type of user has no permission for that action"

    def test_get_all_products_group_by_restaurant_controller_unregisted_employee(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllActiveOrdersByRestaurantUsecase(repo_order, repo_user)
        controller = GetAllActiveOrdersByRestaurantController(usecase=usecase)
        
        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[2].name,
            "email": repo_user.users_list[2].email,
            "custom:isMaua": True}
        },)

        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "This employee is unregistered."