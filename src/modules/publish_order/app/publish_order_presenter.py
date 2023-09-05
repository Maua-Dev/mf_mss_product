from src.modules.publish_order.app.publish_order_controller import PublishOrderController
from src.modules.publish_order.app.publish_order_usecase import PublishOrderUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.dynamo_event_parser import DynamoEventParser
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpResponse


repo_order = Environments.get_order_repo()()
usecase = PublishOrderUsecase(repo_order)
controller = PublishOrderController(usecase=usecase)

def lambda_handler(event, context):

    dynamo_event = DynamoEventParser(event)
    response = controller(dynamo_event)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()