import pytest

from src.modules.change_order_status.app.change_order_status_usecase import ChangeOrderStatusUsecase
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.user import User
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.status_enum import STATUS
from src.shared.helpers.errors.usecase_errors import UserNotAllowed
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


def create_test_user(repo_user):
    return repo_user.create_user(User(
        name="Lucas Santinhos",
        email="lucas@gmail.com",
        restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
        role=ROLE.OWNER,
        user_id="93bc6ada-c0d1-7054-66ab-e17414c48af5"
    ))


class Test_ChangeOrderStatusUsecase:
    def test_change_order_status_to_refused_by_admin(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        repo_order.orders[0].status = STATUS.READY

        usecase = ChangeOrderStatusUsecase(repo_order=repo_order, repo_user=repo_user)

        user = create_test_user(repo_user)
        user.role = ROLE.ADMIN

        response: Order = usecase(
            order_id=repo_order.orders[0].order_id,
            user_id=user.user_id,
            new_status=STATUS.REFUSED
        )

        assert type(response) == Order
        assert response.status == STATUS.REFUSED

    def test_change_order_status_to_refused_by_owner_of_restaurante(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        user = create_test_user(repo_user)

        usecase = ChangeOrderStatusUsecase(repo_order=repo_order, repo_user=repo_user)

        order = repo_order.orders[0]
        order.restaurant = RESTAURANT.CANTINA_DO_MOLEZA

        response: Order = usecase(
            order_id=order.order_id,
            user_id=user.user_id,
            new_status=STATUS.REFUSED
        )

        assert type(response) == Order
        assert response.status == STATUS.REFUSED
        assert response.restaurant == user.restaurant

    def test_change_order_status_to_refused_by_seller_of_restaurante(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        repo_order.orders[0].status = STATUS.READY

        usecase = ChangeOrderStatusUsecase(repo_order=repo_order, repo_user=repo_user)

        user = create_test_user(repo_user)
        user.role = ROLE.SELLER

        order = repo_order.orders[0]
        order.restaurant = RESTAURANT.CANTINA_DO_MOLEZA

        response: Order = usecase(
            order_id=order.order_id,
            user_id=user.user_id,
            new_status=STATUS.REFUSED
        )

        assert type(response) == Order
        assert response.status == STATUS.REFUSED
        assert response.restaurant == user.restaurant

    def test_user_role_cant_update_order_status(self):
        with pytest.raises(UserNotAllowed):
            repo_order = OrderRepositoryMock()
            repo_user = UserRepositoryMock()
            repo_order.orders[0].status = STATUS.READY

            usecase = ChangeOrderStatusUsecase(repo_order=repo_order, repo_user=repo_user)

            user = repo_user.users_list[-1]
            user.role = ROLE.USER
            response: Order = usecase(
                order_id=repo_order.orders[0].order_id,
                user_id=user.user_id,
                new_status=STATUS.REFUSED
            )
