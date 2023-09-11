import json
from src.modules.manage_connection.app.manage_connection_presenter import lambda_handler


class Test_ManageConnectionPresenter:
    def test_create_connection_presenter(self):

        event = {
            'headers':{
                'Host':'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com',
                'x-api-key':'',
                'X-Forwarded-For':'',
                'x-restapi':''
            },
            'multiValueHeaders':{
                'Host':[
                    'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com'
                ],
                'x-api-key':[
                    ''
                ],
                'X-Forwarded-For':[
                    ''
                ],
                'x-restapi':[
                    ''
                ]
            },
            'body':{
                'restaurant': 'HORA_H',
            },
            'requestContext':{
                'routeKey':'$connect',
                'disconnectStatusCode':1005,
                'eventType':'CONNECT',
                'extendedRequestId':'Jx-TaE0_GjQFvSw=',
                'requestTime':'17/Aug/2023:01:26:32 +0000',
                'messageDirection':'IN',
                'disconnectReason':'Client-side close frame status not set',
                'stage':'prod',
                'connectedAt':1692234829479,
                'requestTimeEpoch':1692235592753,
                'identity':{
                    'userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
                    'sourceIp':'177.102.86.227'
                },
                "authorizer": {
                    "claims":
                        {
                            "sub": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                            "name": "Lucas Duez",
                            "email": "lucas.santos@gmail.com",
                            "custom:isMaua": True
                        }
                },
                'requestId':'Jx-TaE0_GjQFvSw=',
                'domainName':'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com',
                'connectionId':'Jx8cJdLcmjQCIIA=',
                'apiId':'e2sl8gy0r4'
            },
            'isBase64Encoded':False
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 200
        assert json.loads(response["body"])["message"] == "the connection status"
        assert json.loads(response["body"])["connection"]["user_id"] == "93bc6ada-c0d1-7054-66ab-e17414c48ae3"
        assert json.loads(response["body"])["connection"]["restaurant"] == 'HORA_H'

    def test_abort_connection_presenter(self):

        event = {
            'headers':{
                'Host':'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com',
                'x-api-key':'',
                'X-Forwarded-For':'',
                'x-restapi':''
            },
            'multiValueHeaders':{
                'Host':[
                    'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com'
                ],
                'x-api-key':[
                    ''
                ],
                'X-Forwarded-For':[
                    ''
                ],
                'x-restapi':[
                    ''
                ]
            },
            'body':{
                'restaurant': 'HORA_H',
            },
            'requestContext':{
                'routeKey':'$disconnect',
                'disconnectStatusCode':1005,
                'eventType':'DISCONNECT',
                'extendedRequestId':'Jx-TaE0_GjQFvSw=',
                'requestTime':'17/Aug/2023:01:26:32 +0000',
                'messageDirection':'IN',
                'disconnectReason':'Client-side close frame status not set',
                'stage':'prod',
                'connectedAt':1692234829479,
                'requestTimeEpoch':1692235592753,
                'identity':{
                    'userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
                    'sourceIp':'177.102.86.227'
                },
                "authorizer": {
                    "claims":
                        {
                            "sub": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                            "name": "Lucas Duez",
                            "email": "lucas.santos@gmail.com",
                            "custom:isMaua": True
                        }
                },
                'requestId':'Jx-TaE0_GjQFvSw=',
                'domainName':'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com',
                'connectionId':'ad2e0f88-2c34-bv',
                'apiId':'e2sl8gy0r4'
            },
            'isBase64Encoded':False
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 200

    def test_manage_connection_presenter_connection_id_none(self):

        event = {
            'headers':{
                'Host':'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com',
                'x-api-key':'',
                'X-Forwarded-For':'',
                'x-restapi':''
            },
            'multiValueHeaders':{
                'Host':[
                    'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com'
                ],
                'x-api-key':[
                    ''
                ],
                'X-Forwarded-For':[
                    ''
                ],
                'x-restapi':[
                    ''
                ]
            },
            'body':{
                'restaurant': 'HORA_H',
            },
            'requestContext':{
                'routeKey':'$connect',
                'disconnectStatusCode':1005,
                'eventType':'CONNECT',
                'extendedRequestId':'Jx-TaE0_GjQFvSw=',
                'requestTime':'17/Aug/2023:01:26:32 +0000',
                'messageDirection':'IN',
                'disconnectReason':'Client-side close frame status not set',
                'stage':'prod',
                'connectedAt':1692234829479,
                'requestTimeEpoch':1692235592753,
                'identity':{
                    'userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
                    'sourceIp':'177.102.86.227'
                },
                "authorizer": {
                    "claims":
                        {
                            "sub": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                            "name": "Lucas Duez",
                            "email": "lucas.santos@gmail.com",
                            "custom:isMaua": True
                        }
                },
                'requestId':'Jx-TaE0_GjQFvSw=',
                'domainName':'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com',
                'apiId':'e2sl8gy0r4'
            },
            'isBase64Encoded':False
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field connection_id is not valid"

    def test_manage_connection_presenter_api_id_none(self):

        event = {
            'headers':{
                'Host':'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com',
                'x-api-key':'',
                'X-Forwarded-For':'',
                'x-restapi':''
            },
            'multiValueHeaders':{
                'Host':[
                    'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com'
                ],
                'x-api-key':[
                    ''
                ],
                'X-Forwarded-For':[
                    ''
                ],
                'x-restapi':[
                    ''
                ]
            },
            'body':{
                'restaurant': 'HORA_H',
            },
            'requestContext':{
                'routeKey':'$connect',
                'disconnectStatusCode':1005,
                'eventType':'CONNECT',
                'extendedRequestId':'Jx-TaE0_GjQFvSw=',
                'requestTime':'17/Aug/2023:01:26:32 +0000',
                'messageDirection':'IN',
                'disconnectReason':'Client-side close frame status not set',
                'stage':'prod',
                'connectedAt':1692234829479,
                'requestTimeEpoch':1692235592753,
                'identity':{
                    'userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
                    'sourceIp':'177.102.86.227'
                },
                "authorizer": {
                    "claims":
                        {
                            "sub": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                            "name": "Lucas Duez",
                            "email": "lucas.santos@gmail.com",
                            "custom:isMaua": True
                        }
                },
                'requestId':'Jx-TaE0_GjQFvSw=',
                'domainName':'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com',
                'connectionId':'Jx8cJdLcmjQCIIA=',
            },
            'isBase64Encoded':False
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field api_id is not valid"

    def test_manage_connection_presenter_restaurant_none(self):

        event = {
            'headers':{
                'Host':'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com',
                'x-api-key':'',
                'X-Forwarded-For':'',
                'x-restapi':''
            },
            'multiValueHeaders':{
                'Host':[
                    'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com'
                ],
                'x-api-key':[
                    ''
                ],
                'X-Forwarded-For':[
                    ''
                ],
                'x-restapi':[
                    ''
                ]
            },
            'body':{

            },
            'requestContext':{
                'routeKey':'$connect',
                'disconnectStatusCode':1005,
                'eventType':'CONNECT',
                'extendedRequestId':'Jx-TaE0_GjQFvSw=',
                'requestTime':'17/Aug/2023:01:26:32 +0000',
                'messageDirection':'IN',
                'disconnectReason':'Client-side close frame status not set',
                'stage':'prod',
                'connectedAt':1692234829479,
                'requestTimeEpoch':1692235592753,
                'identity':{
                    'userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
                    'sourceIp':'177.102.86.227'
                },
                "authorizer": {
                    "claims":
                        {
                            "sub": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                            "name": "Lucas Duez",
                            "email": "lucas.santos@gmail.com",
                            "custom:isMaua": True
                        }
                },
                'requestId':'Jx-TaE0_GjQFvSw=',
                'domainName':'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com',
                'connectionId':'Jx8cJdLcmjQCIIA=',
                'apiId':'e2sl8gy0r4'
            },
            'isBase64Encoded':False
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == 'Field restaurant is missing'

    def test_maange_connection_presenter_restaurant_not_found(self):

        event = {
            'headers':{
                'Host':'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com',
                'x-api-key':'',
                'X-Forwarded-For':'',
                'x-restapi':''
            },
            'multiValueHeaders':{
                'Host':[
                    'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com'
                ],
                'x-api-key':[
                    ''
                ],
                'X-Forwarded-For':[
                    ''
                ],
                'x-restapi':[
                    ''
                ]
            },
            'body':{
                'restaurant': 'Tech Food',
            },
            'requestContext':{
                'routeKey':'$connect',
                'disconnectStatusCode':1005,
                'eventType':'CONNECT',
                'extendedRequestId':'Jx-TaE0_GjQFvSw=',
                'requestTime':'17/Aug/2023:01:26:32 +0000',
                'messageDirection':'IN',
                'disconnectReason':'Client-side close frame status not set',
                'stage':'prod',
                'connectedAt':1692234829479,
                'requestTimeEpoch':1692235592753,
                'identity':{
                    'userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
                    'sourceIp':'177.102.86.227'
                },
                "authorizer": {
                    "claims":
                        {
                            "sub": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                            "name": "Lucas Duez",
                            "email": "lucas.santos@gmail.com",
                            "custom:isMaua": True
                        }
                },
                'requestId':'Jx-TaE0_GjQFvSw=',
                'domainName':'e2sl8gy0r4.execute-api.sa-east-1.amazonaws.com',
                'connectionId':'Jx8cJdLcmjQCIIA=',
                'apiId':'e2sl8gy0r4'
            },
            'isBase64Encoded':False
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == "Field 'Tech Food' is not a restaurant"

    

    

    
        