import boto3

client = boto3.client('cognito-idp')


def lambda_handler(event, context):
    token = event['headers']['Authorization']
    methodArn = event['methodArn'].split('/')
    methodArn = methodArn[0] + '/*/*'
    response = client.get_user(
        AccessToken=token
    )
    auth = 'Allow'
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        auth = 'Deny'

    requested_user = {}
    for item in response['UserAttributes']:
        requested_user[item['Name']] = item['Value']
    
    auth_response = {
    "principalId": response['Username'],
    "policyDocument": {
        "Version": "2012-10-17",
        "Statement": [
                {
                "Action": "execute-api:Invoke",
                "Effect": auth,
                "Resource": [methodArn]
                }
            ]
        },
    "context": {
            "sub": requested_user["sub"],
            "name": requested_user["name"],
            "email": requested_user["email"],
            "custom:isMaua": requested_user["custom:isMaua"]
        }
    }


    print(auth_response)



    return auth_response