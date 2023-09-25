import json

from src.modules.change_order_by_id.app.change_order_by_id_presenter import lambda_handler
from src.modules.change_order_by_id.app.change_order_by_id_usecase import ChangeOrderByIdUsecase
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.status_enum import STATUS
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from tests.shared.helpers.get_event_for_presenter_tests import get_event_for_presenter_sockets_tests


def get_usecase_order_repo_and_user_repo(order_belongs_to_user: bool = True, is_user_admin: bool = False):
    order_repo = OrderRepositoryMock()
    user_repo = UserRepositoryMock()
    usecase = ChangeOrderByIdUsecase(repo_order=order_repo, repo_user=user_repo)

    user = user_repo.users_list[0]
    order = order_repo.orders[0]
    order.status = STATUS.PENDING

    if is_user_admin:
        user.role = ROLE.ADMIN
    else:
        user.role = ROLE.USER

    if order_belongs_to_user:
        order.user_id = user.user_id
    else:
        order.user_id = user_repo.users_list[-2]

    return usecase, order, user

class Test_ChangeOrderByIdPresenter:
    def test_change_order_observation(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo()

        event = get_event_for_presenter_sockets_tests(
            claims={
                "sub": user.user_id,
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            },
            body={
                "order_id": order.order_id,
                "new_observation": "Espero que tenha uma ótima noite de terça-feira - Laura"
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 200
        assert json.loads(response["body"])["message"] == "the order was updated"
        assert json.loads(response["body"])["order"]["observation"] == "Espero que tenha uma ótima noite de terça-feira - Laura"


    def test_change_order_products(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo()

        event = get_event_for_presenter_sockets_tests(
            claims={
                "sub": user.user_id,
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            },
            body={
                "order_id": order.order_id,
                "new_products": []
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 200
        assert json.loads(response["body"])["message"] == "the order was updated"
        assert json.loads(response["body"])["order"]["products"] == []

    def test_order_does_not_exist(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo()

        event = get_event_for_presenter_sockets_tests(
            claims={
                "sub": user.user_id,
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            },
            body={
                "order_id": "um id que não existe",
                "new_products": []
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 404

    def test_user_does_not_exist(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo()

        event = get_event_for_presenter_sockets_tests(
            claims={
                "sub": "um id inexistente",
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            },
            body={
                "order_id": order.order_id,
                "new_products": []
            }
        )

        response = lambda_handler(event, None)

        assert response['statusCode'] == 400
