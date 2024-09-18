from src.shared.environments import Environments
from .get_schedule_by_id_controller import GetScheduleByIdController
from .get_schedule_by_id_usecase import GetScheduleByIdUsecase
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

#repo_order = Environments.get_order_repo()()
repo_schedule = Environments.get_order_repo()()
usecase = GetScheduleByIdUsecase(repo_schedule)
controller = GetScheduleByIdController(usecase=usecase)

def lambda_handler(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()