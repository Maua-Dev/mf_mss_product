from src.modules.get_all_schedules_by_restaurant.app.get_all_schedules_by_restaurant_usecase import GetAllSchedulesByRestaurantUseCase
from src.modules.get_all_schedules_by_restaurant.app.get_all_schedules_by_restaurant_viewmodel import GetAllSchedulesByRestaurantViewmodel
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from datetime import time

class Test_GetAllSchedulesByRestaurantViewmodel:

    def test_get_all_schedules_viewmodel(self):
        userrepo = UserRepositoryMock()
        orderrepo = OrderRepositoryMock()
        usecase = GetAllSchedulesByRestaurantUseCase(userrepo=userrepo, orderrepo=orderrepo)
        schedules = usecase("93bc6ada-c0d1-ab53-66ab-e17414c48af1", restaurant=RESTAURANT.SOUZA_DE_ABREU)

        viewmodel = GetAllSchedulesByRestaurantViewmodel(schedules).to_dict()
        print(viewmodel)
        expected = {
    'schedules': [
        {
            'schedule_id': "afc910c4-a135-4ce3-9ca8-f7ec5e60f4fe",
            'initial_time': time(11, 0, 0),
            'end_time': time(12, 30, 0), 
            'restaurant': "SOUZA_DE_ABREU",
            'accepted_reservation': True
        },
        {
            'schedule_id': "b3f9ecc1-1ac7-40eb-a8dd-54fe7b6f874d",
            'initial_time': time(9, 30, 0),  
            'end_time': time(11, 0, 0),
            'restaurant': "SOUZA_DE_ABREU",
            'accepted_reservation': True
        },
        {
            'schedule_id': "82b76801-9bb3-4eda-a686-8d189c59ba28",
            'initial_time': time(8, 0, 0),   
            'end_time': time(9, 30, 0),
            'restaurant': "SOUZA_DE_ABREU",
            'accepted_reservation': True
        }
    ],
    'message': "the schedules were retrieved"
}

        
        assert sorted(viewmodel['schedules'], key=lambda x: x['schedule_id']) == sorted(expected['schedules'], key=lambda x: x['schedule_id'])
