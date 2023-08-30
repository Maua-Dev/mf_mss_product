import os
from datetime import datetime
import boto3

from .entities.email import Email
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


def send_email(event, context):
    http_request = LambdaHttpRequest(data=event)
    user = http_request.data.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    user_email = http_request.data.get("email") if user is None else user.get("email")

    print(f"User: {user}")
    print(f"User_email {user_email}")

    print(f"Event {event}")

    if user_email is None:
        return LambdaHttpResponse(status_code=400, body="Email não informado").toDict()

    message = http_request.data.get("message")
    if message is None:
        return LambdaHttpResponse(status_code=400, body="Mensagem não informada").toDict()

    subject = "MauaFood - Contato"
    client = boto3.client('ses', region_name=os.environ.get("AWS_REGION"))

    email = Email(subject=subject, message=message, user_email=user_email)

    try:
        client.send_email(
            Destination={
                'ToAddresses': [
                    user_email,
                ],
                'BccAddresses':
                    [
                        os.environ.get("HIDDEN_COPY")
                    ]
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': email.body,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': email.subject,
                },
            },
            ReplyToAddresses=[
                os.environ.get("REPLY_TO_EMAIL"),
            ],
            Source=os.environ.get("FROM_EMAIL")
        )
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        status_code = 200
        response = f"Email enviado com sucesso para {user_email} em {date_time}"
    except Exception as e:
        status_code = 500
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        response = f"Erro ao enviar email para {user_email} em {date_time} - {e}"

    http_response = LambdaHttpResponse(status_code=status_code, body=response)

    return http_response.toDict()


def lambda_handler(event, context):
    response = send_email(event, context)

    return response
