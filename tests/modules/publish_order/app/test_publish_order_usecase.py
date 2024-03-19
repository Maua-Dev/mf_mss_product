import pytest

from src.modules.publish_order.app.publish_order_usecase import PublishOrderUsecase
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock


class Test_PublishOrderUsecase:

    def test_publish_order(self):
        repo_mock = OrderRepositoryMock()
        usecase = PublishOrderUsecase(repo_mock)
        first_order = repo_mock.orders[0]

        publish_order = usecase(order=first_order)

        assert publish_order
