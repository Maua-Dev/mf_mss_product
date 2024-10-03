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
        'restaurant': "SOUZA_DE_ABREU"
        }, headers={'user_id': '93bc6ada-c0d1-ab53-66ab-e17414c48af1'})
        
        response = controller(request=request)
        expected_dict = {
            'schedules': [
                {'schedule': {'schedule_id': "afc910c4-a135-4ce3-9ca8-f7ec5e60f4fe", 'initial_time': "11:00:00", 'end_time': "12:30:00", 'restaurant': "SOUZA_DE_ABREU", 'accepted_reservation': "True"}},
                {'schedule': {'schedule_id': "b3f9ecc1-1ac7-40eb-a8dd-54fe7b6f874d", 'initial_time': "09:30:00", 'end_time': "11:00:00", 'restaurant': "SOUZA_DE_ABREU", 'accepted_reservation': "True"}},
                {'schedule': {'schedule_id': "82b76801-9bb3-4eda-a686-8d189c59ba28", 'initial_time': "08:00:00", 'end_time': "09:30:00", 'restaurant': "SOUZA_DE_ABREU", 'accepted_reservation': "True"}}
            ]
        }

        assert response.status_code == 200
        assert len(response.body['schedules']) == 3
        response = sorted(response.body['schedules'], key=lambda x: x['schedule']['schedule_id'])
        expected_dict = sorted(expected_dict['schedules'], key=lambda x: x['schedule']['schedule_id'])
        assert response == expected_dict

    
    def test_get_all_schedules_by_restaurant_controller__requester_user_none(self):
        userrepo = UserRepositoryMock()
        orderrepo = OrderRepositoryMock()
        usecase = GetAllSchedulesByRestaurantUseCase(userrepo=userrepo, orderrepo=orderrepo)
        controller = GetAllSchedulesByRestaurantController(usecase=usecase)
        request = HttpRequest(body={})
        response = controller(request=request)
        
        assert response.status_code == 400