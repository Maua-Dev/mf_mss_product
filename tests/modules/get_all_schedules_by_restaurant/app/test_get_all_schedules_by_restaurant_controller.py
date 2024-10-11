from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.modules.get_all_schedules_by_restaurant.app.get_all_schedules_by_restaurant_usecase import GetAllSchedulesByRestaurantUseCase
from src.modules.get_all_schedules_by_restaurant.app.get_all_schedules_by_restaurant_controller import GetAllSchedulesByRestaurantController
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.domain.enums.restaurant_enum import RESTAURANT

class Test_GetAllSchedulesByRestaurantController:

    def test_get_all_schedules_by_restaurant_controller(self):
        userrepo = UserRepositoryMock()
        orderrepo = OrderRepositoryMock()
        usecase = GetAllSchedulesByRestaurantUseCase(userrepo=userrepo, orderrepo=orderrepo)
        controller = GetAllSchedulesByRestaurantController(usecase=usecase)
        
        request = HttpRequest(body={
            "requester_user": {
                "sub": userrepo.users_list[0].user_id,
                "name": userrepo.users_list[0].name,
                "email": userrepo.users_list[0].email,
                "custom:isMaua": True
            },
        'restaurant': "SOUZA_DE_ABREU"
        })
        
        response = controller(request)

        assert response.status_code == 200
        
    def test_get_all_schedules_by_restaurant_controller__requester_user_none(self):
        userrepo = UserRepositoryMock()
        orderrepo = OrderRepositoryMock()
        usecase = GetAllSchedulesByRestaurantUseCase(userrepo=userrepo, orderrepo=orderrepo)
        controller = GetAllSchedulesByRestaurantController(usecase=usecase)
        request = HttpRequest(body={})
        response = controller(request=request)
        
        assert response.status_code == 400