import datetime
import uuid
from src.shared.domain.entities.product import Product
from src.shared.domain.entities.user import User
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import UserNotAllowed

class CreateProductUsecase:
    def __init__(self, repo_product: IProductRepository, repo_user: IUserRepository):
        self.repo_product = repo_product
        self.repo_user = repo_user

    def __call__(self, available: bool, price: float, name:str, description: str, meal_type: MEAL_TYPE, photo: str, restaurant: RESTAURANT, prepare_time: int, product_id: str, user_id: str) -> Product:

        user = self.repo_user.get_user_by_id(user_id)

        if user.role not in [ROLE.OWNER,ROLE.ADMIN]:
            raise UserNotAllowed()

        product_id = str(uuid.uuid4())

        product = Product(available=available, price=price, name=name, description=description, meal_type=meal_type, photo=photo, product_id=product_id, last_update=int(datetime.datetime.now().timestamp()*1000), restaurant=restaurant, prepare_time=prepare_time)

        return self.repo_product.create_product(product)