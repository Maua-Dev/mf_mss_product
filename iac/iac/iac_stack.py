from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

from .lambda_stack import LambdaStack
from aws_cdk.aws_apigateway import RestApi, Cors


class IacStack(Stack):
    lambda_stack: LambdaStack

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.rest_api = RestApi(self, "MauaFood_RestApi",
                                rest_api_name="MauaFood_RestApi",
                                description="This is the MauaFood RestApi",
                                default_cors_preflight_options=
                                {
                                    "allow_origins": Cors.ALL_ORIGINS,
                                    "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                                    "allow_headers": ["*"]
                                },
                                )

        api_gateway_resource = self.rest_api.root.add_resource("mss-product", default_cors_preflight_options=
        {
            "allow_origins": Cors.ALL_ORIGINS,
            "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": Cors.DEFAULT_HEADERS
        }
                                                                   )

        ENVIRONMENT_VARIABLES = {
            "STAGE": "TEST",
            # "DYNAMO_TABLE_NAME": self.dynamo_stack.dynamo_table.table_name,
            # "DYNAMO_PARTITION_KEY": self.dynamo_stack.partition_key_name,
            # "DYNAMO_SORT_KEY": self.dynamo_stack.sort_key_name,
            "REGION": self.region,
        }

        self.lambda_stack = LambdaStack(self, api_gateway_resource=api_gateway_resource,
                                        environment_variables=ENVIRONMENT_VARIABLES)

