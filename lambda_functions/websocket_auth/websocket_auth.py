def lambda_handler(event, context):
    
    #1 - Log the event
    print('*********** The event is: ***************')
    print(event)
    
    #2 - See if the person's token is valid
    # if event['authorizationToken'] == 'abc123':
    #     auth = 'Allow'
    # else:
    #     auth = 'Deny'
    
    auth = 'Allow'
    
    #3 - Construct and return the response
    authResponse = { "principalId": "abc123", "policyDocument": { "Version": "2012-10-17", "Statement": [{"Action": "execute-api:Invoke", "Resource": ["arn:aws:execute-api:sa-east-1:264055331071:e2sl8gy0r4/*/*"], "Effect": auth}] }}
    return authResponse