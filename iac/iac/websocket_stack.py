import os
from aws_cdk import (
    aws_lambda as lambda_,
    Duration,
)
from constructs import Construct

from aws_cdk.aws_apigatewayv2_alpha import WebSocketApi, WebSocketStage, WebSocketRouteOptions
from aws_cdk.aws_lambda import LayerVersion
from aws_cdk.aws_apigatewayv2_integrations_alpha import WebSocketLambdaIntegration
from aws_cdk.aws_apigatewayv2_authorizers_alpha import WebSocketLambdaAuthorizer


class WebSocketStack(Construct):

    def __init__(self, scope: Construct, construct_id: str, lambda_layer: LayerVersion, environment_variables: dict) -> None:
        super().__init__(scope, construct_id)
        self.github_ref_name = os.environ.get("GITHUB_REF_NAME")
        self.aws_region = os.environ.get("AWS_REGION")
        self.stage = 'prod'
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

        auth_lambda = lambda_.Function(
            self, "AuthFunction",
            code=lambda_.Code.from_asset(
                f"../lambda_functions/websocket_auth"),
            handler=f"websocket_auth.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[lambda_layer],
            memory_size=512,
            environment=environment_variables,
            timeout=Duration.seconds(15),
        )

        # authorizer = authorizer = WebSocketLambdaAuthorizer("Authorizer", auth_lambda)

        self.manage_connection_function_integration = WebSocketLambdaIntegration(
            id="ManageConnectionFunctionIntegration",
            handler=manage_connection_function
        )

        self.web_socket = WebSocketApi(
            self, f"MauaFood_WebSocketApi_{self.github_ref_name}",
            api_name=f"MauaFood_WebSocketApi_{self.github_ref_name}",
            description="This is the MauaFood WebSocketApi",
            connect_route_options=WebSocketRouteOptions(
                integration=self.manage_connection_function_integration,
                # authorizer=authorizer,
            ),
            disconnect_route_options=WebSocketRouteOptions(
                integration=self.manage_connection_function_integration,
            )
        )

        self.web_socket_stage = WebSocketStage(
            self, f"MauaFood_WebSocketStage_{self.stage}",
            web_socket_api=self.web_socket,
            stage_name=self.stage,
            auto_deploy=True,
        )
