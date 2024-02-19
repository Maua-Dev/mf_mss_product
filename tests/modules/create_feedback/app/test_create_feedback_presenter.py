import json
from src.modules.create_feedback.app.create_feedback_presenter import lambda_handler
from src.shared.domain.entities.feedback import Feedback
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from tests.shared.helpers.get_event_for_presenter_tests import get_event_for_test_presenter_no_socket


class Test_CreateFeedbackPresenter:
    def test_create_feedback_presenter(self):
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
                    "order_id":"d78a47cb-80db-4661-b810-8e7c9419d61b",
                    "restaurant": "HORA_H",
                    "value": 4
            },
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 201
        assert json.loads(response["body"])["message"] == "the feedback was created"
        assert json.loads(response["body"])["feedback"]["order_id"] == "d78a47cb-80db-4661-b810-8e7c9419d61b"
        assert json.loads(response["body"])["feedback"]["restaurant"] == "HORA_H"
        assert json.loads(response["body"])["feedback"]["value"] == 4

    def test_create_feedback_presenter_value_is_missing(self):
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
                    "order_id":"d78a47cb-80db-4661-b810-8e7c9419d61b",
                    "restaurant": "HORA_H"
            },
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert json.loads(response["body"]) == "Field value is missing"
        assert response["statusCode"] == 400

    def test_create_feedback_presenter_value_less_than_minimum(self):
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
                    "order_id":"d78a47cb-80db-4661-b810-8e7c9419d61b",
                    "restaurant": "HORA_H",
                    "value": 0
            },
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert json.loads(response["body"]) == "value can't be less than one"
        assert response["statusCode"] == 400
        
    def test_create_feedback_presenter_value_more_than_maximum(self):
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
                    "order_id":"d78a47cb-80db-4661-b810-8e7c9419d61b",
                    "restaurant": "HORA_H",
                    "value": 100
            },
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert json.loads(response["body"]) == "value can't be more than five"
        assert response["statusCode"] == 400