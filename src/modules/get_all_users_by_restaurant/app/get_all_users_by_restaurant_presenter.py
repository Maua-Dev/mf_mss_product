
from src.modules.get_all_users_by_restaurant.app.get_all_users_by_restaurant_controller import GetAllUsersByRestaurantController
from src.modules.get_all_users_by_restaurant.app.get_all_users_by_restaurant_usecase import GetAllUsersByRestaurantUseCase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


repo_user = Environments.get_user_repo()()
repo_order = Environments.get_order_repo()()
usecase = GetAllUsersByRestaurantUseCase(repo_user, repo_order)
controller = GetAllUsersByRestaurantController(usecase=usecase)

def lambda_handler(event, context):
    
        httpRequest = LambdaHttpRequest(data=event)
        httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
        response = controller(httpRequest)
        httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    
        return httpResponse.toDict()
