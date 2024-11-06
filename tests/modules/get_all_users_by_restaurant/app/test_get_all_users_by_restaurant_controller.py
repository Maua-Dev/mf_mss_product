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
            "user_id": user_repo.users_list[2].user_id,
        })

        response = controller(request)
        
        assert response.status_code == 200
    
    def test_get_all_users_by_restaurant_controller_requester_user_none(self):
        user_repo = UserRepositoryMock()
        order_repo = OrderRepositoryMock()
        usecase = GetAllUsersByRestaurantUseCase(user_repo, order_repo)
        controller = GetAllUsersByRestaurantController(usecase)

        request = HttpRequest(body={})

        response = controller(request)
        
        assert response.status_code == 400