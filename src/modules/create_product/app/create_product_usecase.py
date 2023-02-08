import datetime
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.domain.entities.product import Product
from src.shared.helpers.errors.domain_errors import EntityError


class CreateProductUsecase:
    def __init__(self, repo: IProductRepository):
        self.repo = repo

    def __call__(self, available: bool, price: float, name:str, description: str, meal_type: MEAL_TYPE, photo: str, restaurant: RESTAURANT, prepareTime: int) -> Product:

        product_id = len(self.repo.get_all_products_by_restaurant(restaurant=restaurant)) 

        product = Product(available=available, price=price, name=name, description=description, meal_type=meal_type, photo=photo, product_id=product_id, last_update=int(datetime.datetime.now().timestamp()*1000), restaurant=restaurant, prepareTime=prepareTime)

        return self.repo.create_product(product)