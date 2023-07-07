from src.modules.create_user.app.create_user_viewmodel import CreateUserViewmodel
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE

class Test_CreateUserViewModel:
    def test_create_user_viewmodel(self):
        user = User(
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            name="Rodrigo",
            email="rodrigo.morales@gmail.com",
            restaurant=None,
            role=ROLE.USER
        )
        userViewmodel = CreateUserViewmodel(user=user).to_dict()
        expected = {
            "user": {
                'user_id': "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                'name': 'Rodrigo',
                'email': 'rodrigo.morales@gmail.com',
                'restaurant': None,
                'role':'USER',
            },
            'message': 'the user was created successfully'
        }

        assert expected == userViewmodel