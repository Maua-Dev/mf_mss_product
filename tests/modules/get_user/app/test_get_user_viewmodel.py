from src.modules.get_user.app.get_user_viewmodel import GetUserViewmodel
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE

user = User(name="Lucas Duez", email="lucas.santos@maua.br", user_id="93bc6ada-c0d1-7054-66ab-e17414c48bbb",
            role=ROLE.USER)


class Test_UserViewmodel:
    user_viewmodel = GetUserViewmodel(user)

    def test_viewmodel(self):
        response = self.user_viewmodel.to_dict()

        expected = {
            "product": {
                "user_name": "Lucas Duez",
                "user_email": "lucas.santos@maua.br",
                "role": "USER",
                "user_id": "93bc6ada-c0d1-7054-66ab-e17414c48bbb",
                "restaurant": None
            },
            "message": "the user was retrieved"
        }

        assert response == expected
    