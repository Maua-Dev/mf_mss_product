import json

from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.modules.get_average_feedback_by_restaurant.app.get_average_feedback_by_restaurant_presenter import lambda_handler


class TestGetAverageFeedbackByRestaurantPresenter:
    def test_lambda_handler(self):
        repo_user = UserRepositoryMock()
        user = repo_user.users_list[2]

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
            "body": 'Visualize all the active orders',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert response['statusCode'] == 200
        assert json.loads(response['body'])["average_feedback"] == 3.0
