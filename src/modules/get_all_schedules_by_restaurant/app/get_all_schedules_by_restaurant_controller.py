from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.modules.get_all_schedules_by_restaurant.app.get_all_schedules_by_restaurant_usecase import GetAllSchedulesByRestaurantUseCase
from src.modules.get_all_schedules_by_restaurant.app.get_all_schedules_by_restaurant_viewmodel import GetAllSchedulesViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.enums.restaurant_enum import RESTAURANT

class GetAllSchedulesByRestaurantController:
    def __init__(self, usecase: GetAllSchedulesByRestaurantUseCase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            # Verificar se o user_id foi passado nos headers
            user_id = request.headers.get('user_id', None)
            if not user_id:
                return BadRequest(body="Field user_id is missing")

            # Verificar se o restaurante foi passado no request
            if request.data.get('restaurant') is None:
                raise MissingParameters('restaurant')

            # Validar o restaurante recebido
            try:
                restaurant = RESTAURANT[request.data.get('restaurant')]
            except KeyError:
                raise WrongTypeParameter("restaurant")

            # Executa o usecase usando o user_id e o restaurante como parâmetros
            schedules = self.usecase(user_id=user_id, restaurant=restaurant)

            # Converte o resultado em um ViewModel e retorna a resposta de sucesso
            viewmodel = GetAllSchedulesViewmodel(schedules)
            return OK(viewmodel.to_dict())

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except Exception as err:
            return InternalServerError(body=str(err))