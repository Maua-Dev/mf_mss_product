from src.shared.environments import Environments
from .get_all_schedules_by_restaurant_usecase import GetAllSchedulesByRestaurantUsecase
from .get_all_schedules_by_restaurant_controller import GetAllSchedulesByRestaurantController
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_order = Environments.get_order_repo()()
repo_user = Environments.get_user_repo()()
usecase = GetAllSchedulesByRestaurantUsecase(repo_order, repo_user)
controller = GetAllSchedulesByRestaurantController(usecase=usecase)


def lambda_handler(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()