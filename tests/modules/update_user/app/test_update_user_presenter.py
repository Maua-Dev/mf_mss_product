from src.modules.update_user.app.update_user_presenter import lambda_handler
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateUserPresenter:

    def test_update_user_presenter(self):
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
                            "name": "Meu novo nome",
                            "email": None,
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
                            "name": "Meu novo nome",
                            "email": None,
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
                            "name": "M",
                            "email": None,
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

    def test_update_with_same_name(self):
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
                            "email": None,
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

