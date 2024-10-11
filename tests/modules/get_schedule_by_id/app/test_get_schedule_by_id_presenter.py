import json

from src.modules.get_schedule_by_id.app.get_schedule_by_id_presenter import lambda_handler
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from tests.shared.helpers.get_event_for_presenter_tests import get_event_for_presenter_sockets_tests


class Test_GetScheduleByIdPresenter:
    def test_get_schedule(self):
        repo = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        schedule = repo.schedules[0]
        user = repo_user.users_list[0]

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
          },
          "requestContext": {
            "accountId": "123456789012",
            "apiId": "<urlid>",
            "authentication": None,
            "authorizer": {
                "claims": {
                "sub": user.user_id,
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            }
            },
            "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
            "domainPrefix": "<url-id>",
            "http": {
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
                "schedule_id": schedule.schedule_id
            },
          "pathParameters": None,
          "isBase64Encoded": None,
          "stageVariables": None
        }
        
        response = lambda_handler(event, None)

        expected_body = {'schedule':{
            "schedule_id": schedule.schedule_id,
            "initial_time": schedule.initial_time.strftime("%H:%M"),
            "end_time": schedule.end_time.strftime("%H:%M"),
            "restaurant": schedule.restaurant.value,
            "accepted_reservation":schedule.accepted_reservation},
            'message': 'the schedule object was retrieved'
        }

        assert json.loads(response["body"]) == expected_body
        assert response["statusCode"] == 200


    def test_user_not_registered(self):
        repo = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        schedule = repo.schedules[0]
        user = repo_user.users_list[0]

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
          },
          "requestContext": {
            "accountId": "123456789012",
            "apiId": "<urlid>",
            "authentication": None,
            "authorizer": {
                "claims": {
                "sub": "123456789",
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            }
            },
            "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
            "domainPrefix": "<url-id>",
            "http": {
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
                "schedule_id": schedule.schedule_id
            },
          "pathParameters": None,
          "isBase64Encoded": None,
          "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 404

    def test_nonexistent_schedule(self):
        repo = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        schedule = repo.schedules[0]
        user = repo_user.users_list[0]

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
          },
          "requestContext": {
            "accountId": "123456789012",
            "apiId": "<urlid>",
            "authentication": None,
            "authorizer": {
                "claims": {
                "sub": "123456789",
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            }
            },
            "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
            "domainPrefix": "<url-id>",
            "http": {
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
                "schedule_id": "123456789"
            },
          "pathParameters": None,
          "isBase64Encoded": None,
          "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 404
