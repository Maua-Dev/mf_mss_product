from src.modules.get_user.app.get_user_controller import GetUserController
from src.modules.get_user.app.get_user_usecase import GetUserUseCase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetUserController:
    repo_mock = UserRepositoryMock()
    usecase = GetUserUseCase(repo_mock)
    controller = GetUserController(usecase)
    first_user = repo_mock.users_list[0]

    def test_get_user_controller(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": self.first_user.user_id,
                    "name": self.first_user.name,
                    "email": self.first_user.email,
                    "custom:isMaua": True
                }
            }
        )

        expected_dict = {
            "user": {
                "name": self.first_user.name,
                "email": self.first_user.email,
                "role": self.first_user.role.value,
                "user_id": self.first_user.user_id,
                "restaurant": self.first_user.restaurant
            },
            "message": "the user was retrieved"
        }

        response = self.controller(request)

        assert response.status_code == 200
        assert response.body == expected_dict

    def test_get_controller_with_invalid_id(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": "Um id no formato inválido",
                    "name": self.first_user.name,
                    "email": self.first_user.email,
                    "custom:isMaua": True
                }
            }
        )

        response = self.controller(request)

        assert response.status_code == 400

    def test_get_controller_without_id(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": None,
                    "name": self.first_user.name,
                    "email": self.first_user.email,
                    "custom:isMaua": True
                }
            }
        )

        response = self.controller(request)

        assert response.status_code == 400

    def test_get_controller_with_nonexistentid(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "name": self.first_user.name,
                    "email": self.first_user.email,
                    "custom:isMaua": True
                }
            }
        )

        response = self.controller(request)

        assert response.status_code == 404
