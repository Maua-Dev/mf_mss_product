from src.shared.domain.entities.product import Product
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class UpdateProductUsecase:
    def __init__(self, repo: IProductRepository):
        self.repo = repo

    def __call__(self, new_product_id: str, new_restaurant: RESTAURANT, new_available: bool = None, new_price: float = None, new_name: str = None, new_description: str = None, new_prepare_time: int = None, new_meal_type: MEAL_TYPE = None, new_photo: str = None, new_last_update: int = None) -> Product:
        if type(new_available) != bool:
            raise EntityError("new_available")
        
        if type(new_price) != float:
            raise EntityError("new_price")
        
        if type(new_name) != str:
            raise EntityError("new_name")
        
        if type(new_description) != str:
            raise EntityError("new_description")
        
        if type(new_prepare_time) != int:
            raise EntityError("new_prepare_time")
        
        if type(new_meal_type) != MEAL_TYPE:
            raise EntityError("new_meal_type")
        
        if type(new_photo) != str:
            raise EntityError("new_photo")
        
        if type(new_last_update) != int:
            raise EntityError("new_last_update")
        
        if type(new_restaurant) != RESTAURANT:
            raise EntityError("new_restaurant")
        
        if type(new_product_id) != RESTAURANT:
            raise EntityError("new_restaurant")
        
        product = self.repo.update_product(new_available=new_available, new_price=new_price, new_name=new_name, new_description=new_description, new_prepare_time=new_prepare_time, new_meal_type=new_meal_type, new_photo=new_photo, new_last_update=new_last_update, new_restaurant=new_restaurant)

        if product == None:
            raise NoItemsFound("product_id and restaurant")

        return product