from src.modules.create_connection.app.create_connection_controller import CreateConnectionController
from src.modules.create_connection.app.create_connection_usecase import CreateConnectionUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_CreateConnectionController:
    def test_create_connection_controller(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateConnectionUsecase(repo_order, repo_user)
        controller = CreateConnectionController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "connection_id": "4b1e0f88-2ch6-3t2",
            "api_id": "63c77df8-d1",
            "restaurant": "HORA_H"
        })

        response = controller(request)

        assert response.status_code == 201
        assert response.body["message"] == "the connection was created"
        assert response.body["connection"]["connection_id"] == "4b1e0f88-2ch6-3t2"
        assert response.body["connection"]["api_id"] == "63c77df8-d1"
        assert response.body["connection"]["user_id"] == "93bc6ada-c0d1-7054-66ab-e17414c48ae3"
        assert response.body["connection"]["restaurant"] == "HORA_H"

    def test_create_connection_controller_requester_user_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateConnectionUsecase(repo_order, repo_user)
        controller = CreateConnectionController(usecase)

        request = HttpRequest(body={
            "connection_id": "4b1e0f88-2ch6-3t2",
            "api_id": "63c77df8-d1",
            "restaurant": "HORA_H"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"

    def test_create_connection_controller_connection_id_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateConnectionUsecase(repo_order, repo_user)
        controller = CreateConnectionController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "api_id": "63c77df8-d1",
            "restaurant": "HORA_H"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field connection_id is missing"

    def test_create_connection_controller_api_id_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateConnectionUsecase(repo_order, repo_user)
        controller = CreateConnectionController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "connection_id": "4b1e0f88-2ch6-3t2",
            "restaurant": "HORA_H"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field api_id is missing"

    def test_create_connection_controller_restaurant_none(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateConnectionUsecase(repo_order, repo_user)
        controller = CreateConnectionController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "connection_id": "4b1e0f88-2ch6-3t2",
            "api_id": "63c77df8-d1",
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field restaurant is missing"

    def test_create_connection_controller(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateConnectionUsecase(repo_order, repo_user)
        controller = CreateConnectionController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_user.users_list[0].user_id,
                "name": repo_user.users_list[0].name,
                "email": repo_user.users_list[0].email,
                "custom:isMaua": True
            },
            "connection_id": "4b1e0f88-2ch6-3t2",
            "api_id": "63c77df8-d1",
            "restaurant": "Tech Food"
        })

        response = controller(request)

        assert response.status_code == 404
        assert response.body == "Field 'Tech Food' is not a restaurant"

    