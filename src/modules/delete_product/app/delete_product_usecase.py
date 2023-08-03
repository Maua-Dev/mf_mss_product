from src.shared.domain.entities.product import Product
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser, UserNotAllowed


class DeleteProductUsecase:
    def __init__(self, repo_product: IProductRepository, repo_user: IUserRepository):
        self.repo_product = repo_product
        self.repo_user = repo_user

    def __call__(self, product_id: str, restaurant: RESTAURANT, user_id: str) -> Product:
        
        user = self.repo_user.get_user_by_id(user_id)

        if user is None:
            raise UnregisteredUser()

        if user.role not in [ROLE.OWNER, ROLE.ADMIN]:
            raise UserNotAllowed()
        
        if not Product.validate_product_id(product_id=product_id):
            raise EntityError("product_id")

        if type(restaurant) != RESTAURANT:
            raise EntityError("restaurant")

        product = self.repo_product.delete_product(product_id=product_id,restaurant=restaurant)

        if product is None:
            raise NoItemsFound("product_id and restaurant")
        
        return product