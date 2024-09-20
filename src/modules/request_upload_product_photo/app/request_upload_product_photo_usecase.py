import datetime

from src.modules.delete_product.app.delete_product_presenter import repo_product
from src.shared.domain.entities.product import Product
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed

class RequestUploadProductPhotoUsecase:
    def __init__(self, repo_product: IProductRepository, repo_user: IUserRepository):
        self.repo_product = repo_product
        self.repo_user = repo_user

    def __call__(self, product_id: str, user_id: str) -> dict:
        
        if not Product.validate_product_id(product_id):
            raise EntityError('product_id')
        
        if not User.validate_user_id(user_id):
            raise EntityError('user_id')
        
        user = self.repo_user.get_user_by_id(user_id)

        if user is None:
            raise UnregisteredUser()

        if user.role not in [ROLE.OWNER, ROLE.ADMIN]:
            raise UserNotAllowed()

        if user.restaurant is None:
            raise UserNotAllowed()

        if repo_product.get_product(product_id=product_id, restaurant=user.restaurant) is None:
            raise UserNotAllowed()
        
        presigned_post = self.repo_product.request_upload_product_photo(product_id=product_id, user_id=user.user_id)

        return presigned_post