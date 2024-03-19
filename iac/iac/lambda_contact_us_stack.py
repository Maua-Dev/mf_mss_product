import os

from aws_cdk import (
    aws_lambda as lambda_,
    NestedStack, Duration, aws_iam
)
from aws_cdk.aws_apigateway import Resource, CognitoUserPoolsAuthorizer, LambdaIntegration
from aws_cdk.aws_lambda import LayerVersion

from constructs import Construct


class LambdaContactUsStack(Construct):
    def __init__(self, scope: Construct, api_gateway_resource: Resource, authorizer: CognitoUserPoolsAuthorizer,
                 lambda_layer: LayerVersion = None, stage: str = None) -> None:
        super().__init__(scope, "MauaFood_LambdaContactUs")

        module_name = "contact_us"

        environment_variables = {
            "FROM_EMAIL": os.environ.get("FROM_EMAIL"),
            "REPLY_TO_EMAIL": os.environ.get("REPLY_TO_EMAIL"),
            "HIDDEN_COPY": os.environ.get("HIDDEN_COPY"),
            "STAGE": stage
        }

        function = lambda_.Function(
            self, module_name,
            code=lambda_.Code.from_asset(f"../lambda_functions/contact_us"),
            handler=f"app.send_email_feedback_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[lambda_layer],
            memory_size=512,
            environment=environment_variables,
            timeout=Duration.seconds(15),
        )
        
        api_gateway_with_module = api_gateway_resource.add_resource(module_name.replace("_", "-"))

        api_gateway_with_module.add_method("POST", integration=LambdaIntegration(function),authorizer=authorizer)

        api_gateway_resource.add_resource("public").add_resource(module_name.replace("_", "-")).add_method("POST",
                                                                                                           integration=LambdaIntegration(
                                                                                                               function))
        ses_admin_policy = aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=[
                "ses:*",
            ],
            resources=[
                "*"
            ]
        )
        function.add_to_role_policy(ses_admin_policy)

