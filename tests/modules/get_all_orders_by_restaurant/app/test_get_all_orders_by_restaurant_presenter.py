import json

from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.modules.get_all_orders_by_restaurant.app.get_all_orders_by_restaurant_presenter import lambda_handler


class Test_GetAllOrdersByRestaurantPresenter:

    def test_lambda_handler_with_order_id(self):
        user = UserRepositoryMock().users_list[3]
        order = OrderRepositoryMock().orders[9]

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
            "body": {
                "order_id": order.order_id,
            },
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        response = lambda_handler(event, None)
        expected_all_orders = ["135ef881-1b1f-4f38-a662-8ff7156e6c27", '1eeef881-1b1f-4f38-a662-8ff7156e6c27']

        assert response['statusCode'] == 200
        assert json.loads(response['body'])['message'] == "the orders were retrieved"
        assert [order_id["order_id"] for order_id in json.loads(response['body'])['all_orders']] == expected_all_orders

    def test_lambda_handler_without_order_id(self):
        user = UserRepositoryMock().users_list[3]
        order = OrderRepositoryMock().orders[9]

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
            "body": 'Visualize all orders from a restaurant',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        expected_len_all_orders = 7

        assert response['statusCode'] == 200
        assert json.loads(response['body'])['message'] == "the orders were retrieved"
        assert len(json.loads(response['body'])['all_orders']) == expected_len_all_orders