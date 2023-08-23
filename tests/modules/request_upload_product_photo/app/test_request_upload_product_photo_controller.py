import pytest
from src.modules.request_upload_product_photo.app.request_upload_product_photo_controller import RequestUploadProductPhotoController
from src.modules.request_upload_product_photo.app.request_upload_product_photo_usecase import RequestUploadProductPhotoUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_RequestUploadProductPhotoController:

    def test_request_upload_product_photo_controller(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = RequestUploadProductPhotoUsecase(repo_product, repo_user)
        controller = RequestUploadProductPhotoController(usecase=usecase)
        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
            "product_id": "8a705b91-c9e9-4353-a755-07f13afafed3",
        })
        
        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.body['message'] == "Photo uploaded successufully."
        
    def test_request_upload_product_photo_controller_product_id_is_missing(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = RequestUploadProductPhotoUsecase(repo_product, repo_user)
        controller = RequestUploadProductPhotoController(usecase=usecase)
        request = HttpRequest(body={'requester_user': {
            "sub": repo_user.users_list[0].user_id,
            "name": repo_user.users_list[0].name,
            "email": repo_user.users_list[0].email,
            "custom:isMaua": True
        },
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field product_id is missing"

    def test_request_upload_product_photo_controller_requester_user_is_missing(self):
        repo_product = ProductRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = RequestUploadProductPhotoUsecase(repo_product, repo_user)
        controller = RequestUploadProductPhotoController(usecase=usecase)
        request = HttpRequest(body={
            "product_id": "8a705b91-c9e9-4353-a755-07f13afafed3"
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"

    

        
    