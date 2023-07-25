from .update_product_controller import UpdateProductController
from .update_product_usecase import UpdateProductUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_product = Environments.get_product_repo()()
repo_user = Environments.get_user_repo()()
usecase = UpdateProductUsecase(repo_product,repo_user)
controller = UpdateProductController(usecase=usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()