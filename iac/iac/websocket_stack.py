import os
from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    Duration,
    aws_cognito
)
from constructs import Construct

from aws_cdk.aws_apigatewayv2_alpha import WebSocketApi, WebSocketRouteOptions
from aws_cdk.aws_lambda import LayerVersion
from aws_cdk.aws_apigatewayv2_integrations_alpha import WebSocketLambdaIntegration

class WebSocketStack(Construct):

    def __init__(self, scope: Construct, construct_id: str, lambda_layer: LayerVersion, environment_variables: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.github_ref_name = os.environ.get("GITHUB_REF_NAME")
        self.aws_region = os.environ.get("AWS_REGION")
        self.dev_auth_system_userpool_arn = os.environ.get(
           "AUTH_DEV_SYSTEM_USERPOOL_ARN_DEV")

        manage_connection_function = lambda_.Function(
           self, "ManageConnectionFunction",
           code=lambda_.Code.from_asset(f"../src/modules/manage_connection"),
           handler=f"app.manage_connection_presenter.lambda_handler",
           runtime=lambda_.Runtime.PYTHON_3_9,
           layers=[lambda_layer],
           memory_size=512,
           environment=environment_variables,
           timeout=Duration.seconds(15),
        )

        self.manage_connection_function_integration = WebSocketLambdaIntegration(
            id="ManageConnectionFunctionIntegration",
            handler=manage_connection_function,
        )

        self.web_socket = WebSocketApi(
           self, f"MauaFood_WebSocketApi_{self.github_ref_name}",
           api_name=f"MauaFood_WebSocketApi_{self.github_ref_name}",
           description="This is the MauaFood WebSocketApi",
           connect_route_options=WebSocketRouteOptions(
               integration=self.manage_connection_function_integration,
               route_key="$connect",
           ),
           disconnect_route_options=WebSocketRouteOptions(
               integration=self.manage_connection_function_integration,
               route_key="$disconnect",
           )
        )
