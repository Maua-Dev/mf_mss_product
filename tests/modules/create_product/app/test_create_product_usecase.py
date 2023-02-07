from src.shared.domain.entities.product import Product
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
from src.modules.create_product.app.create_product_usecase import CreateProductUsecase

class Test_CreateProductUsecase:
    def test_create_product_usecase(self):
        repo = ProductRepositoryMock()
        usecase = CreateProductUsecase(repo=repo)
        productLenBefore = len(repo.products)

        product = usecase(product=Product)
        
        productLenAfter = productLenBefore + 1

        assert len(repo.products) == productLenAfter
        
