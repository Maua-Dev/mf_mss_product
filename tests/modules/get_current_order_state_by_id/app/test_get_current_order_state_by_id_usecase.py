import pytest

from src.modules.get_current_order_state_by_id.app.get_current_order_state_by_id_usecase import \
    GetCurrentOrderStateByIdUsecase
from src.shared.domain.entities.order import Order
from src.shared.domain.enums.status_enum import STATUS
from src.shared.helpers.errors.usecase_errors import UserNotOrderOwner, UnregisteredUser
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


def get_items_for_tests(order_status: STATUS = STATUS.READY):
    user_repo = UserRepositoryMock()
    order_repo = OrderRepositoryMock()
    order_repo.orders[-1].status = order_status
    order_repo.orders[-1].user_id = user_repo.users_list[-1].user_id

    return user_repo, order_repo, order_repo.orders[-1]


class Test_GetCurrentOrderStateByIdUsecase:
    def test_get_current_state(self):
        user_repo, order_repo, order = get_items_for_tests()
        user = user_repo.users_list[-1]
        usecase = GetCurrentOrderStateByIdUsecase(user_repo=user_repo, order_repo=order_repo)

        response = usecase(order_id=order_repo.orders[-1].order_id, user_id=user.user_id)

        assert type(response) == Order
        assert response == order_repo.orders[-1]

    def test_raise_exception_when_user_is_not_owner_of_order(self):
        user_repo, order_repo, order = get_items_for_tests(STATUS.READY)
        user = user_repo.users_list[-2]  # O order pertence ao user de indice -1

        with pytest.raises(UserNotOrderOwner):
            usecase = GetCurrentOrderStateByIdUsecase(user_repo=user_repo, order_repo=order_repo)
            response = usecase(order_id=order_repo.orders[-1].order_id, user_id=user.user_id)

    def test_raise_exception_when_user_doesnt_exist(self):
        user_repo, order_repo, order = get_items_for_tests(STATUS.READY)

        with pytest.raises(UnregisteredUser):
            usecase = GetCurrentOrderStateByIdUsecase(user_repo=user_repo, order_repo=order_repo)
            response = usecase(order_id=order_repo.orders[-1].order_id, user_id="um id que não existe")
