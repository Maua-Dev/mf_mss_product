import pytest

from src.shared.helpers.errors.usecase_errors import UserNotAllowed
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.modules.create_product.app.create_product_usecase import CreateProductUsecase
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.domain.enums.role_enum import ROLE

class Test_CreateProductUsecase:
    def test_create_product_usecase(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_prod, repo_user)
    
        
        user = repo_user.users_list[0]
        user.role = ROLE.OWNER

        product = usecase(available=True, price=14.0, name='Lanche Mortadela', description='Mortadela', prepare_time=20, meal_type=MEAL_TYPE.SANDWICHES, photo='https://avatars.githubusercontent.com/u/30812461?v=4', restaurant=RESTAURANT.SOUZA_DE_ABREU, user_id=user.user_id)
        
        assert repo_prod.products[-1].available == product.available
        assert repo_prod.products[-1].price == product.price
        assert repo_prod.products[-1].name == product.name
        assert repo_prod.products[-1].description == product.description
        assert repo_prod.products[-1].prepare_time== product.prepare_time
        assert repo_prod.products[-1].meal_type == product.meal_type
        assert repo_prod.products[-1].photo == product.photo
        assert repo_prod.products[-1].restaurant == product.restaurant
        assert repo_user.users_list[0].user_id == user.user_id

    def test_create_product_usecase_user_role_not_allowed(self):
        repo_prod = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateProductUsecase(repo_prod, repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.USER

        with pytest.raises(UserNotAllowed):
            product = usecase(available=True, price=14.0, name='Lanche Mortadela', description='Mortadela', prepare_time=20, meal_type=MEAL_TYPE.SANDWICHES, photo='https://avatars.githubusercontent.com/u/30812461?v=4', restaurant=RESTAURANT.SOUZA_DE_ABREU, user_id=user.user_id)