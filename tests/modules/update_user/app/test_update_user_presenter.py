import json
from src.modules.update_user.app.update_user_presenter import lambda_handler
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateUserPresenter:

    def test_update_user_presenter(self):
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
                            "sub": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                            "name": "Lucas Duez",
                            "email": "lucas.santos@gmail.com",
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
            "body": {"new_name": "Aaaaaa isso é no presenter", "new_photo":"https://www.thestatesman.com/wp-content/uploads/2022/07/AmericanBullysobakabarobaka-4ce0d4dc0e144dccadb5159b222e275e-e1657808052501.jpg"},
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 200


    def test_update_without_user_id(self):
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
                            "sub": None,
                            "name": "Lucas Duez",
                            "email": "lucas.duzer@gmail.com",
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
            "body": "Hello from client!",
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400


    def test_update_with_invalid_name(self):
        repo_mock = UserRepositoryMock()
        first_user = repo_mock.users_list[0]

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
                            "sub": first_user.user_id,
                            "name": first_user.name,
                            "email": first_user.email,
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
            "body": {"new_name": "L"},
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        
    def test_update_with_invalid_photo(self):
        repo_mock = UserRepositoryMock()
        first_user = repo_mock.users_list[0]

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
                            "sub": first_user.user_id,
                            "name": first_user.name,
                            "email": first_user.email,
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
            "body": {"new_name": "Michael", "new_photo": 12312},
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field user_photo is not valid"



    def test_update_with_same_name(self):
        repo_mock = UserRepositoryMock()
        user = repo_mock.users_list[-1]

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
            "body": {"new_name": user.name},
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        
    def test_update_with_same_photo(self):
        repo_mock = UserRepositoryMock()
        user = repo_mock.users_list[-1]

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
            "body": {"new_name": "Michael", "new_photo": user.photo},
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "The value for user_photo is already the new one"

    # def test_update_with_invalid_email(self):
    #     repo_mock = UserRepositoryMock()
    #     first_user = repo_mock.users_list[0]
    #
    #     event = {
    #         "version": "2.0",
    #         "routeKey": "$default",
    #         "rawPath": "/my/path",
    #         "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
    #         "cookies": [
    #             "cookie1",
    #             "cookie2"
    #         ],
    #         "headers": {
    #             "header1": "value1",
    #             "header2": "value1,value2"
    #         },
    #         "requestContext": {
    #             "accountId": "123456789012",
    #             "apiId": "<urlid>",
    #             "authentication": None,
    #             "authorizer": {
    #                 "claims":
    #                     {
    #                         "sub": first_user.user_id,
    #                         "name": "Meu novo nome",
    #                         "email": "@gmail.com",
    #                         "custom:isMaua": True
    #                     }
    #             },
    #             "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
    #             "domainPrefix": "<url-id>",
    #             "external_interfaces": {
    #                 "method": "POST",
    #                 "path": "/my/path",
    #                 "protocol": "HTTP/1.1",
    #                 "sourceIp": "123.123.123.123",
    #                 "userAgent": "agent"
    #             },
    #             "requestId": "id",
    #             "routeKey": "$default",
    #             "stage": "$default",
    #             "time": "12/Mar/2020:19:03:58 +0000",
    #             "timeEpoch": 1583348638390
    #         },
    #         "body": "Hello from client!",
    #         "pathParameters": None,
    #         "isBase64Encoded": None,
    #         "stageVariables": None
    #     }
    #
    #     response = lambda_handler(event, None)
    #     assert response["statusCode"] == 400
    #
    # def test_update_with_same_email(self):
    #     repo_mock = UserRepositoryMock()
    #     first_user = repo_mock.users_list[0]
    #
    #     event = {
    #         "version": "2.0",
    #         "routeKey": "$default",
    #         "rawPath": "/my/path",
    #         "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
    #         "cookies": [
    #             "cookie1",
    #             "cookie2"
    #         ],
    #         "headers": {
    #             "header1": "value1",
    #             "header2": "value1,value2"
    #         },
    #         "requestContext": {
    #             "accountId": "123456789012",
    #             "apiId": "<urlid>",
    #             "authentication": None,
    #             "authorizer": {
    #                 "claims":
    #                     {
    #                         "sub": first_user.user_id,
    #                         "name": "Meu novo nome",
    #                         "email": first_user.email,
    #                         "custom:isMaua": True
    #                     }
    #             },
    #             "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
    #             "domainPrefix": "<url-id>",
    #             "external_interfaces": {
    #                 "method": "POST",
    #                 "path": "/my/path",
    #                 "protocol": "HTTP/1.1",
    #                 "sourceIp": "123.123.123.123",
    #                 "userAgent": "agent"
    #             },
    #             "requestId": "id",
    #             "routeKey": "$default",
    #             "stage": "$default",
    #             "time": "12/Mar/2020:19:03:58 +0000",
    #             "timeEpoch": 1583348638390
    #         },
    #         "body": "Hello from client!",
    #         "pathParameters": None,
    #         "isBase64Encoded": None,
    #         "stageVariables": None
    #     }
    #
    #     response = lambda_handler(event, None)
    #     assert response["statusCode"] == 400

