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

        user = user_repo.users_list[3]

        users = usecase(user.user_id, restaurant=user.restaurant)

        viewmodel = GetAllUsersByRestaurantViewModel(users).to_dict()

        expected = {
            'users': [
                {
                    'user': 'João Brancas',
                    'restaurant': RESTAURANT.SOUZA_DE_ABREU.value,
                    'role': ROLE.OWNER.value
                },
            ],
            'message': 'the users with restaurant were retrieved'
        }

        assert sorted(viewmodel['users'], key=lambda x: x['user']) == sorted(expected['users'], key=lambda x: x['user'])