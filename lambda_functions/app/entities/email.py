import os
from typing import Tuple, Any, Dict
from datetime import datetime

import boto3


class Email:
    email_address: str = os.environ.get("FROM_EMAIL")
    subject: str = "MauaFood - Contato"
    message: str
    user_registered_email: str
    requested_email: str

    def __init__(self, sender_email: str = email_address, subject: str = subject, message: str = None,
                 user_registered_email: str = None, requested_email: str = None) -> None:

        self.status_code = None
        self.client = boto3.client('ses', region_name=os.environ.get("AWS_REGION"))
        self.sender_email = sender_email
        self.subject = subject
        self.date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        validation_body = self.validate_message(message)
        if not validation_body[0]:
            raise Exception(validation_body[1])
        self.body = """
                 <!DOCTYPE html>
                <html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
                <head>
                <!--[if gte mso 9]>
                <xml>
                <o:OfficeDocumentSettings>
                <o:AllowPNG/>
                <o:PixelsPerInch>96</o:PixelsPerInch>
                </o:OfficeDocumentSettings>
                </xml><![endif]-->

                <style type="text/css">
                @media only screen and (min-width: 620px) {{ {{
                .u-row {{ {{
                width: 600px !important;
                }}
                }}

                .u-row .u-col {{

                {{
                vertical-align: top
                ;
                }}
                }}

                .u-row .u-col-50 {{

                {{
                width: 300px !important
                ;
                }}
                }}

                .u-row .u-col-100 {{

                {{
                width: 600px !important
                ;
                }}
                }}
                }}
                }}

                @media (max-width: 620px) {{ {{
                .u-row-container {{ {{
                max-width: 100% !important;
                padding-left: 0px !important;
                padding-right: 0px !important;
                }}
                }}

                .u-row .u-col {{

                {{
                min-width: 320px !important
                ;
                max-width: 100% !important
                ;
                display: block !important
                ;
                }}
                }}

                .u-row {{

                {{
                width: 100% !important
                ;
                }}
                }}

                .u-col {{

                {{
                width: 100% !important
                ;
                }}
                }}

                .u-col > div {{

                {{
                margin: 0 auto
                ;
                }}
                }}
                }}
                }}

                body {{

                {{
                margin: 0
                ;
                padding: 0
                ;
                }}
                }}

                table, tr, td {{

                {{
                vertical-align: top
                ;
                border-collapse: collapse
                ;
                }}
                }}

                p {{

                {{
                margin: 0
                ;
                }}
                }}

                .ie-container table, .mso-container table {{

                {{
                table-layout: fixed
                ;
                }}
                }}

                * {{

                {{
                line-height: inherit
                ;
                }}
                }}

                a[x-apple-data-detectors=\'true\'] {{

                {{
                color: inherit !important
                ;
                text-decoration: none !important
                ;
                }}
                }}

                table, td {{

                {{
                color: #000000
                ;
                }}
                }}

                #u_body a {{

                {{
                color: #223166
                ;
                text-decoration: underline
                ;
                }}
                }}

                @media (max-width: 480px) {{ {{
                #u_content_heading_6 .v-container-padding-padding {{ {{
                padding: 20px 10px 40px !important;
                }}
                }}

                #u_content_heading_6 .v-font-size {{

                {{
                font-size: 20px !important
                ;
                }}
                }}

                #u_content_text_deprecated_7 .v-container-padding-padding {{

                {{
                padding: 30px 10px 10px !important
                ;
                }}
                }}

                #u_content_text_deprecated_8 .v-container-padding-padding {{

                {{
                padding: 10px 10px 30px !important
                ;
                }}
                }}

                #u_content_text_deprecated_9 .v-container-padding-padding {{

                {{
                padding: 10px 10px 20px !important
                ;
                }}
                }}
                }}
                }}
                </style>
                <title></title>
                </head>
                <body class="clean-body u_body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #f8f8fc;color: #000000">
                <table id="u_body" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #f8f8fc;width:100%" cellpadding="0" cellspacing="0">
                <tbody>
                <tr style="vertical-align: top">
                <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                <div class="u-row-container" style="padding: 0px;background-color: transparent">
                <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                <div class="u-col u-col-50" style="max-width: 320px;min-width: 300px;display: table-cell;vertical-align: top;">
                <div style="background-color: #223166;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                <div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                <table style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                <tr>
                <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Open Sans',sans-serif;" align="left">
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                <td style="padding-right: 0px;padding-left: 0px;" align="center">
                <a><img align="center" border="0" src="https://d3ebnpochj0915.cloudfront.net/logo-footer-mauafood.png" alt="Logo MauaFood" title="Logo Smile" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 280px;" width="280"></a>
                </td>
                </tr>
                </table>
                </td>
                </tr>
                </tbody>
                </table>
                </div>
                </div>
                </div>
                <div class="u-col u-col-50" style="max-width: 320px;min-width: 300px;display: table-cell;vertical-align: top;">
                <div style="background-color: #223166;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                <div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                <table style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                <tr>
                <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Open Sans',sans-serif;" align="left">
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                <td style="padding-right: 0px;padding-left: 0px;" align="center"><img align="center" border="0" src="https://d3ebnpochj0915.cloudfront.net/logo_maua_branco.png" alt="Logo Maua" title="Logo Maua" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 280px;" width="280"></td>
                </tr>
                </table>
                </td>
                </tr>
                </tbody>
                </table>
                </div>
                </div>
                </div>
                </div>
                </div>
                </div>
                <div class="u-row-container" style="padding: 0px;background-color: transparent">
                <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                <div style="background-color: #223166;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                <div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                <table id="u_content_heading_6" style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                <tr>
                <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:25px 10px 50px;font-family:'Open Sans',sans-serif;" align="left">
                <h1 class="v-font-size" style="margin: 0px; color: #ffffff; line-height: 140%; text-align: center; word-wrap: break-word; font-size: 22px;"><strong>FeedBack Enviado!</strong></h1>
                </td>
                </tr>
                </tbody>
                </table>
                </div>
                </div>
                </div>
                </div>
                </div>
                </div>
                <div class="u-row-container" style="padding: 0px;background-color: transparent">
                <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                <div style="background-color: #ffffff;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                <div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                <table id="u_content_text_deprecated_7" style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                <tr>
                <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:50px 50px 0px;font-family:'Open Sans',sans-serif;" align="left">
                <div class="v-font-size" style="font-size: 15px; line-height: 140%; text-align: justify; word-wrap: break-word;">
                <p style="line-height: 140%;">&nbsp;</p>
                <h2 style="line-height: 140%;">Seu feedback foi enviado para nossa equipe analisar:</h2>
                <h4 style="line-height: 140%;">{message}</h4>
                <p style="line-height: 140%;">&nbsp;</p>
                </div>
                </td>
                </tr>
                </tbody>
                </table>
                <table id="u_content_text_deprecated_8" style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                <tr>
                <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:15px 10px 50px 50px;font-family:'Open Sans',sans-serif;" align="left">
                <div class="v-font-size" style="line-height: 160%; text-align: left; word-wrap: break-word;">
                <h5 style="font-size: 14px; line-height: 160%;">{date_time}</h5>
                <h5 style="font-size: 14px; line-height: 160%;">Atenciosamente,</h5>
                <p style="font-size: 14px; line-height: 160%;"><strong>Equipe MauaFood ;)</strong></p>
                </div>
                </td>
                </tr>
                </tbody>
                </table>
                </div>
                </div>
                </div>
                </div>
                </div>
                </div>
                <div class="u-row-container" style="padding: 0px;background-color: transparent">
                <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                <div style="height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                <div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                <table id="u_content_text_deprecated_9" style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                <tr>
                <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px 100px 20px;font-family:'Open Sans',sans-serif;" align="left">
                <div class="v-font-size" style="line-height: 170%; text-align: center; word-wrap: break-word;">
                <p style="line-height: 170%;">MAUAFOOD</p>
                </div>
                </td>
                </tr>
                </tbody>
                </table>
                <table style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                <tbody>
                <tr>
                <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:0px;font-family:'Open Sans',sans-serif;" align="left">
                <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                <tbody>
                <tr style="vertical-align: top">
                <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%"><span>&nbsp;</span></td>
                </tr>
                </tbody>
                </table>
                </td>
                </tr>
                </tbody>
                </table>
                </div>
                </div>
                </div>
                </div>
                </div>
                </div>
                </td>
                </tr>
                </tbody>
                </table>
                </body>
                </html>
                """.format(message=self.message, date_time=self.date_time)

        if requested_email is None:
            self.to_address = user_registered_email
        else:
            validation_to_address = self.validate_email(requested_email)
            if not validation_to_address[0]:
                raise Exception(validation_to_address[1])
            self.to_address = requested_email

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
    def validate_message(body: str = None) -> Tuple[bool, str or None]:
        if body is None:
            return False, "Body is required"
        if type(body) != str:
            return False, "Body must be a string"
        return True, None

    def send(self, user: Any | None = None) -> Dict[str, Any]:
        try:
            response = self.client.send_email(
                Destination={
                    'ToAddresses': [
                        user.email,
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
                            'Data': self.body,
                        },
                    },
                    'Subject': {
                        'Charset': "UTF-8",
                        'Data': self.subject,
                    },
                },
                ReplyToAddresses=[
                    os.environ.get("REPLY_TO_EMAIL"),
                ],
                Source=os.environ.get("FROM_EMAIL")
            )

            date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            self.status_code = 200
            return {
                "body": {
                    "message": f"Email sent at {date_time}"
                }
            }

        except Exception as e:
            self.status_code = 500
            return {
                "body": e
            }
