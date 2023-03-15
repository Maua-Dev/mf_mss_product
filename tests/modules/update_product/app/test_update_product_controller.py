import datetime
from src.modules.update_product.app.update_product_controller import UpdateProductController
from src.modules.update_product.app.update_product_usecase import UpdateProductUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_UpdateProductController:
    def test_update_product_controller(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo=repo)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
            'product_id':'8a705b91-c9e9-4353-a755-07f13afafed3',
            'restaurant':'SOUZA_DE_ABREU',
            'new_available':True,
            'new_price':15.0,
            'new_name':'Nome Atualizado',
            'new_description':'Descrição Atualizada',
            'new_prepare_time':20,
            'new_meal_type':'DRINKS',
            'new_photo':'new_photo',
            }
        )

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body["product"]["available"] == True
        assert response.body["product"]["price"] == 15.0
        assert response.body["product"]["name"] == "Nome Atualizado"
        assert response.body["product"]["description"] == "Descrição Atualizada"
        assert response.body["product"]["prepare_time"] == 20
        assert response.body["product"]["meal_type"] == "DRINKS"
        assert response.body["product"]["photo"] == "new_photo"
        assert response.body["product"]["last_update"] == int(datetime.datetime.now().timestamp()*1000)
        assert response.body["message"] == "the product was updated"

    def test_update_product_controller_product_id_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo=repo)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
            'restaurant':'SOUZA_DE_ABREU',
            'new_available':True,
            'new_price':15.0,
            'new_name':'Nome Atualizado',
            'new_description':'Descrição Atualizada',
            'new_prepare_time':20,
            'new_meal_type':'DRINKS',
            'new_photo':'new_photo'
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field product_id is missing"

    def test_update_product_controller_restaurant_is_missing(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo=repo)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
            'product_id':'8a705b91-c9e9-4353-a755-07f13afafed3',
            'new_available':True,
            'new_price':15.0,
            'new_name':'Nome Atualizado',
            'new_description':'Descrição Atualizada',
            'new_prepare_time':20,
            'new_meal_type':'DRINKS',
            'new_photo':'new_photo'
            }
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field restaurant is missing"

    def test_update_product_controller_restaurant_not_valid(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo=repo)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
            'product_id':'8a705b91-c9e9-4353-a755-07f13afafed3',
            'restaurant':'Souzinha',
            'new_available':True,
            'new_price':15.0,
            'new_name':'Nome Atualizado',
            'new_description':'Descrição Atualizada',
            'new_prepare_time':20,
            'new_meal_type':'DRINKS',
            'new_photo':'new_photo'
            }
        )

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == "No items found for restaurant"

    def test_update_product_controller_meal_type_not_valid(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo=repo)
        controller = UpdateProductController(usecase=usecase)

        request = HttpRequest(
            body={
            'product_id':'8a705b91-c9e9-4353-a755-07f13afafed3',
            'restaurant':'SOUZA_DE_ABREU',
            'new_available':True,
            'new_price':15.0,
            'new_name':'Nome Atualizado',
            'new_description':'Descrição Atualizada',
            'new_prepare_time':20,
            'new_meal_type':'SARGADIN',
            'new_photo':'new_photo'
            }
        )

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == "No items found for new_meal_type"