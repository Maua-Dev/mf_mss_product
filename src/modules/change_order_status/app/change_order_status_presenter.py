from .change_order_status_controller import ChangeOrderStatusController
from .change_order_status_usecase import ChangeOrderStatusUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_order = Environments.get_order_repo()()
repo_product = Environments.get_product_repo()()
repo_user = Environments.get_user_repo()()
usecase = ChangeOrderStatusUsecase(repo_order, repo_user)
controller = ChangeOrderStatusController(usecase=usecase)


def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
