# from src.shared.infra.repositories.order_repository_dynamo import OrderRepositoryDynamo
# from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock


# class Test_OrderRepositoryDynamo:

#     # @pytest.mark.skip("Can't test dynamo in Github")
#     def test_create_order(self):
#         repo_dynamo = OrderRepositoryDynamo()
#         repo_mock = OrderRepositoryMock()

#         order = repo_mock.orders[0]

#         new_order = repo_dynamo.create_order(new_order=order)

#         assert new_order == repo_mock.orders[0]