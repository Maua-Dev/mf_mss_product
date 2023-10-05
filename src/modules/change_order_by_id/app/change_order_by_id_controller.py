from .change_order_by_id_usecase import ChangeOrderByIdUsecase
from .change_order_by_id_viewmodel import ChangeOrderByIdViewmodel
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityParameterError, \
    EntityError
from src.shared.helpers.errors.usecase_errors import UserNotAllowed, NoItemsFound, \
    UnregisteredUser, UserNotOrderOwner, OrderCantBeUpdated, ProducutsListCantBeEmpty
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, Forbidden, NotFound, InternalServerError
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class ChangeOrderByIdController:
    def __init__(self, usecase: ChangeOrderByIdUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get("order_id") is None:
                raise MissingParameters("order_id")

            order_id = request.data.get("order_id")

            products_list = request.data.get("new_products")

            new_products_list = []

            if products_list is not None:

                for product in products_list:
                    prod_name = product.get("product_name")
                    prod_id = product.get("product_id")
                    quantity = product.get("quantity")

                    new_products_list.append(OrderProduct(
                        product_name=prod_name,
                        product_id=prod_id,
                        quantity=quantity
                    ))

            order = self.usecase(
                order_id=order_id,
                user_id=requester_user.user_id,
                new_prods_list=new_products_list if products_list is not None else None
            )
            viewmodel = ChangeOrderByIdViewmodel(order)

            return OK(viewmodel.to_dict())

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except UserNotAllowed as err:
            return Forbidden(body=err.message)

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except UserNotOrderOwner as err:
            return Forbidden(body=err.message)

        except OrderCantBeUpdated as err:
            return Forbidden(body=err.message)

        except ProducutsListCantBeEmpty as err:
            return Forbidden(body=err.message)

        except UnregisteredUser as err:
            return BadRequest(body=err.message)

        except EntityParameterError as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
