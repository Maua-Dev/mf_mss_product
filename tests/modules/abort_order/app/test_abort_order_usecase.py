import pytest

from src.modules.abort_order.app.abort_order_usecase import AbortOrderUsecase
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.user import User
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.usecase_errors import UserNotAllowed, UserNotRelatedToRestaurant
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

def create_test_user(repo_user):
    return repo_user.create_user(User(
        name="Felipe Carillo",
        email="felipecarillo@outlook.com",
        restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
        role=ROLE.OWNER,
        user_id="93bc6ada-c0d1-7054-66ab-e17414c48af5"
    ))

class Test_AbortOrderUseCase:
    def test_abort_order_to_refused_by_admin(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        repo_order.orders[0].aborted_reason = "Desisti da compra!"
        last_update_before = repo_order.orders[0].last_status_update_milliseconds

        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)

        user = create_test_user(repo_user)
        user.role = ROLE.ADMIN

        response: Order = usecase(
            order_id=repo_order.orders[0].order_id,
            user_id=user.user_id,
            new_aborted_reason="Desisti da compra!",
        )

        assert type(response) == Order
        assert response.aborted_reason == "Desisti da compra!"
        assert response.last_status_update_milliseconds > response.creation_time_milliseconds

    def test_abort_order_to_refused_by_owner_of_restaurant(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        user = create_test_user(repo_user)

        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)

        order = repo_order.orders[0]
        order.restaurant = RESTAURANT.CANTINA_DO_MOLEZA

        response: Order = usecase(
            order_id=order.order_id,
            user_id=user.user_id,
            new_aborted_reason="Desisti da compra!",
        )

        assert type(response) == Order
        assert response.aborted_reason == "Desisti da compra!"
        assert response.last_status_update_milliseconds > response.creation_time_milliseconds

    def test_other_owner_cant_change_order_status(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        user = create_test_user(repo_user)
        user.restaurant = RESTAURANT.HORA_H

        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)

        order = repo_order.orders[0]
        order.restaurant = RESTAURANT.CANTINA_DO_MOLEZA

        with pytest.raises(UserNotRelatedToRestaurant):
            response: Order = usecase(
                order_id=order.order_id,
                user_id=user.user_id,
                new_aborted_reason="Desisti da compra!",
            )

    def test_other_seller_cant_change_order_status(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        user = create_test_user(repo_user)
        user.role = ROLE.SELLER
        user.restaurant = RESTAURANT.HORA_H

        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)

        order = repo_order.orders[0]
        order.restaurant = RESTAURANT.CANTINA_DO_MOLEZA

        with pytest.raises(UserNotRelatedToRestaurant):
            response: Order = usecase(
                order_id=order.order_id,
                user_id=user.user_id,
                new_aborted_reason="Desisti da compra!",
            )

    def test_change_order_status_to_refused_by_seller_of_restaurant(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        repo_order.orders[0].aborted_reason = "Desisti da compra!"

        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)

        user = create_test_user(repo_user)
        user.role = ROLE.SELLER

        order = repo_order.orders[0]
        order.restaurant = RESTAURANT.CANTINA_DO_MOLEZA

        response: Order = usecase(
            order_id=order.order_id,
            user_id=user.user_id,
            new_aborted_reason="Desisti da compra!",
        )

        assert type(response) == Order
        assert response.aborted_reason == "Desisti da compra!"
        assert response.restaurant == user.restaurant

    def test_user_role_cant_update_order_status(self):
        with pytest.raises(UserNotAllowed):
            repo_order = OrderRepositoryMock()
            repo_user = UserRepositoryMock()
            repo_order.orders[0].aborted_reason = "Desisti da compra!"

            usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)

            user = repo_user.users_list[-1]
            user.role = ROLE.USER
            response: Order = usecase(
                order_id=repo_order.orders[0].order_id,
                user_id=user.user_id,
                new_aborted_reason="Desisti da compra!"
            )

