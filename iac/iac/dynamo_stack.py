import os


from aws_cdk import (
    CfnOutput,
    aws_dynamodb,
    RemovalPolicy
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration

class DynamoStack(Construct):

        def __init__(self, scope: Construct) -> None:
            super().__init__(scope, "MauaFood_Dynamo")

            self.github_ref_name = os.environ.get("GITHUB_REF_NAME")

            REMOVAL_POLICY = RemovalPolicy.RETAIN if 'prod' in self.github_ref_name else RemovalPolicy.DESTROY

            self.dynamo_table_product = aws_dynamodb.Table(
                self, "MauaFood_Product_Table",
                partition_key=aws_dynamodb.Attribute(
                    name="PK",
                    type=aws_dynamodb.AttributeType.STRING
                ),
                point_in_time_recovery=True,
                sort_key=aws_dynamodb.Attribute(
                    name="SK",
                    type=aws_dynamodb.AttributeType.STRING
                ),
                billing_mode=aws_dynamodb.BillingMode.PAY_PER_REQUEST,
                removal_policy=REMOVAL_POLICY,
                stream=aws_dynamodb.StreamViewType.NEW_IMAGE
            )

            self.dynamo_table_product.add_global_secondary_index(
                partition_key=aws_dynamodb.Attribute(
                    name="GSI1-PK",
                    type=aws_dynamodb.AttributeType.STRING
                ),
                sort_key=aws_dynamodb.Attribute(
                    name="GSI1-SK",
                    type=aws_dynamodb.AttributeType.STRING
                ),
                index_name="GSI1"
            )

            self.dynamo_table_user = aws_dynamodb.Table(
                self, "MauaFood_User_Table",
                partition_key=aws_dynamodb.Attribute(
                    name="PK",
                    type=aws_dynamodb.AttributeType.STRING
                ),
                point_in_time_recovery=True,
                billing_mode=aws_dynamodb.BillingMode.PAY_PER_REQUEST,
                removal_policy=REMOVAL_POLICY
            )

            CfnOutput(self, 'DynamoProductRemovalPolicy',
                        value=REMOVAL_POLICY.value,
                        export_name=f'MauaFood{self.github_ref_name}DynamoProductRemovalPolicyValue')
            
            CfnOutput(self, 'DynamoUserRemovalPolicy',
                        value=REMOVAL_POLICY.value,
                        export_name=f'MauaFood{self.github_ref_name}DynamoUserRemovalPolicyValue')

