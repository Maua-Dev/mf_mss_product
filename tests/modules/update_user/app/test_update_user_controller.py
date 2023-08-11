from src.modules.update_user.app.update_user_controller import UpdateUserController
from src.modules.update_user.app.update_user_usecase import UpdateUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateUserController:
    def test_update_user_controller(self):
        repo_mock = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo_mock)
        first_user = repo_mock.users_list[0]

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": first_user.user_id,
                    "name": first_user.name,
                    "email": first_user.email,
                    "custom:isMaua": True
                },

                "new_name": "Meu novo nome",
                "new_photo": "https://www.thestatesman.com/wp-content/uploads/2022/07/AmericanBullysobakabarobaka-4ce0d4dc0e144dccadb5159b222e275e-e1657808052501.jpg"
            }
        )

        expected_dict = {
            "user": {
                "name": "Meu novo nome",
                "email": first_user.email,
                "role": first_user.role.value,
                "user_id": first_user.user_id,
                "restaurant": first_user.restaurant,
                "photo": "https://www.thestatesman.com/wp-content/uploads/2022/07/AmericanBullysobakabarobaka-4ce0d4dc0e144dccadb5159b222e275e-e1657808052501.jpg"
            },
            "message": "the user was updated"
        }

        controller = UpdateUserController(usecase=usecase)

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body == expected_dict

    def test_update_user_with_name_of_other_user(self):
        repo_mock = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo_mock)
        first_user = repo_mock.users_list[0]

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": first_user.user_id,
                    "name": first_user.name,
                    "email": first_user.email,
                    "custom:isMaua": True
                },
                "new_name": repo_mock.users_list[-1].name
            }
        )

        expected_dict = {
            "user": {
                "name": repo_mock.users_list[-1].name,
                "email": first_user.email,
                "role": first_user.role.value,
                "user_id": first_user.user_id,
                "restaurant": first_user.restaurant,
                "photo": first_user.photo
            },
            "message": "the user was updated"
        }

        controller = UpdateUserController(usecase=usecase)

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body == expected_dict

    # def test_update_user_with_email_of_other_user(self):
    #     repo_mock = UserRepositoryMock()
    #     usecase = UpdateUserUsecase(repo_mock)
    #     first_user = repo_mock.users_list[0]
    #
    #     request = HttpRequest(
    #         body={
    #             'requester_user': {
    #                 "sub": first_user.user_id,
    #                 "name": "Um novo nome",
    #                 "email": repo_mock.users_list[-1].email,
    #                 "custom:isMaua": True
    #             }
    #         }
    #     )
    #
    #     expected_dict = {
    #         "user": {
    #             "name": "Um novo nome",
    #             "email": repo_mock.users_list[-1].email,
    #             "role": first_user.role.value,
    #             "user_id": first_user.user_id,
    #             "restaurant": first_user.restaurant
    #         },
    #         "message": "the user was updated"
    #     }
    #
    #     controller = UpdateUserController(usecase=usecase)
    #
    #     response = controller(request=request)
    #
    #     assert response.status_code == 200
    #     assert response.body == expected_dict

    def test_update_user_with_invalid_id(self):
        repo_mock = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo_mock)
        first_user = repo_mock.users_list[0]

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": "um id inválido",
                    "name": first_user.name,
                    "email": first_user.email,
                    "custom:isMaua": True
                },
                "new_name": "Um nome qualquer"
            }
        )

        controller = UpdateUserController(usecase=usecase)

        response = controller(request=request)

        assert response.status_code == 400

    def test_update_user_with_nonexistent_id(self):
        repo_mock = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo_mock)
        first_user = repo_mock.users_list[0]

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "name": first_user.name,
                    "email": first_user.email,
                    "custom:isMaua": True
                },
                "new_name": "Novo nome"
            }
        )

        controller = UpdateUserController(usecase=usecase)

        response = controller(request=request)

        assert response.status_code == 404

    def test_update_user_with_invalid_name(self):
        repo_mock = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo_mock)
        first_user = repo_mock.users_list[0]

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": first_user.user_id,
                    "name": first_user.name,
                    "email": first_user.email,
                    "custom:isMaua": True
                },
                "new_name": "U"
            }
        )

        controller = UpdateUserController(usecase=usecase)

        response = controller(request=request)

        assert response.status_code == 400
        
    def test_update_user_with_invalid_photo(self):
        repo_mock = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo_mock)
        first_user = repo_mock.users_list[0]

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": first_user.user_id,
                    "name": first_user.name,
                    "email": first_user.email,
                    "custom:isMaua": True
                },
                "new_name": "Michael Jackson",
                "new_photo": 123123
            }
        )

        controller = UpdateUserController(usecase=usecase)

        response = controller(request=request)

        assert response.status_code == 400

    def test_update_user_with_same_name(self):
        repo_mock = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo_mock)
        first_user = repo_mock.users_list[0]

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": first_user.user_id,
                    "name": first_user.name,
                    "email": first_user.email,
                    "custom:isMaua": True
                },
                "new_name": first_user.name
            }
        )

        controller = UpdateUserController(usecase=usecase)

        response = controller(request=request)

        assert response.status_code == 400
        
    def test_update_user_with_same_photo(self):
        repo_mock = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo_mock)
        first_user = repo_mock.users_list[0]

        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": first_user.user_id,
                    "name": first_user.name,
                    "email": first_user.email,
                    "custom:isMaua": True
                },
                "new_name": "Michael Jackson",
                "new_photo": first_user.photo
            }
        )

        controller = UpdateUserController(usecase=usecase)

        response = controller(request=request)

        assert response.status_code == 400


    # def test_update_user_with_invalid_email(self):
    #     repo_mock = UserRepositoryMock()
    #     usecase = UpdateUserUsecase(repo_mock)
    #     first_user = repo_mock.users_list[0]
    #
    #     request = HttpRequest(
    #         body={
    #             'requester_user': {
    #                 "sub": first_user.user_id,
    #                 "name": "Um novo nome",
    #                 "email": "@gmail.com",
    #                 "custom:isMaua": True
    #             }
    #         }
    #     )
    #
    #     controller = UpdateUserController(usecase=usecase)
    #
    #     response = controller(request=request)
    #
    #     assert response.status_code == 400

    # def test_update_user_with_same_email(self):
    #     repo_mock = UserRepositoryMock()
    #     usecase = UpdateUserUsecase(repo_mock)
    #     first_user = repo_mock.users_list[0]
    #
    #     request = HttpRequest(
    #         body={
    #             'requester_user': {
    #                 "sub": first_user.user_id,
    #                 "name": "Um novo nome",
    #                 "email": first_user.email,
    #                 "custom:isMaua": True
    #             }
    #         }
    #     )
    #
    #     controller = UpdateUserController(usecase=usecase)
    #
    #     response = controller(request=request)
    #
    #     assert response.status_code == 400
