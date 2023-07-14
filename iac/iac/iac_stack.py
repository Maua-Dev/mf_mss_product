import os
from aws_cdk import (
    Stack,
    aws_cognito
)
from constructs import Construct
from .dynamo_stack import DynamoStack

from .lambda_stack import LambdaStack
from aws_cdk.aws_apigateway import RestApi, Cors, CognitoUserPoolsAuthorizer


class IacStack(Stack):
    lambda_stack: LambdaStack

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.github_ref_name = os.environ.get("GITHUB_REF_NAME")
        self.aws_region = os.environ.get("AWS_REGION")
        self.s3_assets_cdn = os.environ.get("S3_ASSETS_CDN")
        self.dev_auth_system_userpool_arn = os.environ.get("AUTH_DEV_SYSTEM_USERPOOL_ARN_DEV")

        # self.dynamo_stack = DynamoStack(self)
        
        self.rest_api = RestApi(self, f"MauaFood_RestApi_{self.github_ref_name}",
                                rest_api_name=f"MauaFood_RestApi_{self.github_ref_name}",
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
        if 'prod' in self.github_ref_name:
            stage = 'PROD'

        elif 'homolog' in self.github_ref_name:
            stage = 'HOMOLOG'

        else:
            stage = 'DEV'

        ENVIRONMENT_VARIABLES = {
            "STAGE": stage,
            "S3_ASSETS_CDN": self.s3_assets_cdn,
            # "DYNAMO_TABLE_NAME": self.dynamo_stack.dynamo_table.table_name,
            # "DYNAMO_PARTITION_KEY": self.dynamo_stack.partition_key_name,
            # "DYNAMO_SORT_KEY": self.dynamo_stack.sort_key_name,
        }

        

        self.cognito_auth = CognitoUserPoolsAuthorizer(self, f"mf_cognito_auth_{self.github_ref_name}",
                                                     cognito_user_pools=[aws_cognito.UserPool.from_user_pool_arn(
                                                            self, f"mf_cognito_auth_userpool_{self.github_ref_name}",
                                                            self.dev_auth_system_userpool_arn
                                                     )]
                                                     )

        self.lambda_stack = LambdaStack(self, api_gateway_resource=api_gateway_resource,
                                        environment_variables=ENVIRONMENT_VARIABLES, authorizer=self.cognito_auth)

        # for f in self.lambda_stack.functions_that_need_dynamo_permissions:
        #     self.dynamo_stack.dynamo_table.grant_read_write_data(f)