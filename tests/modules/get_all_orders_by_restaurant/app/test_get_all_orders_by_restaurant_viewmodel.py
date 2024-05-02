from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.modules.get_all_orders_by_restaurant.app.get_all_orders_by_restaurant_usecase import \
    GetAllOrdersByRestaurantUsecase
from src.modules.get_all_orders_by_restaurant.app.get_all_orders_by_restaurant_viewmodel import \
    GetAllOrdersByRestaurantViewmodel


class Test_GetAllOrdersByRestaurantViewmodel:
    def test_get_all_active_orders_by_restaurant_viewmodel(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllOrdersByRestaurantUsecase(repo_order, repo_user)
        all_orders = usecase(user_id=repo_user.users_list[3].user_id,
                             exclusive_start_key="1eeef881-1b1f-4f38-a662-8ff7156e6c27")
        viewmodel = GetAllOrdersByRestaurantViewmodel(all_orders)

        expected = {
            'all_orders_by_restaurant': [
                {
                    "order_id": "1eeef881-1b1f-4f38-a662-8ff7156e6c27",
                    "user_name": "Gabriel G Godoy",
                    "user_id": "93bc6ada-c0d1-7054-42je-e17414c48af1",
                    "products": [
                        {
                            "product_name": "Pão de Queijo",
                            "product_id": "0165b801-04c5-41b7-82bb-10f1501333ae",
                            "quantity": 2,
                            "observation": None
                        },
                        {
                            "product_name": "Capuccino - gde.",
                            "product_id": "4e6979d6-c9c3-438e-9b8c-e4d799358720",
                            "quantity": 1,
                            "observation": None
                        },
                        {
                            "product_name": "Paçoquita",
                            "product_id": "79e2706e-7621-43ab-b6d1-82aeb45fc57c",
                            "quantity": 3,
                            "observation": None
                        }
                    ],
                    "creation_time_milliseconds": 1692157822000,
                    "restaurant": "SOUZA_DE_ABREU",
                    "status": "REFUSED",
                    "aborted_reason": None,
                    "total_price": 35.5,
                    "last_status_update": 1992061596999,
                    "action": "NEW",
                                    'time_reserved': None
                }

            ],
            'last_order_id': '1eeef881-1b1f-4f38-a662-8ff7156e6c27',
            'message': 'the orders were retrieved',

        }

        assert viewmodel.to_dict() == expected
