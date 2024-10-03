from src.modules.get_schedule_by_id.app.get_schedule_by_id_controller import \
    GetScheduleByIdController
from src.modules.get_schedule_by_id.app.get_schedule_by_id_usecase import \
    GetScheduleByIdUsecase
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetScheduleByIdController:
    def test_controller(self):
        repo_schedules = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetScheduleByIdUsecase(repo_schedule=repo_schedules, repo_user=repo_user)
        controller = GetScheduleByIdController(usecase)

        schedules = repo_schedules.schedules[-1]
        user = repo_user.users_list[-1]

        request = HttpRequest(body={
            "requester_user": {
                "sub": user.user_id,
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            },
            "schedule_id": schedules.schedule_id
        })

        response = controller(request)

        assert response.status_code == 200


    def test_user_not_registered(self):
        repo_schedules = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetScheduleByIdUsecase(repo_schedule=repo_schedules, repo_user=repo_user)
        controller = GetScheduleByIdController(usecase)

        schedules = repo_schedules.schedules[-1]
        user = repo_user.users_list[-1]

        request = HttpRequest(body={
            "requester_user": {
                "sub": "um id que não existe",
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            },
            "schedule_id": schedules.schedule_id
        })

        response = controller(request)

        assert response.status_code == 404

    def test_missing_requester_user(self):
        repo_schedules = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetScheduleByIdUsecase(repo_schedule=repo_schedules, repo_user=repo_user)
        controller = GetScheduleByIdController(usecase)

        schedules = repo_schedules.schedules[-1]
        user = repo_user.users_list[-1]

        request = HttpRequest(body={
            "schedule_id": schedules.schedule_id
        })

        response = controller(request)

        assert response.status_code == 400

    def test_schedule_id_doesnt_exist(self):
        repo_schedules = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetScheduleByIdUsecase(repo_schedule=repo_schedules, repo_user=repo_user)
        controller = GetScheduleByIdController(usecase)

        schedules = repo_schedules.schedules[-1]
        user = repo_user.users_list[-1]

        request = HttpRequest(body={
            "requester_user": {
                "sub": user.user_id,
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            },
            "schedule_id": "Um id que não existe"
        })

        response = controller(request)

        assert response.status_code == 404
