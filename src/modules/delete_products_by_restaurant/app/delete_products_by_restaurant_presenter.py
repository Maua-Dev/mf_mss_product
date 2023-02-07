from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .delete_products_by_restaurant_controller import DeleteProductsByRestaurantController
from .delete_products_by_restaurant_usecase import DeleteProductsByRestaurantUsecase

repo = Environments.get_user_repo()()
usecase = DeleteProductsByRestaurantUsecase(repo=repo)
controller = DeleteProductsByRestaurantController(usecase=usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()