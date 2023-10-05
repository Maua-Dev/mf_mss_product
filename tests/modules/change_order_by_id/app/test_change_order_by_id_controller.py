from src.modules.change_order_by_id.app.change_order_by_id_controller import ChangeOrderByIdController
from src.modules.change_order_by_id.app.change_order_by_id_usecase import ChangeOrderByIdUsecase
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.status_enum import STATUS
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


def get_usecase_order_repo_and_user_repo(order_belongs_to_user: bool = True, is_user_admin: bool = False):
    order_repo = OrderRepositoryMock()
    user_repo = UserRepositoryMock()
    usecase = ChangeOrderByIdUsecase(repo_order=order_repo, repo_user=user_repo)

    user = user_repo.users_list[-1]
    order = order_repo.orders[-1]
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


class Test_ChangeOrderByIdController:
    def test_update_products_list(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo()
        controller = ChangeOrderByIdController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": user.user_id,
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            },
            "order_id": order.order_id,
            "new_products": [
                {
                    "product_name": "Pamonha",
                    "product_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "quantity": 12}
            ]
        })

        response = controller(request)

        assert response.status_code == 200
        assert response.body["message"] == "the order was updated"

    def test_request_user_is_missing(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo()
        controller = ChangeOrderByIdController(usecase)

        request = HttpRequest(body={
            "order_id": order.order_id,
            "new_products": []
        })

        response = controller(request)

        assert response.status_code == 400

    def test_non_owner_user_cant_change_order(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo(order_belongs_to_user=False, is_user_admin=False)
        controller = ChangeOrderByIdController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": user.user_id,
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            },
            "order_id": order.order_id,
            "new_products": []
        })

        response = controller(request)

        assert response.status_code == 403

    def test_order_does_not_exist(self):
        usecase, order, user = get_usecase_order_repo_and_user_repo(order_belongs_to_user=False, is_user_admin=False)
        controller = ChangeOrderByIdController(usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": user.user_id,
                "name": user.name,
                "email": user.email,
                "custom:isMaua": True
            },
            "order_id": "um id que não existe",
            "new_products": []
        })

        response = controller(request)

        assert response.status_code == 404
