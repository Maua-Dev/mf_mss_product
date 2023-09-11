from src.modules.get_current_order_state_by_id.app.get_current_order_state_by_id_controller import \
    GetCurrentOrderStateByIdController
from src.modules.get_current_order_state_by_id.app.get_current_order_state_by_id_usecase import \
    GetCurrentOrderStateByIdUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_order = Environments.get_order_repo()()
repo_product = Environments.get_product_repo()()
repo_user = Environments.get_user_repo()()
usecase = GetCurrentOrderStateByIdUsecase(order_repo=repo_order, user_repo=repo_user)
controller = GetCurrentOrderStateByIdController(usecase=usecase)

def lambda_handler(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
