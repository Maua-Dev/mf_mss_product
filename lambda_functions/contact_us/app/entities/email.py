import os
from typing import Tuple, Any, Dict
from datetime import datetime

import boto3


class Email:
    email_address: str
    subject: str
    message: str
    user_registered_email: str
    requested_email: str

    def __init__(self, subject: str = None, message: str = None, user_name: str = None,
                 user_email: str = None) -> None:

        self.subject = subject
        self.message = message
        self.date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.body = f"""
        <!DOCTYPE html>
        <html lang="pt-br" charset="UTF-8">
        <head>
        </head>
        <body style="margin: 0; padding: 0; display: flex; align-items: center; justify-content: center; min-height: 100vh; background-color: white; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">
        <table class="main" style="width: 50vw; max-width: 600px; background-color: white; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.25); overflow: hidden;">
            <tr>
            <td>
                <table class="TittleBox" style="width: 100%; background-color: #726057; border-radius: 10px 10px 0 0;">
                <tr>
                    <td style="text-align: center; padding: 20px;">
                    <img alt="MauaFood Logo" src="https://dygzp3rn48wd5.cloudfront.net/logos/images/brown_logo.png" />
                    <h1 style="color: #F3B986; margin-top: 10px;"><strong>Feedback Enviado!</strong></h1>
                    </td>
                </tr>
                </table>
                <table class="ContentBox" style="width: 100%; background-color: #f5e7db;">
                <tr>
                    <td style="text-align: center; padding: 20px;">
                    <div class="TextsBox" style="word-wrap: break-word;">
                        <h2 style="color: #72310E;">Obrigado, {user_name}<p>Seu feedback foi enviado para nossa equipe analisar:</p></h2>
                        <h4 style="color: #726057;">{self.message}</h4>
                        <h4 style="color: #726057;">{self.date_time}</h4>
                    </div>
                    </td>
                </tr>
                </table>
                <table class="BottomBox" style="width: 100%; background-color: #f5e7db; border-top: 1px solid #726057; border-radius: 0 0 10px 10px;">
                <tr>
                    <td style="text-align: center; padding: 20px;">
                    <div class="TextsBox" style="color: #72310E; word-wrap: break-word;">
                        <h2>Atenciosamente,</h2>
                        <h2><strong>Equipe MauaFood</strong>&#127839;</h2>
                    </div>
                    </td>
                </tr>
                </table>
            </td>
            </tr>
        </table>
        </body>
        </html>
        """
        self.to_address = user_email