import json
from src.modules.get_all_active_orders_by_restaurant.app.get_all_active_orders_by_restaurant_presenter import lambda_handler
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

class Test_GetAllActiveOrdersByRestaurantPresenter:
    def test_get_all_active_orders_by_restaurant_presenter(self):
        repo_user = UserRepositoryMock()
        repo_order = OrderRepositoryMock()
        user = repo_user.users_list[2]

        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/my/path",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "header1": "value1",
                "header2": "value1,value2"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authentication": None,
                "authorizer": {
                    "claims":
                        {
                            "sub": user.user_id,
                            "name": user.name,
                            "email": user.email,
                            "custom:isMaua": True
                        }
                },
                "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
                "domainPrefix": "<url-id>",
                "external_interfaces": {
                    "method": "POST",
                    "path": "/my/path",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "123.123.123.123",
                    "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": 'Visualize all the active orders',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

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

        assert response["statusCode"] == 200
        assert json.loads(response["body"])["message"] == "the active orders were retrieved"
        assert json.loads(response["body"]) == expected

