from datetime import time

from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.modules.create_schedule.app.create_schedule_usecase import CreateScheduleUsecase
from src.modules.create_schedule.app.create_schedule_controller import CreateScheduleController
from src.shared.helpers.external_interfaces.http_models import HttpRequest

class Test_CreateScheduleController:
    def test_create_schedule_controller(self):
        repo_schedule = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateScheduleUsecase(repo_schedule, repo_user)
        controller = CreateScheduleController(usecase)

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": repo_user.users_list[3].user_id,
                    "name": repo_user.users_list[0].name,
                    "email": repo_user.users_list[0].email,
                    "custom:isMaua": True
                },
                "initial_time": "10:00:00",
                "end_time": "12:00:00",
            },
        )

        response = controller(request)
        
        assert response.status_code == 201

    def test_create_schedule_controller_schedule_is_missing(self):
        repo_schedule = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateScheduleUsecase(repo_schedule=repo_schedule, repo_user=repo_user)
        controller = CreateScheduleController(usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[3].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "schedule_id": None,
            "initial_time": "10:00:00",
            "end_time": "12:00:00",
            "restaurant": "SOUZA_DE_ABREU",
            "accepted_reservation": True
        })

        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == 'Field schedule_id is missing'

    def test_create_schedule_controller_initial_time_is_missing(self):
        repo_schedule = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateScheduleUsecase(repo_schedule=repo_schedule, repo_user=repo_user)
        controller = CreateScheduleController(usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[3].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "schedule_id": "e51b48a0-e33c-4ace-98a0-d9af96157dfc",
            "end_time": "12:00:00",
            "restaurant": "SOUZA_DE_ABREU",
            "accepted_reservation": True
        })

        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == 'Field initial_time is missing'
    
    def test_create_schedule_controller_end_time_is_missing(self):
        repo_schedule = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateScheduleUsecase(repo_schedule=repo_schedule, repo_user=repo_user)
        controller = CreateScheduleController(usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[3].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "initial_time": "10:00:00",
            "end_time": "12:00:00",
        })

        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == 'Field end_time is missing'

    def test_create_schedule_controller_restaurant_is_missing(self):
        repo_schedule = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateScheduleUsecase(repo_schedule=repo_schedule, repo_user=repo_user)
        controller = CreateScheduleController(usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[3].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "initial_time": "10:00:00",
            "end_time": "12:00:00",
        })

        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == 'Field restaurant is missing'

    def test_create_schedule_controller_accepted_reservation_is_missing(self):
        repo_schedule = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateScheduleUsecase(repo_schedule=repo_schedule, repo_user=repo_user)
        controller = CreateScheduleController(usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[3].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "initial_time": "10:00:00",
            "end_time": "12:00:00",
        })

        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == 'Field accepted_reservation is missing'

    def test_create_schedule_controller_invalid_schedule_id(self):
        repo_schedule = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateScheduleUsecase(repo_schedule=repo_schedule, repo_user=repo_user)
        controller = CreateScheduleController(usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[3].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "initial_time": "10:00:00",
            "end_time": "12:00:00",
        })

        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == 'Field schedule_id is not valid'

    def test_create_schedule_controller_invalid_restaurant_invalid(self):
        repo_schedule = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateScheduleUsecase(repo_schedule=repo_schedule, repo_user=repo_user)
        controller = CreateScheduleController(usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[3].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "initial_time": "10:00:00",
            "end_time": "12:00:00",
        })

        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == 'Field restaurant is not valid'

    def test_create_schedule_controller_invalid_accepted_reservation(self):
        repo_schedule = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateScheduleUsecase(repo_schedule=repo_schedule, repo_user=repo_user)
        controller = CreateScheduleController(usecase)

        request = HttpRequest(body={
            'requester_user': {
                "sub": repo_user.users_list[3].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "initial_time": "10:00:00",
            "end_time": "12:00:00",
        })

        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == 'Field accepted_reservation is not valid'
    