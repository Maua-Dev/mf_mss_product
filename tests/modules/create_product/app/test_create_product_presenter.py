import json
from src.modules.create_product.app.create_product_presenter import lambda_handler

class Test_CreateProductPresenter:
    def test_create_product_presenter(self):

        event = {'version': '2.0', 'routeKey': '$default', 'rawPath': '/my/path', 'rawQueryString': 'parameter1=value1&parameter1=value2&parameter2=value', 'cookies': ['cookie1', 'cookie2'], 'headers': {'header1': 'value1', 'header2': 'value1,value2'}, 'queryStringParameters': {'parameter1': '1'}, 'requestContext': {'accountId': '123456789012', 'apiId': '<urlid>', 'authentication': None, 'authorizer': {'iam': {'accessKey': 'AKIA...', 'accountId': '111122223333', 'callerId': 'AIDA...', 'cognitoIdentity': None, 'principalOrgId': None, 'userArn': 'arn:aws:iam::111122223333:user/example-user', 'userId': 'AIDA...'}}, 'domainName': '<url-id>.lambda-url.us-west-2.on.aws', 'domainPrefix': '<url-id>', 'external_interfaces': {'method': 'POST', 'path': '/my/path', 'protocol': 'HTTP/1.1', 'sourceIp': '123.123.123.123', 'userAgent': 'agent'}, 'requestId': 'id', 'routeKey': '$default', 'stage': '$default', 'time': '12/Mar/2020:19:03:58 +0000', 'timeEpoch': 1583348638390}, 'body': '{"available": true, "price": 16.0, "name": "Misto", "description": "Mussarela e Presunto", "meal_type": "SANDWICHES", "photo": "https://avatars.githubusercontent.com/u/30812461?v=4", "restaurant": "HORA_H", "prepare_time": 15}', 'pathParameters': None, 'isBase64Encoded': None, 'stageVariables': None}   

        response = lambda_handler(event, None)

        assert json.loads(response["body"])["message"] == "the product was created"
        assert response["statusCode"] == 201
        assert json.loads(response["body"])["product"]["available"] == True
        assert json.loads(response["body"])["product"]["price"] == 16.0
        assert json.loads(response["body"])["product"]["name"] == "Misto"
        assert json.loads(response["body"])["product"]["description"] == "Mussarela e Presunto"
        assert json.loads(response["body"])["product"]["meal_type"] == "SANDWICHES"
        assert json.loads(response["body"])["product"]["photo"] == "https://avatars.githubusercontent.com/u/30812461?v=4"
        assert json.loads(response["body"])["product"]["restaurant"] == "HORA_H"
        assert json.loads(response["body"])["product"]["prepare_time"] == 15

    def test_create_product_presenter_price_is_missing(self):

        event = {'version': '2.0', 'routeKey': '$default', 'rawPath': '/my/path', 'rawQueryString': 'parameter1=value1&parameter1=value2&parameter2=value', 'cookies': ['cookie1', 'cookie2'], 'headers': {'header1': 'value1', 'header2': 'value1,value2'}, 'queryStringParameters': {'parameter1': '1'}, 'requestContext': {'accountId': '123456789012', 'apiId': '<urlid>', 'authentication': None, 'authorizer': {'iam': {'accessKey': 'AKIA...', 'accountId': '111122223333', 'callerId': 'AIDA...', 'cognitoIdentity': None, 'principalOrgId': None, 'userArn': 'arn:aws:iam::111122223333:user/example-user', 'userId': 'AIDA...'}}, 'domainName': '<url-id>.lambda-url.us-west-2.on.aws', 'domainPrefix': '<url-id>', 'external_interfaces': {'method': 'POST', 'path': '/my/path', 'protocol': 'HTTP/1.1', 'sourceIp': '123.123.123.123', 'userAgent': 'agent'}, 'requestId': 'id', 'routeKey': '$default', 'stage': '$default', 'time': '12/Mar/2020:19:03:58 +0000', 'timeEpoch': 1583348638390}, 'body': '{"available": true, "name": "Misto", "description": "Mussarela e Presunto", "meal_type": "SANDWICHES", "photo": "https://avatars.githubusercontent.com/u/30812461?v=4", "restaurant": "HORA_H", "prepare_time": 15}', 'pathParameters': None, 'isBase64Encoded': None, 'stageVariables': None}   
        response = lambda_handler(event, None)

        assert json.loads(response["body"]) == "Field price is missing"
        assert response["statusCode"] == 400


    def test_create_product_presenter_invalid_name(self):

        event = {'version': '2.0', 'routeKey': '$default', 'rawPath': '/my/path', 'rawQueryString': 'parameter1=value1&parameter1=value2&parameter2=value', 'cookies': ['cookie1', 'cookie2'], 'headers': {'header1': 'value1', 'header2': 'value1,value2'}, 'queryStringParameters': {'parameter1': '1'}, 'requestContext': {'accountId': '123456789012', 'apiId': '<urlid>', 'authentication': None, 'authorizer': {'iam': {'accessKey': 'AKIA...', 'accountId': '111122223333', 'callerId': 'AIDA...', 'cognitoIdentity': None, 'principalOrgId': None, 'userArn': 'arn:aws:iam::111122223333:user/example-user', 'userId': 'AIDA...'}}, 'domainName': '<url-id>.lambda-url.us-west-2.on.aws', 'domainPrefix': '<url-id>', 'external_interfaces': {'method': 'POST', 'path': '/my/path', 'protocol': 'HTTP/1.1', 'sourceIp': '123.123.123.123', 'userAgent': 'agent'}, 'requestId': 'id', 'routeKey': '$default', 'stage': '$default', 'time': '12/Mar/2020:19:03:58 +0000', 'timeEpoch': 1583348638390}, 'body': '{"available": true, "price": 16.0, "name": 3, "description": "Mussarela e Presunto", "meal_type": "SANDWICHES", "photo": "https://avatars.githubusercontent.com/u/30812461?v=4", "restaurant": "HORA_H", "prepare_time": 15}', 'pathParameters': None, 'isBase64Encoded': None, 'stageVariables': None}

        response = lambda_handler(event, None)

        assert json.loads(response["body"]) == "Field name is not valid"
        assert response["statusCode"] == 400  
        