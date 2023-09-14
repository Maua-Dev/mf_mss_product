import pytest

from src.modules.abort_order.app.abort_order_usecase import AbortOrderUsecase
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.usecase_errors import UserNotOrderOwner, NoItemsFound, UnregisteredUser, OrderAlreadyPreparing
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

def create_test_user(repo_user):
    return repo_user.create_user(User(
        name="Fernandão",
        email="fernandao@outlook.com",
        role=ROLE.USER,
        user_id="d05bbfae-c06b-4d99-ac03-28945e6c30f3"
    ))

class Test_AbortOrderUseCase:
    def test_abort_order_by_admin(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        last_update_before = repo_order.orders[-3].last_status_update_milliseconds

        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)

        user = create_test_user(repo_user)
        user.role = ROLE.ADMIN

        response: Order = usecase(
            order_id=repo_order.orders[-3].order_id,
            user_id=user.user_id,
            new_aborted_reason="Minha aula já está prestes a começar! :( ",
        )

        assert type(response) == Order
        assert response.aborted_reason == "Minha aula já está prestes a começar! :( "
        assert response.last_status_update_milliseconds > response.creation_time_milliseconds

    def test_abort_order_by_owner(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        last_update_before = repo_order.orders[-3].last_status_update_milliseconds

        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)

        user = repo_user.users_list[-1]
        user.role = ROLE.OWNER

        response: Order = usecase(
            order_id=repo_order.orders[-3].order_id,
            user_id=user.user_id,
            new_aborted_reason="Minha aula já está prestes a começar! :( ",
        )

        assert type(response) == Order
        assert response.aborted_reason == "Minha aula já está prestes a começar! :( "
        assert response.last_status_update_milliseconds > response.creation_time_milliseconds

    def test_abort_order_by_seller(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        last_update_before = repo_order.orders[-3].last_status_update_milliseconds

        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)

        user = repo_user.users_list[-1]
        user.role = ROLE.SELLER

        response: Order = usecase(
            order_id=repo_order.orders[-3].order_id,
            user_id=user.user_id,
            new_aborted_reason="Minha aula já está prestes a começar! :( ",
        )

        assert type(response) == Order
        assert response.aborted_reason == "Minha aula já está prestes a começar! :( "
        assert response.last_status_update_milliseconds > response.creation_time_milliseconds

    def test_abort_order_by_user(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        last_update_before = repo_order.orders[-3].last_status_update_milliseconds

        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)

        user = repo_user.users_list[-1]
        user.role = ROLE.USER

        response: Order = usecase(
            order_id=repo_order.orders[-3].order_id,
            user_id=user.user_id,
            new_aborted_reason="Minha aula já está prestes a começar! :( ",
        )

        assert type(response) == Order
        assert response.aborted_reason == "Minha aula já está prestes a começar! :( "
        assert response.last_status_update_milliseconds > response.creation_time_milliseconds

    def test_user_not_order_owner(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)

        user = create_test_user(repo_user)

        with pytest.raises(UserNotOrderOwner):
            response: Order = usecase(
                order_id=repo_order.orders[-3].order_id,
                user_id=user.user_id,
                new_aborted_reason=repo_order.orders[-3].aborted_reason,
            )

    def test_abort_order_with_invalid_order_id(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)

        user = create_test_user(repo_user)

        with pytest.raises(NoItemsFound):
            response: Order = usecase(
                order_id="invalid_order_id",
                user_id=user.user_id,
                new_aborted_reason=repo_order.orders[-2].aborted_reason,
            )

    def test_abort_order_with_invalid_user_id(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)

        with pytest.raises(UnregisteredUser):
            response: Order = usecase(
                order_id=repo_order.orders[-2].order_id,
                user_id="invalid_user_id",
                new_aborted_reason=repo_order.orders[-2].aborted_reason,
            )

    def test_abort_order_already_preparing_not_admin(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)

        with pytest.raises(OrderAlreadyPreparing):
            response: Order = usecase(
                order_id=repo_order.orders[-2].order_id,
                user_id=repo_order.orders[-2].user_id,
                new_aborted_reason=repo_order.orders[-2].aborted_reason,
            )

    def test_abort_order_already_preparing_admin(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()

        usecase = AbortOrderUsecase(repo_order=repo_order, repo_user=repo_user)

        user = create_test_user(repo_user)
        user.role = ROLE.ADMIN

        response: Order = usecase(
            order_id=repo_order.orders[-2].order_id,
            user_id=user.user_id,
            new_aborted_reason=repo_order.orders[-2].aborted_reason,
        )

        assert type(response) == Order
        assert response.aborted_reason == repo_order.orders[-2].aborted_reason
        assert response.last_status_update_milliseconds > response.creation_time_milliseconds






