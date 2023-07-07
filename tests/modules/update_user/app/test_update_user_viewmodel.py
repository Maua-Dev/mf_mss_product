from src.modules.update_user.app.update_user_viewmodel import UpdateUserViewmodel
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE

user = User(name="Lucas Duez", email="lucas.santos@maua.br", user_id="93bc6ada-c0d1-7054-66ab-e17414c48bbb",
            role=ROLE.USER)


class Test_UserViewmodel:
    user_viewmodel = UpdateUserViewmodel(user)

    def test_viewmodel(self):
        response = self.user_viewmodel.to_dict()

        expected = {
            "user": {
                "user_name": "Lucas Duez",
                "user_email": "lucas.santos@maua.br",
                "role": "USER",
                "user_id": "93bc6ada-c0d1-7054-66ab-e17414c48bbb",
                "restaurant": None
            },
            "message": "the user was updated"
        }

        assert response == expected

