import datetime
from src.shared.domain.entities.product import Product
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UserNotAllowed


class UpdateProductUsecase:
    def __init__(self, repo_product: IProductRepository, repo_user: IUserRepository):
        self.repo_product = repo_product
        self.repo_user = repo_user

    def __call__(self, product_id: str, restaurant: RESTAURANT, user_id: str, new_available: bool = None, new_price: float = None, new_name: str = None, new_description: str = None, new_prepare_time: int = None, new_meal_type: MEAL_TYPE = None, new_photo: str = None, new_last_update: int = None) -> Product:
        user = self.repo_user.get_user_by_id(user_id)

        if user.role not in [ROLE.OWNER, ROLE.ADMIN, ROLE.SELLER]:
            raise UserNotAllowed()
        
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
        
        if type(restaurant) != RESTAURANT:
            raise EntityError("restaurant")
        
        if not Product.validate_product_id(product_id=product_id):
            raise EntityError("product_id")
        
        product = self.repo_product.update_product(product_id=product_id, restaurant=restaurant,new_available=new_available, new_price=new_price, new_name=new_name, new_description=new_description, new_prepare_time=new_prepare_time, new_meal_type=new_meal_type, new_photo=new_photo, new_last_update=int(datetime.datetime.now().timestamp()))

        if product == None:
            raise NoItemsFound("product_id and restaurant")

        return product