from .entities.email import Email
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


def send_email(event, context):
    http_request = LambdaHttpRequest(data=event)
    user = http_request.data.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    email = Email(message=user.message, user_registered_email=user.email,
                  requested_email=http_request.data.get("email")).send(user=user)
    http_response = LambdaHttpResponse(status_code=email.status_code, body=email)

    return http_response.toDict()


def lambda_handler(event, context):
    response = send_email(event, context)

    return response
