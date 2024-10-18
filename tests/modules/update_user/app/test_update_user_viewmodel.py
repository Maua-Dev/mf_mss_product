from src.modules.update_user.app.update_user_viewmodel import UpdateUserViewmodel
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE

user_1 = User(name="Lucas Duez", email="lucas.santos@maua.br", user_id="93bc6ada-c0d1-7054-66ab-e17414c48bbb", confirm_user = True,
            role=ROLE.USER, photo="https://www.thestatesman.com/wp-content/uploads/2022/07/AmericanBullysobakabarobaka-4ce0d4dc0e144dccadb5159b222e275e-e1657808052501.jpg")
user_2 = User(name="Lucas Duez", email="lucas.santos@maua.br", user_id="93bc6ada-c0d1-7054-66ab-e17414c48bbb", confirm_user = False,
            role=ROLE.USER)


class Test_UserViewmodel:
    user_viewmodel_1 = UpdateUserViewmodel(user_1)
    user_viewmodel_2 = UpdateUserViewmodel(user_2)

    def test_viewmodel(self):
        response = self.user_viewmodel_1.to_dict()

        expected = {
            "user": {
                "name": "Lucas Duez",
                "email": "lucas.santos@maua.br",
                "role": "USER",
                "user_id": "93bc6ada-c0d1-7054-66ab-e17414c48bbb",
                "restaurant": None,
                "photo": "https://www.thestatesman.com/wp-content/uploads/2022/07/AmericanBullysobakabarobaka-4ce0d4dc0e144dccadb5159b222e275e-e1657808052501.jpg",
                "confirm_user": True
            },
            "message": "the user was updated"
        }

        assert response == expected

    def test_viewmodel_without_photo(self):
        response = self.user_viewmodel_2.to_dict()

        expected = {
            "user": {
                "name": "Lucas Duez",
                "email": "lucas.santos@maua.br",
                "role": "USER",
                "user_id": "93bc6ada-c0d1-7054-66ab-e17414c48bbb",
                "restaurant": None,
                "photo": None,
                "confirm_user": False
            },
            "message": "the user was updated"
        }

        assert response == expected
