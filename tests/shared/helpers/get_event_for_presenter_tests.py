from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


def get_event_for_test_presenter_no_socket(body: dict, claims: dict = None):
    user_repo = UserRepositoryMock()
    user = user_repo.users_list[1]

    if claims is None:
        claims = {
            "sub": user.user_id,
            "name": user.name,
            "email": user.email,
            "custom:isMaua": True
        }

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
                "claims": claims
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
        "body": body,
        "pathParameters": None,
        "isBase64Encoded": None,
        "stageVariables": None
    }

    return event


def get_event_for_presenter_sockets_tests(body: dict, claims: dict = None):
    user_repo = UserRepositoryMock()
    user = user_repo.users_list[0]

    if claims is None:
        claims = {
            "sub": user.user_id,
            "name": user.name,
            "email": user.email,
            "custom:isMaua": True
        }

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
                    "claims": claims
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
            "body": body,
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
    }

    return event
