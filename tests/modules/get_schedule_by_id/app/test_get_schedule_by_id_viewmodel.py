from src.modules.get_schedule_by_id.app.get_schedule_by_id_viewmodel import \
    GetScheduleByIdViewmodel
from src.shared.domain.enums.status_enum import STATUS
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock


class Test_GetScheduleByIdViewmodel:
    def test_viewmodel(self):
        schedules_repo = OrderRepositoryMock()
        schedule = schedules_repo.schedules[-1]

        viewmodel = GetScheduleByIdViewmodel(schedule).to_dict()
        
        expected = {'schedule':{
            "schedule_id": schedule.schedule_id,
            "initial_time": schedule.initial_time.strftime("%H:%M"),
            "end_time": schedule.end_time.strftime("%H:%M"),
            "restaurant": schedule.restaurant.value,
            "accepted_reservation":schedule.accepted_reservation},
            'message': 'the schedule object was retrieved'
        }

        assert viewmodel == expected

