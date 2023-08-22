import os
from typing import Tuple, Any
from datetime import datetime

import boto3


class Email:
    email_address: str
    subject: str
    body: str
    to_addresses: str

    def __init__(self, sender_email: str = None, subject: str = None, body: str = None, to_address: str = None) -> None:

        self.__client = boto3.client('ses', region_name=os.environ.get("AWS_REGION"))

        validation_sender_email = self.validate_email(sender_email)
        if not validation_sender_email[0]:
            raise Exception(validation_sender_email[1])
        self.sender_email = sender_email

        validation_subject = self.validate_subject(subject)
        if not validation_subject[0]:
            raise Exception(validation_subject[1])
        self.subject = subject

        validation_body = self.validate_body(body)
        if not validation_body[0]:
            raise Exception(validation_body[1])
        self.body = body

        validation_to_addresses = self.validate_email(to_address)
        if not validation_to_addresses[0]:
            raise Exception(validation_to_addresses[1])
        self.to_addresses = to_address

    @staticmethod
    def validate_email(email: str = None) -> Tuple[bool, str or None]:
        if email is None:
            return False, "Email is required"
        if "@" not in email:
            return False, "Email is invalid"
        if type(email) != str:
            return False, "Email must be a string"
        return True, None

    @staticmethod
    def validate_subject(subject: str = None) -> Tuple[bool, str or None]:
        if subject is None:
            return False, "Subject is required"
        if type(subject) != str:
            return False, "Subject must be a string"
        return True, None

    @staticmethod
    def validate_body(body: str = None) -> Tuple[bool, str or None]:
        if body is None:
            return False, "Body is required"
        if type(body) != str:
            return False, "Body must be a string"
        return True, None

    def send_email(self) -> tuple[Any, str]:
        response = self.__client.send_email(
            Source=self.sender_email,
            Destination={
                'ToAddresses': [
                    self.to_addresses
                ]
            },
            Message={
                'Subject': {
                    'Data': self.subject,
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': self.body,
                        'Charset': 'UTF-8'
                    }
                }
            }
        )

        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        return response, date_time
