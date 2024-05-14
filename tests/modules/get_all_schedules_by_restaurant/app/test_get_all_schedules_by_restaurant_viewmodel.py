# from src.modules.get_all_schedules_by_restaurant.app.get_all_schedules_by_restaurant_usecase import GetAllSchedulesByRestaurantUsecase
# from src.modules.get_all_schedules_by_restaurant.app.get_all_schedules_by_restaurant_viewmodel import GetAllSchedulesByRestaurantViewmodel
# from src.shared.domain.entities.order import Order
# from src.shared.domain.entities.order_product import OrderProduct
# from src.shared.domain.enums.action_enum import ACTION
# from src.shared.domain.enums.restaurant_enum import RESTAURANT
# from src.shared.domain.enums.status_enum import STATUS
# from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock


# class Test_GetAllSchedulesByRestaurantViewmodel:
#     def test_get_all_schedules_by_restaurant_viewmodel(self):
#         repo_order = OrderRepositoryMock()
#         usecase = GetAllSchedulesByRestaurantUsecase(repo_order)

#         order = Order(order_id="135ef881-1b1f-4f38-a662-8ff7156e6fff", user_name="Lucas Milas",
#                   user_id="93bc6ada-c0d1-7054-66ab-e17414c48gbf", products=[
#                 OrderProduct(product_name="X-Calabresa", product_id="8ffcc3ef-6d35-4fef-abf0-85d3649a85d5",
#                              quantity=2)], creation_time_milliseconds=1692157822666,
#                   restaurant=RESTAURANT.SOUZA_DE_ABREU, status=STATUS.PENDING, total_price=48.0,
#                   aborted_reason=None,
#                   last_status_update_milliseconds=1992061596123, action=ACTION.EDITED, time_reserved=8)

#         create_prod = repo_order.create_order(order)

#         viewmodel = GetAllSchedulesByRestaurantViewmodel(create_prod)

#         expected = {
#             'all_orders_by_user': [{
#                 'aborted_reason': None,
#                 'creation_time_milliseconds': 1692061296000,
#                 'order_id': "b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
#                 'products': [{
#                         'product_id':'4081a83a-516f-442c-85e2-b54bfb192e55', 
#                         'product_name':'Cimento (400mL)',
#                         'quantity':2,
#                         'observation': None,
#                 }],
#                 'restaurant': 'CANTINA_DO_MOLEZA',
#                 'status': 'READY',
#                 'action':'NEW',
#                 'total_price': 30.00,
#                 'user_id': "93bc6ada-c0d1-7054-66ab-e17414c48gbf",
#                 'user_name':'Lucas Milas',
#                 'last_status_update':1992061596999,
#                 'time_reserved': None
#             }],
#             'message': 'the orders were retrieved',
#         }

#         assert viewmodel.to_dict() == expected