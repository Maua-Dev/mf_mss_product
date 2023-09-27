from src.modules.get_all_orders_by_user.app.get_all_orders_by_user_controller import GetAllOrdersByUserController
from src.modules.get_all_orders_by_user.app.get_all_orders_by_user_usecase import GetAllOrdersByUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllOrdersByUserController:
    def test_get_all_orders_by_user_controller(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)
        controller = GetAllOrdersByUserController(usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[5].user_id,
                "name": repo_user.users_list[5].name,
                "email": repo_user.users_list[5].email,
                "custom:isMaua": True},
            'exclusive_start_key': repo_order.orders[4].order_id
        })

        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.data["message"] == "the orders were retrieved"

    def test_get_all_orders_by_user_controller_without_exclusive_start_key(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)
        controller = GetAllOrdersByUserController(usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[5].user_id,
                "name": repo_user.users_list[5].name,
                "email": repo_user.users_list[5].email,
                "custom:isMaua": True},
        })

        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.data["message"] == "the orders were retrieved"

    def test_get_all_orders_by_user_controller_requester_user_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)
        controller = GetAllOrdersByUserController(usecase)

        request = HttpRequest(body={
            'exclusive_start_key': repo_order.orders[4].order_id
        })

        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"

    def test_get_all_orders_by_user_controller_unregister_user(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)
        controller = GetAllOrdersByUserController(usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": "sem id",
                "name": repo_user.users_list[5].name,
                "email": repo_user.users_list[5].email,
                "custom:isMaua": True},
            'exclusive_start_key': repo_order.orders[4].order_id
        })

        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "That user is not registered"

    def test_get_all_orders_by_user_controller_order_not_found(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)
        controller = GetAllOrdersByUserController(usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[5].user_id,
                "name": repo_user.users_list[5].name,
                "email": repo_user.users_list[5].email,
                "custom:isMaua": True},
            'exclusive_start_key': "4b1e0f88-2c34-3t"
        })

        response = controller(request=request)
        
        assert response.status_code == 404
        assert response.body == "No items found for exclusive_start_key"

    def test_get_all_orders_by_user_controller_user_not_order_owner(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)
        controller = GetAllOrdersByUserController(usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[4].user_id,
                "name": repo_user.users_list[4].name,
                "email": repo_user.users_list[4].email,
                "custom:isMaua": True},
            'exclusive_start_key': repo_order.orders[4].order_id
        })

        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "The user_id does not match with the inserted order_id"