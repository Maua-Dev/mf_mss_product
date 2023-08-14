import datetime
from src.modules.request_upload_product_photo.app.request_upload_product_photo_usecase import RequestUploadProductPhotoUsecase
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
import pytest

class Test_RequestUploadProductPhotoUsecase:
    def test_request_upload_product_photo(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = RequestUploadProductPhotoUsecase(repo_product, repo_user)
       
        presignedPost = usecase(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae5")
       
        assert presignedPost['url'] == "https://test-upload-product-photo.s3.amazonaws.com/"
        assert presignedPost['metadata']['product_id'] == "8a705b91-c9e9-4353-a755-07f13afafed3"
        assert presignedPost['metadata']['user_id'] == "93bc6ada-c0d1-7054-66ab-e17414c48ae5"
        assert presignedPost['metadata']['time_created'] == str(int(datetime.datetime.now().timestamp()*1000))
        
    def test_request_upload_product_photo_user_not_allowed(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = RequestUploadProductPhotoUsecase(repo_product, repo_user)
       
        with pytest.raises(UserNotAllowed):
            presignedPost = usecase(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", user_id="93bc6ada-c0d1-7054-66ab-e17414c48af9")
       
    def test_request_upload_product_photo_unregisted_user(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = RequestUploadProductPhotoUsecase(repo_product, repo_user)
       
        with pytest.raises(UnregisteredUser):
            presignedPost = usecase(product_id="8a705b91-c9e9-4353-a755-07f13afafed3", user_id="id")

    def test_request_upload_product_photo_invalid_product_id(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = RequestUploadProductPhotoUsecase(repo_product, repo_user)
       
        with pytest.raises(EntityError):
            presignedPost = usecase(product_id="um product_id", user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae5")
    