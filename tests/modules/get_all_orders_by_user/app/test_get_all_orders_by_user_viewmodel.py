from src.modules.get_all_orders_by_user.app.get_all_orders_by_user_usecase import GetAllOrdersByUserUsecase
from src.modules.get_all_orders_by_user.app.get_all_orders_by_user_viewmodel import GetAllOrdersByUserViewmodel
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllOrdersByUserViewmodel:
    def test_get_all_orders_by_user_viewmodel(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)

        all_orders = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48af9", order_id="d4c63753-5119-4990-b427-926798499924")
        viewmodel = GetAllOrdersByUserViewmodel(all_orders)

        expected = {
            'all_orders_by_user': [{
                'aborted_reason': None,
                'creation_time_milliseconds': 1692156322000,
                'observation': None,
                'order_id': "d4c63753-5119-4990-b427-926798499924",
                'products': [{
                        'product_id':'9589b258-ed44-4c24-b7d6-e96ae221baae', 
                        'product_name':'Carteira',
                        'quantity':3
                        }],
                'restaurant': 'CANTINA_DO_MOLEZA',
                'status': 'PREPARING',
                'total_price': 25.5,
                'user_id': "93bc6ada-c0d1-7054-66ab-e17414c48af9",
                'user_name':'Rodrigo Morales'
            }],
            'message': 'the orders were retrieved',
        }

        assert viewmodel.to_dict() == expected

    def test_get_all_orders_by_user_several_orders(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByUserUsecase(repo_order, repo_user)

        all_orders = usecase(user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf", order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53")
        viewmodel = GetAllOrdersByUserViewmodel(all_orders)

        expected = {
            'all_orders_by_user': [{
                'aborted_reason': None,
                'creation_time_milliseconds': 1692061296000,
                'observation': "Capricha no morango",
                'order_id': "b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
                'products': [{
                        'product_id':'4081a83a-516f-442c-85e2-b54bfb192e55', 
                        'product_name':'Cimento (400mL)',
                        'quantity':2
                        }],
                'restaurant': 'CANTINA_DO_MOLEZA',
                'status': 'READY',
                'total_price': 30.00,
                'user_id': "93bc6ada-c0d1-7054-66ab-e17414c48gbf",
                'user_name':'Lucas Milas'
            },
            {
                'aborted_reason': None,
                'creation_time_milliseconds': 1692061297000,
                'observation': None,
                'order_id': "b3f6c5aa-80ad-4f95-ae16-455b4f874553",
                'products': [{
                        'product_id':'6624e731-1301-4b24-a036-1e7f2553e023', 
                        'product_name':'Salada de Frutas',
                        'quantity':2
                        }],
                'restaurant': 'CANTINA_DO_MOLEZA',
                'status': 'READY',
                'total_price': 14.00,
                'user_id': "93bc6ada-c0d1-7054-66ab-e17414c48gbf",
                'user_name':'Lucas Milas'
            }],
            'message': 'the orders were retrieved',
        }

        assert viewmodel.to_dict() == expected
        