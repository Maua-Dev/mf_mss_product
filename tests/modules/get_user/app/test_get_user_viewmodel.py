from src.modules.get_user.app.get_user_viewmodel import GetUserViewmodel
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE

user = User(name="Lucas Duez", email="lucas.santos@maua.br", user_id="93bc6ada-c0d1-7054-66ab-e17414c48bbb",
            role=ROLE.USER, restaurant=None, photo="https://img.freepik.com/free-photo/red-white-cat-i-white-studio_155003-13189.jpg?w=2000")


class Test_UserViewmodel:
    user_viewmodel = GetUserViewmodel(user)

    def test_get_user_viewmodel(self):
        response = self.user_viewmodel.to_dict()

        expected = {
            "user": {
                "name": "Lucas Duez",
                "email": "lucas.santos@maua.br",
                "role": "USER",
                "user_id": "93bc6ada-c0d1-7054-66ab-e17414c48bbb",
                "restaurant": None,
                "photo": "https://img.freepik.com/free-photo/red-white-cat-i-white-studio_155003-13189.jpg?w=2000"
            },
            "message": "the user was retrieved"
        }

        assert response == expected
    