import datetime
import json
from src.modules.update_product.app.update_product_presenter import lambda_handler
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

user_repo = UserRepositoryMock()
user = user_repo.users_list[0]

class Test_UpdateProductPresenter:
    def test_update_product_presenter(self):
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
            "queryStringParameters": {
                'query_params': "value1"
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
            "body": """{

                "product_id": "8a705b91-c9e9-4353-a755-07f13afafed3",
                "restaurant": "SOUZA_DE_ABREU",
                "new_available": "True",
                "new_price": 15.0,
                "new_name": "Nome Atualizado",
                "new_description": "Descrição Atualizada",
                "new_prepare_time": 20,
                "new_meal_type":"DRINKS",
                "new_photo": "new_photo"
            }""",
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        expected = {
            'product_id':'8a705b91-c9e9-4353-a755-07f13afafed3',
            'restaurant':'SOUZA_DE_ABREU',
            'available':True,
            'price':15.0,
            'name':'Nome Atualizado',
            'description':'Descrição Atualizada',
            'prepare_time':20,
            'meal_type':'DRINKS',
            'photo':'new_photo',
            'last_update': int(datetime.datetime.now().timestamp())
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 200
        assert json.loads(response["body"])['product'] == expected
        assert json.loads(response["body"])['message'] == "the product was updated"

    def test_update_product_presenter_product_id_is_missing(self):
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
            "queryStringParameters": {
                'query_params': "value1"
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
            "body": '{"restaurant": "SOUZA_DE_ABREU", "new_available": "True", "new_price": 15.0, "new_name": "Nome Atualizado", "new_description": "Descrição Atualizada", "new_prepare_time": 20, "new_meal_type":"DRINKS", "new_photo": "new_photo"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field product_id is missing"

    def test_update_product_presenter_restaurant_is_missing(self):
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
            "queryStringParameters": {
                'query_params': "value1"
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
            "body": '{"product_id": "8a705b91-c9e9-4353-a755-07f13afafed3", "new_available": "True", "new_price": 15.0, "new_name": "Nome Atualizado", "new_description": "Descrição Atualizada", "new_prepare_time": 20, "new_meal_type":"DRINKS", "new_photo": "new_photo"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field restaurant is missing"

    def test_update_product_presenter_restaurant_not_found(self):
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
            "queryStringParameters": {
                'query_params': "value1"
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
            "body": '{"product_id": "8a705b91-c9e9-4353-a755-07f13afafed3", "restaurant": "SOUZINHA", "new_available": "True", "new_price": 15.0, "new_name": "Nome Atualizado", "new_description": "Descrição Atualizada", "new_prepare_time": 20, "new_meal_type":"DRINKS", "new_photo": "new_photo"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == "No items found for restaurant"

    def test_update_product_presenter_meal_type_not_found(self):
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
            "queryStringParameters": {
                'query_params': "value1"
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
            "body": '{"product_id": "8a705b91-c9e9-4353-a755-07f13afafed3", "restaurant": "SOUZA_DE_ABREU", "new_available": "True", "new_price": 15.0, "new_name": "Nome Atualizado", "new_description": "Descrição Atualizada", "new_prepare_time": 20, "new_meal_type":"BEBIDINHAS", "new_photo": "new_photo"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == "No items found for new_meal_type"