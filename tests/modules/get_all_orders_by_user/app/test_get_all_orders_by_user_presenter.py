import json
from src.modules.get_all_orders_by_user.app.get_all_orders_by_user_presenter import lambda_handler
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllOrdersByUserPresenter:
    def test_get_all_orders_by_user_presenter(self):
        repo_user = UserRepositoryMock().users_list

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
                                "sub": repo_user[5].user_id,
                                "name": repo_user[5].name,
                                "email": repo_user[5].email,
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
                "body": {'exclusive_start_key': "d4c63753-5119-4990-b427-926798499924"},
                "pathParameters": None,
                "isBase64Encoded": None,
                "stageVariables": None
            }

        response = lambda_handler(event, None)

        expected = {
            'all_orders_by_user': [{'aborted_reason': None,
                                    'creation_time_milliseconds': 1692156322000,
                                    'last_status_update': 1992061596999,
                                    'observation': None,
                                    'order_id': 'd4c63753-5119-4990-b427-926798499924',
                                    'products': [{'product_id': '9589b258-ed44-4c24-b7d6-e96ae221baae',
                                                  'product_name': 'Carteira',
                                                  'quantity': 3}],
                                    'restaurant': 'CANTINA_DO_MOLEZA',
                                    'status': 'PREPARING',
                                    'total_price': 25.5,
                                    'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48af9',
                                    'user_name': 'Rodrigo Morales'}],
            'last_order_id': 'd4c63753-5119-4990-b427-926798499924',
            'message': 'the orders were retrieved',
           }
        
        assert response["statusCode"] == 200
        assert json.loads(response["body"])["message"] == "the orders were retrieved"
        assert json.loads(response["body"]) == expected

    def test_get_all_orders_by_user_presenter_several_orders(self):
        repo_user = UserRepositoryMock().users_list

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
                                "sub": repo_user[4].user_id,
                                "name": repo_user[4].name,
                                "email": repo_user[4].email,
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
                "body": {'exclusive_start_key': "b3f6c5aa-80ad-4f95-ae16-455b4f87fb53", 'amount': 2},
                "pathParameters": None,
                "isBase64Encoded": None,
                "stageVariables": None
            }

        response = lambda_handler(event, None)

        expected = {
            'all_orders_by_user': [{
                'aborted_reason': None,
                'creation_time_milliseconds': 1692061296000,
                'last_status_update': 1992061596999,
                'observation': 'Capricha no morango',
                'order_id': 'b3f6c5aa-80ad-4f95-ae16-455b4f87fb53',
                'products': [{'product_id': '4081a83a-516f-442c-85e2-b54bfb192e55',
                              'product_name': 'Cimento (400mL)',
                              'quantity': 2}],
                'restaurant': 'CANTINA_DO_MOLEZA',
                'status': 'READY',
                'total_price': 30.0,
                'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48gbf',
                'user_name': 'Lucas Milas'},

                {
                'aborted_reason': None,
                'creation_time_milliseconds': 1692061297000,
                'last_status_update': 1992061596999,
                'observation': None,
                'order_id': 'b3f6c5aa-80ad-4f95-ae16-455b4f874553',
                'products': [{'product_id': '6624e731-1301-4b24-a036-1e7f2553e023',
                              'product_name': 'Salada de Frutas',
                              'quantity': 2}],
                'restaurant': 'CANTINA_DO_MOLEZA',
                'status': 'READY',
                'total_price': 14.0,
                'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48gbf',
                'user_name': 'Lucas Milas'}],
            'last_order_id': 'b3f6c5aa-80ad-4f95-ae16-455b4f874553',
            'message': 'the orders were retrieved'
           }
        
        assert response["statusCode"] == 200
        assert json.loads(response["body"])["message"] == "the orders were retrieved"
        assert json.loads(response["body"]) == expected

    def test_get_all_orders_by_user_presenter_without_exclusive_start_key(self):
        repo_user = UserRepositoryMock().users_list

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
                                "sub": repo_user[4].user_id,
                                "name": repo_user[4].name,
                                "email": repo_user[4].email,
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
                "body": {"amount": 1},
                "pathParameters": None,
                "isBase64Encoded": None,
                "stageVariables": None
            }

        response = lambda_handler(event, None)

        expected = {
            'all_orders_by_user': [{
                'order_id': 'b3f6c5aa-80ad-4f95-ae16-455b4f87fb53', 
                'user_name': 'Lucas Milas', 
                'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48gbf', 
                'products': [{
                    'product_name': 'Cimento (400mL)', 
                    'product_id': '4081a83a-516f-442c-85e2-b54bfb192e55', 
                    'quantity': 2}], 
                'creation_time_milliseconds': 1692061296000, 
                'restaurant': 'CANTINA_DO_MOLEZA', 
                'observation': 'Capricha no morango', 
                'status': 'READY', 
                'aborted_reason': None, 
                'total_price': 30.0, 
                'last_status_update': 1992061596999}], 
            'last_order_id': 'b3f6c5aa-80ad-4f95-ae16-455b4f87fb53',
            'message': 'the orders were retrieved'}
        
        assert response["statusCode"] == 200
        assert json.loads(response["body"])["message"] == "the orders were retrieved"
        assert json.loads(response["body"]) == expected

    def test_get_all_orders_by_user_presenter_requester_user_none(self):
        repo_user = UserRepositoryMock().users_list

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
                "body": {'exclusive_start_key': "d4c63753-5119-4990-b427-926798499924"},
                "pathParameters": None,
                "isBase64Encoded": None,
                "stageVariables": None
            }

        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field requester_user is missing"

    def test_get_all_orders_by_user_presenter_unregister_user(self):
        repo_user = UserRepositoryMock().users_list

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
                                "sub": "id",
                                "name": repo_user[5].name,
                                "email": repo_user[5].email,
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
                "body": {'exclusive_start_key': "d4c63753-5119-4990-b427-926798499924"},
                "pathParameters": None,
                "isBase64Encoded": None,
                "stageVariables": None
            }

        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "That user is not registered"

    def test_get_all_orders_by_user_presenter_order_not_found(self):
        repo_user = UserRepositoryMock().users_list

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
                                "sub": repo_user[5].user_id,
                                "name": repo_user[5].name,
                                "email": repo_user[5].email,
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
                "body": {'exclusive_start_key': "d4c63753-5119-4990-b427-926798496664"},
                "pathParameters": None,
                "isBase64Encoded": None,
                "stageVariables": None
            }

        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == "No items found for exclusive_start_key"

    def test_get_all_orders_by_user_presenter_mismatch_id(self):
        repo_user = UserRepositoryMock().users_list

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
                                "sub": repo_user[4].user_id,
                                "name": repo_user[4].name,
                                "email": repo_user[4].email,
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
                "body": {'exclusive_start_key': "d4c63753-5119-4990-b427-926798499924"},
                "pathParameters": None,
                "isBase64Encoded": None,
                "stageVariables": None
            }

        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "The user_id does not match with the inserted order_id"