from src.modules.delete_user.app.delete_user_controller import DeleteUserController
from src.modules.delete_user.app.delete_user_usecase import DeleteUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_DeleteUserController:

    def test_delete_user_controller(self):
        repo = UserRepositoryMock()
        usecase = DeleteUserUsecase(repo=repo)
        controller = DeleteUserController(usecase=usecase)
        user = repo.users_list[0]

        request = HttpRequest(
            headers={
                'requester_user': {
                    "sub": user.user_id,
                    "name": user.name,
                    "email": user.email,
                    "custom:isMaua": True
                }
            }
        )

        expected_dict = {
            "user": {
                "name": user.name,
                "email": user.email,
                "role": user.role.value,
                "user_id": user.user_id,
                "restaurant": user.restaurant,
                "photo": user.photo
            },
            "message": "the user was deleted"
        }

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body == expected_dict

    def test_delete_controller_invalid_id(self):
        repo = UserRepositoryMock()
        usecase = DeleteUserUsecase(repo=repo)
        controller = DeleteUserController(usecase=usecase)
        user = repo.users_list[0]

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": 666,
                    "name": user.name,
                    "email": user.email,
                    "custom:isMaua": True
                }
            }
        )

        response = controller(request=request)

        assert response.status_code == 400

    def test_delete_controller_user_id_none(self):
        repo = UserRepositoryMock()
        usecase = DeleteUserUsecase(repo=repo)
        controller = DeleteUserController(usecase=usecase)
        user = repo.users_list[0]

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": None,
                    "name": user.name,
                    "email": user.email,
                    "custom:isMaua": True
                }
            }
        )

        response = controller(request=request)

        assert response.status_code == 400

    def test_delete_controller_user_id_not_found(self):
        repo = UserRepositoryMock()
        usecase = DeleteUserUsecase(repo=repo)
        controller = DeleteUserController(usecase=usecase)
        user = repo.users_list[0]

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "name": user.name,
                    "email": user.email,
                    "custom:isMaua": True
                }
            }
        )

        response = controller(request=request)

        assert response.status_code == 404