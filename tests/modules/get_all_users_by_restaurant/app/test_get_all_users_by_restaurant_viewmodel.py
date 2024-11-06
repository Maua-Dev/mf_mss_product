from src.modules.get_all_users_by_restaurant.app.get_all_users_by_restaurant_viewmodel import GetAllUsersByRestaurantViewModel
from src.modules.get_all_users_by_restaurant.app.get_all_users_by_restaurant_usecase import GetAllUsersByRestaurantUseCase
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllUsersByRestaurantViewmodel:
    def test_get_all_users_by_restaurant(self):
        user_repo = UserRepositoryMock()
        order_repo = OrderRepositoryMock()
        usecase = GetAllUsersByRestaurantUseCase(user_repo, order_repo)

        users = usecase('93bc6ada-c0d1-7054-66ab-e17414c48af4')

        viewmodel = GetAllUsersByRestaurantViewModel(users).to_dict()
        print(viewmodel)

        expected = {
            'users': [
                {
                    'name': 'João Brancas',
                    'restaurant': 'SOUZA_DE_ABREU',
                    'role': 'OWNER',
                    'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48af4',
                    'email': 'brancas.dev@gmail.com',
                    'photo': 'https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1200:*',
                    'confirm_user': True,
                    'new_confirm_user': True
                }
            ],
            'message': 'the users with restaurant were retrieved'
        }

        assert sorted(viewmodel['users'], key=lambda x: x['name']) == sorted(expected['users'], key=lambda x: x['name'])