import json
from src.modules.create_product.app.create_product_presenter import lambda_handler
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from tests.shared.helpers.get_event_for_presenter_tests import get_event_for_test_presenter


class Test_CreateProductPresenter:
    def test_create_product_presenter(self):
        repo = UserRepositoryMock()
        user = repo.users_list[0]

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
                    "available": True,
                    "name": "Misto",
                    "price": 16.0,
                    "description": "Mussarela e Presunto",
                    "meal_type": "SANDWICHES",
                    "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
                    "restaurant": "HORA_H",
                    "prepare_time": 15
            },
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 201
        assert json.loads(response["body"])["message"] == "the product was created"
        assert json.loads(response["body"])["product"]["available"] == True
        assert json.loads(response["body"])["product"]["price"] == 16.0
        assert json.loads(response["body"])["product"]["name"] == "Misto"
        assert json.loads(response["body"])["product"]["description"] == "Mussarela e Presunto"
        assert json.loads(response["body"])["product"]["meal_type"] == "SANDWICHES"
        assert json.loads(response["body"])["product"][
                   "photo"] == "https://avatars.githubusercontent.com/u/30812461?v=4"
        assert json.loads(response["body"])["product"]["restaurant"] == "HORA_H"
        assert json.loads(response["body"])["product"]["prepare_time"] == 15

    def test_create_product_presenter_price_is_missing(self):
        event = {'version': '2.0', 'routeKey': '$default', 'rawPath': '/my/path',
                 'rawQueryString': 'parameter1=value1&parameter1=value2&parameter2=value',
                 'cookies': ['cookie1', 'cookie2'], 'headers': {'header1': 'value1', 'header2': 'value1,value2'},
                 'queryStringParameters': {'parameter1': '1'},
                 'requestContext': {'accountId': '123456789012', 'apiId': '<urlid>', 'authentication': None,
                                    "authorizer": {
                                        "claims":
                                            {
                                                "sub": "d61dbf66-a10f-11ed-a8fc-0242ac120002",
                                                "name": "Vitinho Molhas",
                                                "email": "molhas@maua.br",
                                                "custom:isMaua": True
                                            }
                                    }, 'domainName': '<url-id>.lambda-url.us-west-2.on.aws', 'domainPrefix': '<url-id>',
                                    'external_interfaces': {'method': 'POST', 'path': '/my/path',
                                                            'protocol': 'HTTP/1.1', 'sourceIp': '123.123.123.123',
                                                            'userAgent': 'agent'}, 'requestId': 'id',
                                    'routeKey': '$default', 'stage': '$default', 'time': '12/Mar/2020:19:03:58 +0000',
                                    'timeEpoch': 1583348638390},
                 "body": {
                         "available": True,
                         "name": "Misto",
                         "description": "Mussarela e Presunto",
                         "meal_type": "SANDWICHES",
                         "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
                         "restaurant": "HORA_H",
                         "prepare_time": 15
                 },
                 'pathParameters': None, 'isBase64Encoded': None, 'stageVariables': None}
        response = lambda_handler(event, None)

        assert json.loads(response["body"]) == "Field price is missing"
        assert response["statusCode"] == 400

    def test_create_product_presenter_name_is_missing(self):
        event = {'version': '2.0', 'routeKey': '$default', 'rawPath': '/my/path',
                 'rawQueryString': 'parameter1=value1&parameter1=value2&parameter2=value',
                 'cookies': ['cookie1', 'cookie2'], 'headers': {'header1': 'value1', 'header2': 'value1,value2'},
                 'queryStringParameters': {'parameter1': '1'},
                 'requestContext': {'accountId': '123456789012', 'apiId': '<urlid>', 'authentication': None,
                                    "authorizer": {
                                        "claims":
                                            {
                                                "sub": "d61dbf66-a10f-11ed-a8fc-0242ac120002",
                                                "name": "Vitinho Molhas",
                                                "email": "molhas@maua.br",
                                                "custom:isMaua": True
                                            }
                                    }, 'domainName': '<url-id>.lambda-url.us-west-2.on.aws', 'domainPrefix': '<url-id>',
                                    'external_interfaces': {'method': 'POST', 'path': '/my/path',
                                                            'protocol': 'HTTP/1.1', 'sourceIp': '123.123.123.123',
                                                            'userAgent': 'agent'}, 'requestId': 'id',
                                    'routeKey': '$default', 'stage': '$default', 'time': '12/Mar/2020:19:03:58 +0000',
                                    'timeEpoch': 1583348638390},
                 "body": {
                         "available": True,
                         "price": 16.0,
                         "description": "Mussarela e Presunto",
                         "meal_type": "SANDWICHES",
                         "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
                         "restaurant": "HORA_H",
                         "prepare_time": 15
                 },
                 'pathParameters': None, 'isBase64Encoded': None, 'stageVariables': None}

        response = lambda_handler(event, None)

        assert json.loads(response["body"]) == "Field name is missing"
        assert response["statusCode"] == 400

    def test_create_product_with_negative_prepare_time(self):
        event = get_event_for_test_presenter(
            body={
                "available": True,
                "name": "Misto",
                "price": 16.0,
                "description": "Mussarela e Presunto",
                "meal_type": "SANDWICHES",
                "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
                "restaurant": "HORA_H",
                "prepare_time": -15
            }
        )

        response = lambda_handler(event, None)

        assert response["statusCode"] == 400

    def test_create_product_with_negative_price(self):
        event = get_event_for_test_presenter(
            body={
                "available": True,
                "name": "Misto",
                "price": -16.0,
                "description": "Mussarela e Presunto",
                "meal_type": "SANDWICHES",
                "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
                "restaurant": "HORA_H",
                "prepare_time": 15
            }
        )

        response = lambda_handler(event, None)

        assert response["statusCode"] == 400

    def test_create_product_with_none_price(self):
        event = get_event_for_test_presenter(
            body={
                "available": True,
                "name": "Misto",
                "price": None,
                "description": "Mussarela e Presunto",
                "meal_type": "SANDWICHES",
                "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
                "restaurant": "HORA_H",
                "prepare_time": 15
            }
        )

        response = lambda_handler(event, None)

        assert response["statusCode"] == 400

    def test_create_product_with_void_description(self):
        event = get_event_for_test_presenter(
            body={
                "available": True,
                "name": "Misto",
                "price": 42,
                "description": "",
                "meal_type": "SANDWICHES",
                "photo": "https://avatars.githubusercontent.com/u/30812461?v=4",
                "restaurant": "HORA_H",
                "prepare_time": 15
            }
        )

        response = lambda_handler(event, None)

        assert response["statusCode"] == 201
