import datetime
from typing import List

from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.entities.product import Product
from src.shared.helpers.errors.domain_errors import EntityError

class CreateProductUsecase:
    def __init__(self, repo: IProductRepository):
        self.repo = repo

    def __call__(self, available: bool, price: float, name:str, description: str, meal_type: MEAL_TYPE, photo: str, product_id: int, last_update: int, restaurant: RESTAURANT, prepareTime: int) -> Product:
        
        if type(available)!= bool:
            raise EntityError ("available")

        if type(price)!= float:
            raise EntityError ("price")

        if type(name)!= str:
            raise EntityError ("name")

        if type(description)!= str:
            raise EntityError ("description")

        if type(meal_type)!= MEAL_TYPE:
            raise EntityError ("meal_type")

        if type(photo)!= str:
            raise EntityError ("photo")

        if type(product_id)!= int:
            raise EntityError ("product_id")

        if type(last_update)!= int:
            raise EntityError ("last_update")   

        if type(restaurant)!= RESTAURANT:
            raise EntityError ("restaurant")

        if type(prepareTime)!= int:
            raise EntityError ("prepareTime")

        product_id = len(self.repo.get_all_products_by_restaurant(restaurant=restaurant)) 

        product = Product(available=available, price=price, name=name, description=description, meal_type=meal_type, photo=photo, product_id=product_id, last_update=int(datetime.datetime.now().timestamp()*1000), restaurant=restaurant, prepareTime=prepareTime)

        return self.repo.create_product(product)