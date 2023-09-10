import os
from aws_cdk import (
    Stack,
    aws_cognito
)
from constructs import Construct

from .bucket_stack import BucketStack
from .dynamo_stack import DynamoStack

from .lambda_stack import LambdaStack
from aws_cdk.aws_apigatewayv2_integrations_alpha import WebSocketLambdaIntegration

class WebSocketStack(Stack):
    lambda_stack: LambdaStack

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.github_ref_name = os.environ.get("GITHUB_REF_NAME")
        self.aws_region = os.environ.get("AWS_REGION")
        self.s3_assets_cdn = os.environ.get("S3_ASSETS_CDN")
        self.dev_auth_system_userpool_arn = os.environ.get("AUTH_DEV_SYSTEM_USERPOOL_ARN_DEV")

        self.dynamo_stack = DynamoStack(self)

        self.websocket_api = WebSocketLambdaIntegration(self, api_name=f"MauaFood_WebSocketApi_{self.github_ref_name}",
                                                        connect_route_options=[],
                                                        disconnect_route_options=[],
                                                        default_route_options=[],
                                                        route_selection_expression=[],)