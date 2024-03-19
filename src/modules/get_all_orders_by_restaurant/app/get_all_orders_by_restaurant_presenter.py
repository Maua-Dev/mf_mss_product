from src.shared.environments import Environments
from .get_all_orders_by_restaurant_usecase import GetAllOrdersByRestaurantUsecase
from .get_all_orders_by_restaurant_controller import GetAllOrdersByRestaurantController
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_order = Environments.get_order_repo()()
repo_user = Environments.get_user_repo()()
usecase = GetAllOrdersByRestaurantUsecase(repo_order, repo_user)
controller = GetAllOrdersByRestaurantController(usecase=usecase)


def lambda_handler(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()