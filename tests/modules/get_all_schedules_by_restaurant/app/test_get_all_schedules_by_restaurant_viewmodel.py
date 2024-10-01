from src.modules.get_all_schedules_by_restaurant.app.get_all_schedules_by_restaurant_usecase import GetAllSchedulesByRestaurantUseCase
from src.modules.get_all_schedules_by_restaurant.app.get_all_schedules_by_restaurant_viewmodel import GetAllSchedulesViewmodel
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.domain.enums.restaurant_enum import RESTAURANT

class Test_GetAllSchedulesViewModel:

    def test_get_all_schedules_viewmodel(self):
        userrepo = UserRepositoryMock()
        orderrepo = OrderRepositoryMock()
        usecase = GetAllSchedulesByRestaurantUseCase(userrepo=userrepo, orderrepo=orderrepo)
        schedules = usecase("93bc6ada-c0d1-ab53-66ab-e17414c48af1", restaurant=RESTAURANT.SOUZA_DE_ABREU)

        viewmodel = GetAllSchedulesViewmodel(schedules).to_dict()
        print(viewmodel)
        expected = {
    'schedules': [
        {
            'schedule': {
                'schedule_id': "afc910c4-a135-4ce3-9ca8-f7ec5e60f4fe",
                'initial_time': "11:00:00",
                'end_time': "12:30:00",
                'restaurant': "SOUZA_DE_ABREU",
                'accepted_reservation': "True"
            }
        },
        {
            'schedule': {
                'schedule_id': "b3f9ecc1-1ac7-40eb-a8dd-54fe7b6f874d",
                'initial_time': "09:30:00",
                'end_time': "11:00:00",
                'restaurant': "SOUZA_DE_ABREU",
                'accepted_reservation': "True"
            }
        },
        {
            'schedule': {
                'schedule_id': "82b76801-9bb3-4eda-a686-8d189c59ba28",
                'initial_time': "08:00:00",
                'end_time': "09:30:00",
                'restaurant': "SOUZA_DE_ABREU",
                'accepted_reservation': "True"
            }
        }
    ],
}
        
        assert sorted(viewmodel['schedules'], key=lambda x: x['schedule']['schedule_id']) == sorted(expected['schedules'], key=lambda x: x['schedule']['schedule_id'])