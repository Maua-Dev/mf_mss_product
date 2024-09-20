from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .request_upload_product_photo_usecase import RequestUploadProductPhotoUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UserNotAllowed
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, Forbidden, HttpResponse, InternalServerError, NotFound
from src.shared.helpers.external_interfaces.http_models import HttpRequest

class RequestUploadProductPhotoController:
    def __init__(self, usecase: RequestUploadProductPhotoUsecase):
        self.requestUploadProductUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:

            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.body.get('product_id') is None:
                raise MissingParameters('product_id')

            presigned_post = self.requestUploadProductUsecase(product_id=request.body.get('product_id'), user_id=requester_user.user_id)

            message = {"message": f"Photo uploaded successufully."}

            presigned_post.update(message)

            response = OK(presigned_post) 
            
            return response

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except UserNotAllowed as err:
            return Forbidden(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except ForbiddenAction as err:
            return Forbidden(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
        
        