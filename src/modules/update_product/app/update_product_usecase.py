import datetime
from typing import Optional

from src.shared.domain.entities.product import Product
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterExcededMaximumValue
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UserNotAllowed, UnregisteredUser


class UpdateProductUsecase:
    def __init__(self, repo_prod: IProductRepository, repo_user: IUserRepository):
        self.repo_prod = repo_prod
        self.repo_user = repo_user

    def __call__(self, product_id: str,
                 restaurant: RESTAURANT,
                 user_id: str,
                 new_available: Optional[bool] = None,
                 new_price: Optional[float] = None,
                 new_name: Optional[str] = None,
                 new_description: Optional[str] = '-1',
                 new_prepare_time: Optional[int] = -1,
                 new_meal_type: Optional[MEAL_TYPE] = None,
                 new_photo: Optional[str] = None,
                 new_last_update: Optional[int] = None) -> Product:

        user = self.repo_user.get_user_by_id(user_id)

        if user is None:
            raise UnregisteredUser()

        if user.role not in [ROLE.OWNER, ROLE.ADMIN, ROLE.SELLER]:
            raise UserNotAllowed()

        if type(new_available) != bool and new_available is not None:
            raise EntityError("new_available")

        if type(new_price) != float and new_price is not None:
            raise EntityError("new_price")

        if new_price is not None and new_price > 10000.00:
            raise EntityParameterExcededMaximumValue("price", Product.MAXIMUM_PRICE)

        if type(new_name) != str and new_name is not None:
            raise EntityError("new_name")

        if type(new_description) != str and new_description is not None:
            raise EntityError("new_description")

        if type(new_prepare_time) != int and new_prepare_time is not None:
            raise EntityError("new_prepare_time")

        if type(new_meal_type) != MEAL_TYPE and new_meal_type is not None:
            raise EntityError("new_meal_type")

        if type(new_photo) != str and new_photo is not None:
            raise EntityError("new_photo")

        if type(restaurant) != RESTAURANT and not None:
            raise EntityError("restaurant")

        if not Product.validate_product_id(product_id=product_id):
            raise EntityError("product_id")

        product = self.repo_prod.update_product(product_id=product_id, restaurant=restaurant,
                                                new_available=new_available, new_price=new_price, new_name=new_name,
                                                new_description=new_description, new_prepare_time=new_prepare_time,
                                                new_meal_type=new_meal_type, new_photo=new_photo,
                                                new_last_update=int(datetime.datetime.now().timestamp()))

        if product is None:
            raise NoItemsFound("product_id and restaurant")

        return product
