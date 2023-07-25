from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .delete_product_controller import DeleteProductController
from .delete_product_usecase import DeleteProductUsecase

repo_product = Environments.get_product_repo()()
repo_user = Environments.get_user_repo()()
usecase = DeleteProductUsecase(repo_product,repo_user)
controller = DeleteProductController(usecase=usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()