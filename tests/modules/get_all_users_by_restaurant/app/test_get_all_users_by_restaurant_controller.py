from src.modules.get_all_users_by_restaurant.app.get_all_users_by_restaurant_controller import GetAllUsersByRestaurantController
from src.modules.get_all_users_by_restaurant.app.get_all_users_by_restaurant_usecase import GetAllUsersByRestaurantUseCase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllUsersByRestaurantController:
    def test_get_all_users_by_restaurant_controller(self):
        user_repo = UserRepositoryMock()
        order_repo = OrderRepositoryMock()
        usecase = GetAllUsersByRestaurantUseCase(user_repo, order_repo)
        controller = GetAllUsersByRestaurantController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": user_repo.users_list[2].user_id,
                "name": user_repo.users_list[2].name,
                "email": user_repo.users_list[2].email,
                "custom:isMaua": True
            },
        'restaurant': "SOUZA_DE_ABREU"
        })

        response = controller(request)
        
        assert response.status_code == 200
    
    def test_get_all_users_by_restaurant_controller_role_user_not_allowed(self):
        repo_user = UserRepositoryMock()
        order_repo = OrderRepositoryMock()
        usecase = GetAllUsersByRestaurantUseCase(repo_user, order_repo)
        controller = GetAllUsersByRestaurantController(usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": repo_user.users_list[4].user_id,
                    "name": repo_user.users_list[4].name,
                    "email": repo_user.users_list[4].email,
                    "custom:isMaua": True
                },
                "user_id": repo_user.users_list[4].user_id,
                "restaurant": "CANTINA_DO_MOLEZA"
            },
        )

        response = controller(request)
        
        assert response.status_code == 403

    def test_get_all_users_by_restaurant_controller_restaurant_is_missing(self):
        repo_user = UserRepositoryMock()
        order_repo = OrderRepositoryMock()
        usecase = GetAllUsersByRestaurantUseCase(repo_user, order_repo)
        controller = GetAllUsersByRestaurantController(usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": repo_user.users_list[2].user_id,
                    "name": repo_user.users_list[2].name,
                    "email": repo_user.users_list[2].email,
                    "custom:isMaua": True
                },
            },
        )

        response = controller(request)
        
        assert response.status_code == 400

    def test_get_all_users_by_restaurant_controller_restaurant_is_not_valid(self):
        repo_user = UserRepositoryMock()
        order_repo = OrderRepositoryMock()
        usecase = GetAllUsersByRestaurantUseCase(repo_user, order_repo)
        controller = GetAllUsersByRestaurantController(usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": repo_user.users_list[2].user_id,
                    "name": repo_user.users_list[2].name,
                    "email": repo_user.users_list[2].email,
                    "custom:isMaua": True
                },
                "restaurant": "INVALID_RESTAURANT"
            },
        )

        response = controller(request)
        
        assert response.status_code == 404