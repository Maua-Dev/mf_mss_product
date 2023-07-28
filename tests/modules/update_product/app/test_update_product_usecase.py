import pytest
from src.modules.update_product.app.update_product_usecase import UpdateProductUsecase
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UserNotAllowed, UnregisteredUser
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

user_repo = UserRepositoryMock()
user_id = user_repo.users_list[0].user_id


class Test_UpdateProductUsecase:
    def test_update_product_usecase(self):
        repo = ProductRepositoryMock()

        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        product = usecase(user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
                          restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0,
                          new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20,
                          new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo')

        assert repo.products[0].available == product.available
        assert repo.products[0].price == product.price
        assert repo.products[0].name == product.name
        assert repo.products[0].description == product.description
        assert repo.products[0].prepare_time == product.prepare_time
        assert repo.products[0].meal_type == product.meal_type
        assert repo.products[0].photo == product.photo
        assert repo.products[0].last_update == product.last_update

    def test_update_with_a_nonexistent_user(self):
        repo = ProductRepositoryMock()

        with pytest.raises(UnregisteredUser):
            usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)
            product = usecase(user_id="um id que não existe",
                              product_id="8a705b91-c9e9-4353-a755-07f13afafed3", restaurant=RESTAURANT.SOUZA_DE_ABREU,
                              new_available=True, new_price=15.0, new_name='Nome Atualizado',
                              new_description='Descrição Atualizada', new_prepare_time=20,
                              new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo')

    def test_update_without_permission(self):
        repo = ProductRepositoryMock()
        user_without_permission = user_repo.users_list[-1]
        user_without_permission.role = ROLE.USER

        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        with pytest.raises(UserNotAllowed):
            product = usecase(user_id=user_without_permission.user_id,
                              product_id="8a705b91-c9e9-4353-a755-07f13afafed3", restaurant=RESTAURANT.SOUZA_DE_ABREU,
                              new_available=True, new_price=15.0, new_name='Nome Atualizado',
                              new_description='Descrição Atualizada', new_prepare_time=20,
                              new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo')

    def test_update_product_product_id_invalid_length(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        with pytest.raises(EntityError):
            product = usecase(user_id=user_id, product_id="27cb49f5-4313-49a7-9f84",
                              restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0,
                              new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20,
                              new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo')

    def test_update_product_not_found_product_id(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        with pytest.raises(NoItemsFound):
            product = usecase(user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afaf666",
                              restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0,
                              new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20,
                              new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo')

    def test_update_product_product_id_invalid_type(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        with pytest.raises(EntityError):
            product = usecase(user_id=user_id, product_id=123, restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True,
                              new_price=15.0, new_name='Nome Atualizado', new_description='Descrição Atualizada',
                              new_prepare_time=20, new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo')

    def test_update_product_restaurant_invalid_type(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        with pytest.raises(EntityError):
            product = usecase(user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
                              restaurant="RESTAURANT.SOUZA_DE_ABREU", new_available=True, new_price=15.0,
                              new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20,
                              new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo')

    def test_update_product_available_invalid_type(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        with pytest.raises(EntityError):
            product = usecase(user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
                              restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available='True', new_price=15.0,
                              new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20,
                              new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo')

    def test_update_only_name(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        product_old_description = repo.get_product(product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
                                                   restaurant=RESTAURANT.SOUZA_DE_ABREU).description

        product = usecase(
            user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            new_name='Nome Atualizado')

        assert product.name == 'Nome Atualizado'
        assert product.description == product_old_description

    def test_update_product_price_invalid_type(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        with pytest.raises(EntityError):
            product = usecase(user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
                              restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15,
                              new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20,
                              new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo')

    def test_update_only_price(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        product_old_description = repo.get_product(product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
                                                   restaurant=RESTAURANT.SOUZA_DE_ABREU).description

        product = usecase(
            user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            new_price=42.0)

        assert product.price == 42.0
        assert product.description == product_old_description

    def test_update_product_name_invalid_type(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        with pytest.raises(EntityError):
            product = usecase(user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
                              restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0, new_name=27.0,
                              new_description='Descrição Atualizada', new_prepare_time=20,
                              new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo')

    def test_update_product_description_invalid_type(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        with pytest.raises(EntityError):
            product = usecase(user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
                              restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0,
                              new_name='Nome Atualizado', new_description=RESTAURANT.SOUZA_DE_ABREU,
                              new_prepare_time=20, new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo')

    def test_update_only_description(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        product_old_name = repo.get_product(product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
                                            restaurant=RESTAURANT.SOUZA_DE_ABREU).name

        product = usecase(
            user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            new_description="Minha nova descricao")

        assert product.description == 'Minha nova descricao'
        assert product.name == product_old_name

    def test_update_product_prepare_time_invalid_type(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        with pytest.raises(EntityError):
            product = usecase(user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
                              restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0,
                              new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20.2,
                              new_meal_type=MEAL_TYPE.DRINKS, new_photo='new_photo')

    def test_update_only_prepare_time(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        product_old_name = repo.get_product(product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
                                            restaurant=RESTAURANT.SOUZA_DE_ABREU).name

        product = usecase(
            user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            new_prepare_time=90)

        assert product.prepare_time == 90
        assert product.name == product_old_name

    def test_update_only_prepare_time_with_none_value(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        product_old_name = repo.get_product(product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
                                            restaurant=RESTAURANT.SOUZA_DE_ABREU).name

        product = usecase(
            user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            new_prepare_time=None)

        assert product.prepare_time is None
        assert product.name == product_old_name

    def test_update_name_and_price(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        product_old_description = repo.get_product(product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
                                                   restaurant=RESTAURANT.SOUZA_DE_ABREU).description

        product = usecase(
            user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            new_price=420.0,
            new_name="Novo nome"
        )

        assert product.name == 'Novo nome'
        assert product.price == 420.0
        assert product.description == product_old_description

    def test_update_product_meal_type_invalid_type(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        with pytest.raises(EntityError):
            product = usecase(user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
                              restaurant=RESTAURANT.SOUZA_DE_ABREU, new_available=True, new_price=15.0,
                              new_name='Nome Atualizado', new_description='Descrição Atualizada', new_prepare_time=20,
                              new_meal_type="MEAL_TYPE.DRINKS", new_photo='new_photo')

    def test_update_product_photo_invalid_type(self):
        repo = ProductRepositoryMock()
        usecase = UpdateProductUsecase(repo_prod=repo, repo_user=user_repo)

        with pytest.raises(EntityError):
            product = usecase(user_id=user_id, product_id="8a705b91-c9e9-4353-a755-07f13afafed3",
                              restaurant=RESTAURANT.SOUZA_DE_ABREU,
                              new_available=True, new_price=15.0,
                              new_name='Nome Atualizado',
                              new_description='Descrição Atualizada',
                              new_prepare_time=20,
                              new_meal_type=MEAL_TYPE.DRINKS,
                              new_photo=1678744638
                              )
