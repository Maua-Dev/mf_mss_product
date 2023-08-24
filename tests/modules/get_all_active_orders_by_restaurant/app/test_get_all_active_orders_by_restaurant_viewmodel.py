from src.modules.get_all_active_orders_by_restaurant.app.get_all_active_orders_by_restaurant_usecase import GetAllActiveOrdersByRestaurantUsecase
from src.modules.get_all_active_orders_by_restaurant.app.get_all_active_orders_by_restaurant_viewmodel import GetAllActiveOrdersByRestaurantViewmodel
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.domain.enums.restaurant_enum import RESTAURANT

class Test_GetAllActiveOrdersByRestaurantViewmodel:
    def test_get_all_active_orders_by_restaurant_viewmodel(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllActiveOrdersByRestaurantUsecase(repo_order, repo_user)
        all_active_orders = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb")
        viewmodel = GetAllActiveOrdersByRestaurantViewmodel(all_active_orders)

        expected = {
                    'all_active_orders': [{'aborted_reason': None,
                                           'creation_time_milliseconds': 1692156322,
                                           'observation': None,
                                           'order_id': 'd4c63753-5119-4990-b427-926798499924',
                                           'products': [{'product_id':'9589b258-ed44-4c24-b7d6-e96ae221baae', 
                                                         'product_name':'Carteira',
                                                         'quantity':3}],
                                           'restaurant': 'CANTINA_DO_MOLEZA',
                                           'status': 'PREPARING',
                                           'total_price': 25.5,
                                           'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48af9',
                                           'user_name':'Rodrigo Morales'}],
                    'message': 'the active orders were retrieved',
                    }

        assert viewmodel.to_dict() == expected