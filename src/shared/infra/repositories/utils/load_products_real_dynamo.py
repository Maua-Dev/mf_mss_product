from src.shared.environments import Environments
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


if __name__ == '__main__':

    repo_product = Environments.get_product_repo()()
    products = ProductRepositoryMock().products

    for product in products:
        try:
            new_product = repo_product.create_product(product)

            print(new_product)

        except Exception as e:
            print("Erro ao criar produto: ", e)