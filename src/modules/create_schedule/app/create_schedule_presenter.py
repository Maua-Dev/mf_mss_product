from src.modules.create_schedule.app.create_schedule_controller import CreateScheduleController
from src.modules.create_schedule.app.create_schedule_usecase import CreateScheduleUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_user = Environments.get_user_repo()()
repo_schedule = Environments.get_order_repo()()
usecase = CreateScheduleUsecase(repo_schedule=repo_schedule, repo_user=repo_user)
controller = CreateScheduleController(usecase)

def create_schedule_presenter(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

def lambda_handler(event, context):
    
    response = create_schedule_presenter(event, context)
   
    return response

