from src.shared.environments import Environments
from .get_all_product_by_restaurant_controller import GetAllProductByRestaurantController
from .get_all_product_by_restaurant_usecase import GetAllProductsByRestaurantUsecase
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo = Environments.get_user_repo()()
usecase = GetAllProductsByRestaurantUsecase(repo=repo)
controller = GetAllProductByRestaurantController(usecase=usecase)

def lambda_handler(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()