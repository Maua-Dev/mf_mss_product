from src.modules.delete_user.app.delete_user_viewmodel import DeleteUserViewmodel
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_DeleteUserViewmodel:
    def test_delete_user_viewmodel(self):
        repo = UserRepositoryMock()
        viewmodel = DeleteUserViewmodel(repo.users_list[0])

        expected = {
            "user":{
                'user_id': "Lucas Duez",
                'name': "lucas.santos@gmail.com",
                'email': "lucas.santos@gmail.com",
                'restaurant': None,
                'role': "ADMIN",
            },
            "message": "the user was deleted"
        }