import datetime
import pytest
from src.modules.update_product.app.update_product_usecase import UpdateProductUsecase
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateProductUsecase:
    def test_update_product_usecase(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod,repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.OWNER

        product = usecase(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0, new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20, new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo', user_id=user.user_id)

        assert repo_prod.products[0].available == product.available
        assert repo_prod.products[0].price == product.price
        assert repo_prod.products[0].name == product.name
        assert repo_prod.products[0].description == product.description
        assert repo_prod.products[0].prepare_time == product.prepare_time
        assert repo_prod.products[0].meal_type == product.meal_type
        assert repo_prod.products[0].photo == product.photo
        assert repo_prod.products[0].last_update == product.last_update
        assert repo_user.users_list[0].user_id == user.user_id

    def test_update_product_product_id_invalid_length(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod,repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.OWNER

        with pytest.raises(EntityError):
            product = usecase(product_id="27cb49f5-4313-49a7-9f84", restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0, new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20, new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo', user_id=user.user_id)

    def test_update_product_not_found_product_id(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod,repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.OWNER

        with pytest.raises(NoItemsFound):
            product = usecase(product_id="8a705b91-c9e9-4353-a755-07f13afaf666", restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0, new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20, new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo', user_id=user.user_id)

    def test_update_product_product_id_invalid_type(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod,repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.OWNER

        with pytest.raises(EntityError):
            product = usecase(product_id=123, restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0, new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20, new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo', user_id=user.user_id)

    def test_update_product_restaurant_invalid_type(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod,repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.OWNER

        with pytest.raises(EntityError):
            product = usecase(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", restaurant="RESTAURANT.SOUZA_DE_ABREU", new_available=True, new_price=15.0, new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20, new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo', user_id=user.user_id)

    def test_update_product_available_invalid_type(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod,repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.OWNER

        with pytest.raises(EntityError):
            product = usecase(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available='True', new_price=15.0, new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20, new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo', user_id=user.user_id)

    def test_update_product_price_invalid_type(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod,repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.OWNER

        with pytest.raises(EntityError):
            product = usecase(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15, new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20, new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo', user_id=user.user_id)

    def test_update_product_name_invalid_type(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod,repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.OWNER

        with pytest.raises(EntityError):
            product = usecase(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0, new_name=27.0, new_description='Descrição Atualizada', new_prepare_time=20, new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo', user_id=user.user_id)

    def test_update_product_description_invalid_type(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod,repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.OWNER

        with pytest.raises(EntityError):
            product = usecase(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0, new_name='Nome Atualizado', new_description=RESTAURANT.SOUZA_DE_ABREU, new_prepare_time=20, new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo', user_id=user.user_id)

    def test_update_product_prepare_time_invalid_type(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod,repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.OWNER

        with pytest.raises(EntityError):
            product = usecase(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0, new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20.2, new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo', user_id=user.user_id)

    def test_update_product_meal_type_invalid_type(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod,repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.OWNER

        with pytest.raises(EntityError):
            product = usecase(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0, new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20, new_meal_type="MEAL_TYPE.DRINKS", new_photo='new_photo', user_id=user.user_id)

    def test_update_product_photo_invalid_type(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod,repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.OWNER

        with pytest.raises(EntityError):
            product = usecase(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0, new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20, new_meal_type=MEAL_TYPE.DRINKS, new_photo=1678744638, user_id=user.user_id)