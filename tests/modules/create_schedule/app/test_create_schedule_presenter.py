import pytest
import json

from src.modules.create_schedule.app.create_schedule_presenter import lambda_handler
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_CreateSchedulePresenter:
    def test_create_schedule_presenter(self):
        repo = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        user = repo_user.users_list[3]

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
              "parameter1": "1",
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
                "schedule_id": "e51b48a0-e33c-4ace-98a0-d9af96157dfc",
                "initial_time": "12:00:00",
                "end_time": "14:00:00",
                "restaurant": "SOUZA_DE_ABREU",
                "accepted_reservation": True
            },
          "pathParameters": None,
          "isBase64Encoded": None,
          "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 201
        assert json.loads(response["body"])["message"] == "Schedule created successfully"
        assert json.loads(response["body"])["schedule"]["initial_time"] == "12:00:00"
        assert json.loads(response["body"])["schedule"]["end_time"] == "14:00:00"
        assert json.loads(response["body"])["schedule"]["restaurant"] == "SOUZA_DE_ABREU"
        assert json.loads(response["body"])["schedule"]["accepted_reservation"] == True


