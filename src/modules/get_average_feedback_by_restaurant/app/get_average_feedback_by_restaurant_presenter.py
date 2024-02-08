from src.shared.environments import Environments
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from .get_average_feedback_by_restaurant_usecase import GetAverageFeedbackByRestaurantUsecase
from .get_average_feedback_by_restaurant_controller import GetAverageFeedbackByRestaurantController
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_order = Environments.get_order_repo()()
repo_user = Environments.get_user_repo()()
usecase = GetAverageFeedbackByRestaurantUsecase(repo_order, repo_user)
controller = GetAverageFeedbackByRestaurantController(usecase=usecase)


def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
