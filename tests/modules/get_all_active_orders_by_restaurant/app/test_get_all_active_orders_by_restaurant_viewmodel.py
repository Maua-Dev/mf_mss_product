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
    
        expected = {'all_active_orders': 
                    [{'order_id': 'b3f6c5aa-80ad-4f95-ae16-455b4f87fb53', 
                      'user_name': 'Lucas Milas', 
                      'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48gbf', 
                      'products': [{'product_name': 'Cimento (400mL)', 
                                    'product_id': '4081a83a-516f-442c-85e2-b54bfb192e55', 
                                    'quantity': 2, 
                                    'observation': None}], 
                      'creation_time_milliseconds': 1692061296000, 
                      'restaurant': 'CANTINA_DO_MOLEZA', 
                      'status': 'READY', 
                      'aborted_reason': None, 
                      'total_price': 30.0, 
                      'action': 'NEW'},
                      {'order_id': 'b3f6c5aa-80ad-4f95-ae16-455b4f874553', 
                       'user_name': 'Lucas Milas', 
                       'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48gbf', 
                       'products': [{'product_name': 'Salada de Frutas', 
                                     'product_id': '6624e731-1301-4b24-a036-1e7f2553e023', 
                                     'quantity': 2, 'observation': None}], 
                        'creation_time_milliseconds': 1692061297000, 
                        'restaurant': 'CANTINA_DO_MOLEZA', 
                        'status': 'READY', 
                        'aborted_reason': None, 
                        'total_price': 14.0, 
                        'action': 'EDITED'},                         
                      {'order_id': 'd4c63753-5119-4990-b427-926798499924', 
                       'user_name': 'Rodrigo Morales', 
                       'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48af9', 
                       'products': [{'product_name': 'Carteira', 
                                     'product_id': '9589b258-ed44-4c24-b7d6-e96ae221baae', 
                                     'quantity': 3, 
                                     'observation': None}], 
                        'creation_time_milliseconds': 1692156322000, 
                        'restaurant': 'CANTINA_DO_MOLEZA', 
                        'status': 'PREPARING', 
                        'aborted_reason': None, 
                        'total_price': 25.5, 
                        'action': 'EDITED'}], 
                    'message': 'the active orders were retrieved'}

        assert viewmodel.to_dict() == expected