from src.shared.environments import Environments
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from .request_upload_product_photo_controller import RequestUploadProductPhotoController
from .request_upload_product_photo_usecase import RequestUploadProductPhotoUsecase
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_product = Environments.get_product_repo()()
repo_user = Environments.get_user_repo()()
usecase = RequestUploadProductPhotoUsecase(repo_product, repo_user)
controller = RequestUploadProductPhotoController(usecase)


def lambda_handler(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()