from .manage_connection_controller import ManageConnectionController
from .manage_connection_usecase import ManageConnectionUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_order = Environments.get_order_repo()()
repo_user = Environments.get_user_repo()()
usecase = ManageConnectionUsecase(repo_order, repo_user)
controller = ManageConnectionController(usecase=usecase)


def lambda_handler(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    httpRequest.data['route_key'] = event.get('requestContext', {}).get('routeKey', "$default")
    httpRequest.data['api_id'] = event.get('requestContext', {}).get('apiId', "")
    httpRequest.data['connection_id'] = event.get('requestContext', {}).get('connectionId', "")
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()