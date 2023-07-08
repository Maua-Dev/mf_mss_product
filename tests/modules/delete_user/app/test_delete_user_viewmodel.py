from src.modules.delete_user.app.delete_user_viewmodel import DeleteUserViewmodel
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_DeleteUserViewmodel:
    def test_delete_user_viewmodel(self):
        repo = UserRepositoryMock()
        viewmodel = DeleteUserViewmodel(repo.users_list[0])

        expected = {
            "user":{
                'user_id': "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                'name': "Lucas Duez",
                'email': "lucas.santos@gmail.com",
                'restaurant': None,
                'role': "ADMIN",
            },
            "message": "the user was deleted"
        }

        assert viewmodel.to_dict() == expected