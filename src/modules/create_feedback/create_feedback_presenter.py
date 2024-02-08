from src.shared.environments import Environments
from .create_feedback_controller import CreateFeedbackController
from .create_feedback_usecase import CreateFeedbackUsecase
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_feedback = Environments.get_order_repo()()
repo_user = Environments.get_user_repo()()
usecase = CreateFeedbackUsecase(repo_feedback, repo_user)
controller = CreateFeedbackController(usecase=usecase)

def lambda_handler(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()