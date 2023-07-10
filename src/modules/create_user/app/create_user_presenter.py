from .create_user_controller import CreateUserController
from .create_user_usecase import CreateUserUsecase
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.shared.environments import Environments

repo = Environments.get_user_repo()()
usecase = CreateUserUsecase(repo)
controller = CreateUserController(usecase)

def create_user_presenter(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

def lambda_handler(event, context):
    
    response = create_user_presenter(event, context)
   
    return response