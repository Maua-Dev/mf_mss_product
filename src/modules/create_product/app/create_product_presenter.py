from src.shared.environments import Environments
from .create_product_controller import CreateProductController
from .create_product_usecase import CreateProductUsecase
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo = Environments.get_product_repo()()
usecase = CreateProductUsecase(repo=repo)
controller = CreateProductController(usecase=usecase)

def lambda_handler(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()