from src.modules.manage_connection.app.manage_connection_controller import ManageConnectionController
from src.modules.manage_connection.app.manage_connection_usecase import ManageConnectionUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ManageConnectionController:
    def test_create_connection_controller(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManageConnectionUsecase(repo_order, repo_user)
        controller = ManageConnectionController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[7].user_id,
                "name": repo_user.users_list[7].name,
                "email": repo_user.users_list[7].email,
                "custom:isMaua": True
            },
            "route_key": '$connect',
            "connection_id": "4b1e0f88-2ch6-3t",
            "api_id": "63c77df8-d"
        })

        response = controller(request)

        assert response.status_code == 200
        assert response.body["message"] == "the connection status"
        assert response.body["connection"]["connection_id"] == "4b1e0f88-2ch6-3t"
        assert response.body["connection"]["api_id"] == "63c77df8-d"
        assert response.body["connection"]["user_id"] == "93bc6ada-c0d1-7054-66ab-egu923c48af1"
        assert response.body["connection"]["restaurant"] == "HORA_H"

    def test_abort_connection_controller(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManageConnectionUsecase(repo_order, repo_user)
        controller = ManageConnectionController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[2].user_id,
                "name": repo_user.users_list[2].name,
                "email": repo_user.users_list[2].email,
                "custom:isMaua": True
            },
            "route_key": '$connect',
            "connection_id": "4b1e0f88-2c34-3t",
            "api_id": "63c77df8-d"
        })

        response = controller(request)

        assert response.status_code == 200
        assert response.body["message"] == "the connection status"
        assert response.body["connection"]["connection_id"] == "4b1e0f88-2c34-3t"
        assert response.body["connection"]["api_id"] == "63c77df8-d"
        assert response.body["connection"]["user_id"] == "93bc6ada-c0d1-7054-66ab-e17414c48abb"
        assert response.body["connection"]["restaurant"] == "CANTINA_DO_MOLEZA"

    def test_create_connection_controller_requester_user_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManageConnectionUsecase(repo_order, repo_user)
        controller = ManageConnectionController(usecase)

        request = HttpRequest(body={
            "route_key": '$connect',
            "connection_id": "4b1e0f88-2ch6-3t",
            "api_id": "63c77df8-d"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"

    def test_manage_connection_controller_connection_id_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManageConnectionUsecase(repo_order, repo_user)
        controller = ManageConnectionController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "route_key": '$disconnect',
            "api_id": "63c77df8-d"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field connection_id is missing"

    def test_create_connection_controller_api_id_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManageConnectionUsecase(repo_order, repo_user)
        controller = ManageConnectionController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "route_key": '$connect',
            "connection_id": "4b1e0f88-2ch6-3t"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field api_id is missing"



    