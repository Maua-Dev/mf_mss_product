from src.modules.create_user.app.create_user_controller import CreateUserController
from src.modules.create_user.app.create_user_usecase import CreateUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_CreateUserControler:
    def test_create_user_controller(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo=repo)
        controller = CreateUserController(usecase=usecase)

        request = HttpRequest(headers={"requester_user":{"sub":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "name":"Rodas Morales", "email":"rodas.morales@gmail.com", "custom:isMaua": True  }})

        response = controller(request)

        assert response.status_code == 201

    def test_create_user_controller_requester_user_none(self):
        repo = UserRepositoryMock()
        usecase = CreateUserUsecase(repo=repo)
        controller = CreateUserController(usecase=usecase)

        request = HttpRequest(headers={})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"