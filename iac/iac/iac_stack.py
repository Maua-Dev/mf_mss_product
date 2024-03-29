import os
from aws_cdk import (
    aws_lambda as lambda_,
    Stack,
    aws_cognito,
    Duration
)
from constructs import Construct

from .websocket_stack import WebSocketStack

from .bucket_stack import BucketStack
from .dynamo_stack import DynamoStack

from .lambda_contact_us_stack import LambdaContactUsStack
from .lambda_stack import LambdaStack
from aws_cdk.aws_apigateway import RestApi, Cors, CognitoUserPoolsAuthorizer


class IacStack(Stack):
    lambda_stack: LambdaStack

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.github_ref_name = os.environ.get("GITHUB_REF_NAME")
        self.aws_region = os.environ.get("AWS_REGION")
        self.s3_assets_cdn = os.environ.get("S3_ASSETS_CDN")
        self.dev_auth_system_userpool_arn = os.environ.get(
            "AUTH_DEV_SYSTEM_USERPOOL_ARN_DEV")

        self.dynamo_stack = DynamoStack(self)

        self.rest_api = RestApi(self, f"MauaFood_RestApi_{self.github_ref_name}",
                                rest_api_name=f"MauaFood_RestApi_{self.github_ref_name}",
                                description="This is the MauaFood RestApi",
                                default_cors_preflight_options={
                                    "allow_origins": Cors.ALL_ORIGINS,
                                    "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                                    "allow_headers": ["*"]
                                },
                                )

        api_gateway_resource = self.rest_api.root.add_resource("mss-product", default_cors_preflight_options={
            "allow_origins": Cors.ALL_ORIGINS,
            "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": Cors.DEFAULT_HEADERS
        }
        )
        self.bucket_stack = BucketStack(self)

        if 'prod' in self.github_ref_name:
            stage = 'PROD'

        elif 'homolog' in self.github_ref_name:
            stage = 'HOMOLOG'

        else:
            stage = 'DEV'

        ENVIRONMENT_VARIABLES = {
            "STAGE": stage,
            "S3_ASSETS_CDN": self.s3_assets_cdn,
            "DYNAMO_TABLE_NAME_PRODUCT": self.dynamo_stack.dynamo_table_product.table_name,
            "DYNAMO_TABLE_NAME_USER": self.dynamo_stack.dynamo_table_user.table_name,
            "DYNAMO_PARTITION_KEY": "PK",
            "DYNAMO_SORT_KEY": "SK",
            "DYNAMO_GSI_PARTITION_KEY": "GSI1-PK",
            "DYNAMO_GSI_SORT_KEY": "GSI1-SK",
            "S3_BUCKET_NAME": self.bucket_stack.s3_bucket.bucket_name,
            "CLOUD_FRONT_DISTRIBUTION_DOMAIN_ASSETS": self.bucket_stack.cloudfront_distribution.domain_name,

        }

        self.cognito_auth = CognitoUserPoolsAuthorizer(self, f"mf_cognito_auth_{self.github_ref_name}",
                                                       cognito_user_pools=[aws_cognito.UserPool.from_user_pool_arn(
                                                           self, f"mf_cognito_auth_userpool_{self.github_ref_name}",
                                                           self.dev_auth_system_userpool_arn
                                                       )]
                                                       )



        self.lambda_stack = LambdaStack(self, api_gateway_resource=api_gateway_resource,
                                        environment_variables=ENVIRONMENT_VARIABLES, authorizer=self.cognito_auth)

        self.contact_us_lambda_stack = LambdaContactUsStack(self, api_gateway_resource=api_gateway_resource,
                                                            authorizer=self.cognito_auth,
                                                            lambda_layer=self.lambda_stack.lambda_layer,
                                                            stage=stage)

        self.websocket_stack = WebSocketStack(self, construct_id="MauaFood_WebSocketApi",
                                              lambda_layer=self.lambda_stack.lambda_layer,
                                              environment_variables=ENVIRONMENT_VARIABLES)
        
        ENVIRONMENT_VARIABLES_WITH_WEBSOCKET = ENVIRONMENT_VARIABLES.copy()
        ENVIRONMENT_VARIABLES_WITH_WEBSOCKET["WEBSOCKET_URL"] = self.websocket_stack.web_socket.api_endpoint


        dynamo_event_handler_function = lambda_.Function(
            self, "OrderEventHandlerFunction",
            code=lambda_.Code.from_asset(f"../src/modules/publish_order"),
            handler=f"app.publish_order_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[self.lambda_stack.lambda_layer],
            memory_size=512,
            environment=ENVIRONMENT_VARIABLES_WITH_WEBSOCKET,
            timeout=Duration.seconds(15),
        )

        self.lambda_stack.functions_that_need_dynamo_product_permissions.append(dynamo_event_handler_function)
        
        self.dynamo_stack.dynamo_table_product.grant_stream_read(dynamo_event_handler_function)

        dynamo_event_handler_function.add_event_source_mapping(
            "DynamoEventSourceMapping",
            event_source_arn=self.dynamo_stack.dynamo_table_product.table_stream_arn,
            starting_position=lambda_.StartingPosition.TRIM_HORIZON,
            batch_size=1,
        )

        self.websocket_stack.web_socket.grant_manage_connections(dynamo_event_handler_function)
    
        for f in self.lambda_stack.functions_that_need_dynamo_product_permissions:
            self.dynamo_stack.dynamo_table_product.grant_read_write_data(f)

        for f in self.lambda_stack.functions_that_need_dynamo_user_permissions:
            self.dynamo_stack.dynamo_table_user.grant_read_write_data(f)

        for f in self.websocket_stack.functions_that_need_dynamo_product_permissions:
            self.dynamo_stack.dynamo_table_product.grant_read_write_data(f)

        for f in self.websocket_stack.functions_that_need_dynamo_user_permissions:
            self.dynamo_stack.dynamo_table_user.grant_read_write_data(f)
