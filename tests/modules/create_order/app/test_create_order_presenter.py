import json
from src.modules.create_order.app.create_order_presenter import lambda_handler
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_CreateOrderPresenter:
    def test_create_order_presenter(self):
        repo_product = ProductRepositoryMock()

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
                            "sub": "93bc6ada-c0d1-7054-66ab-e17414c48gbf",
                            "name": "Lucas Milas",
                            "email": "milas@maua.br",
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
                "products": [{
                    "product_name": repo_product.products[0].name,
                    "product_id": repo_product.products[0].product_id,
                    "quantity": 2,
                }],
                "restaurant": repo_product.products[0].restaurant.value,
            },
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
    
        assert response["statusCode"] == 201
        assert json.loads(response["body"])["message"] == "the order was created"
        assert json.loads(response["body"])["order"]["user_name"] == "Lucas Milas"
        assert json.loads(response["body"])["order"]["user_id"] == "93bc6ada-c0d1-7054-66ab-e17414c48gbf"
        assert json.loads(response["body"])["order"]["products"][0]["product_name"] == "X-Salada"
        assert json.loads(response["body"])["order"]["products"][0]["product_id"] == "8a705b91-c9e9-4353-a755-07f13afafed3"
        assert json.loads(response["body"])["order"]["products"][0]["quantity"] == 2
        assert json.loads(response["body"])["order"]["restaurant"] == "SOUZA_DE_ABREU"
        assert json.loads(response["body"])["order"]["status"] == "PENDING"
        assert json.loads(response["body"])["order"]["total_price"] == 38.00

    def test_create_order_presenter_products_none(self):
        repo_product = ProductRepositoryMock()

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
                            "sub": "93bc6ada-c0d1-7054-66ab-e17414c48gbf",
                            "name": "Lucas Milas",
                            "email": "milas@maua.br",
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
                "restaurant": repo_product.products[0].restaurant.value,
            },
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
    
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field products is missing"

    def test_create_order_presenter_restaurant_none(self):
        repo_product = ProductRepositoryMock()

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
                            "sub": "93bc6ada-c0d1-7054-66ab-e17414c48gbf",
                            "name": "Lucas Milas",
                            "email": "milas@maua.br",
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
                "products": [{
                    "product_name": repo_product.products[0].name,
                    "product_id": repo_product.products[0].product_id,
                    "quantity": 2
                }],
            },
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
    
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field restaurant is missing"

    def test_create_order_presenter_restaurant_not_found(self):
        repo_product = ProductRepositoryMock()

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
                            "sub": "93bc6ada-c0d1-7054-66ab-e17414c48gbf",
                            "name": "Lucas Milas",
                            "email": "milas@maua.br",
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
                "products": [{
                    "product_name": repo_product.products[0].name,
                    "product_id": repo_product.products[0].product_id,
                    "quantity": 2
                }],
                "restaurant": "Tech Food",
            },
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
    
        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == "Field 'Tech Food' is not a restaurant"

