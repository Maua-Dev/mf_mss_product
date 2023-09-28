
from aws_cdk import (
    aws_lambda as lambda_,
    NestedStack, Duration
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration, CognitoUserPoolsAuthorizer


class LambdaStack(Construct):

    functions_that_need_dynamo_permissions = []
    functions_that_need_dynamo_user_permissions = []

    def create_lambda_api_gateway_integration(self, module_name: str, method: str, api_resource: Resource, environment_variables: dict = {"STAGE": "TEST"}, authorizer = None):
        function = lambda_.Function(
            self, module_name.title(),
            code=lambda_.Code.from_asset(f"../src/modules/{module_name}"),
            handler=f"app.{module_name}_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[self.lambda_layer],
            memory_size=512,
            environment=environment_variables,
            timeout=Duration.seconds(15)
        )
        

        api_resource.add_resource(module_name.replace("_", "-")).add_method(method,
                                                                            integration=LambdaIntegration(
                                                                                function),
                                                                                authorizer=authorizer)

        return function

    def __init__(self, scope: Construct, api_gateway_resource: Resource, environment_variables: dict, authorizer: CognitoUserPoolsAuthorizer) -> None:
        super().__init__(scope, "MauaFood_Lambdas")

        self.lambda_layer = lambda_.LayerVersion(self, "MauaFood_Layer",
                                                 code=lambda_.Code.from_asset("./lambda_layer_out_temp"),
                                                 compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
                                                )

        self.get_all_products_group_by_restaurant_function = self.create_lambda_api_gateway_integration(
            module_name="get_all_products_group_by_restaurant",
            method="GET",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )

        self.delete_product = self.create_lambda_api_gateway_integration(
            module_name="delete_product",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.create_product = self.create_lambda_api_gateway_integration(
            module_name="create_product",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        
        self.get_product = self.create_lambda_api_gateway_integration(
            module_name="get_product",
            method="GET",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )
        
        self.update_product = self.create_lambda_api_gateway_integration(
            module_name="update_product",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
          
        self.create_user = self.create_lambda_api_gateway_integration(
            module_name="create_user",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.update_user = self.create_lambda_api_gateway_integration(
            module_name="update_user",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.get_user = self.create_lambda_api_gateway_integration(
            module_name="get_user",
            method="GET",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.delete_user = self.create_lambda_api_gateway_integration(
            module_name="delete_user",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.request_upload_product_photo = self.create_lambda_api_gateway_integration(
            module_name="request_upload_product_photo",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.get_all_active_orders_by_restaurant = self.create_lambda_api_gateway_integration(
            module_name="get_all_active_orders_by_restaurant",
            method="GET",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        
        self.create_order = self.create_lambda_api_gateway_integration(
            module_name="create_order",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.change_order_status = self.create_lambda_api_gateway_integration(
            module_name="change_order_status",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.get_current_order_state_by_id = self.create_lambda_api_gateway_integration(
            module_name="get_current_order_state_by_id",
            method="GET",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.abort_order = self.create_lambda_api_gateway_integration(
            module_name="abort_order",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )


        self.change_order_by_id = self.create_lambda_api_gateway_integration(
            module_name="change_order_by_id",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer)

        self.get_all_orders_by_user = self.create_lambda_api_gateway_integration(
            module_name="get_all_orders_by_user",
            method="GET",

            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.functions_that_need_dynamo_user_permissions = [
            self.create_user,
            self.update_user,
            self.get_user,
            self.delete_user,
            self.delete_product,
            self.create_product,
            self.update_product,
            self.request_upload_product_photo,
            self.get_all_active_orders_by_restaurant,
            self.create_order,
            self.change_order_status,
            self.abort_order,
            self.change_order_by_id,
            self.get_all_orders_by_user,
            self.get_current_order_state_by_id
        ]

        self.functions_that_need_dynamo_product_permissions = [
            self.get_all_products_group_by_restaurant_function,
            self.delete_product,
            self.create_product,
            self.get_product,
            self.update_product,
            self.request_upload_product_photo,
            self.create_order,
            self.get_current_order_state_by_id,
        ]
        