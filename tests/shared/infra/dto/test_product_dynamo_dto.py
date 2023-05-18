from decimal import Decimal

from src.shared.domain.entities.product import Product
from src.shared.domain.enums.meal_type_enum import MEAL_TYPE
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.infra.dto.product_dynamo_dto import ProductDynamoDTO
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock


class Test_ProductDynamoDto:
    def test_from_entity(self):
        repo = ProductRepositoryMock()

        product_dto = ProductDynamoDTO.from_entity(product=repo.products[0])

        expected_product_dto = ProductDynamoDTO(
            available=repo.products[0].available,
            price=repo.products[0].price,
            name=repo.products[0].name,
            description=repo.products[0].description,
            meal_type=repo.products[0].meal_type,
            photo=repo.products[0].photo,
            product_id=repo.products[0].product_id,
            last_update=repo.products[0].last_update,
            restaurant=repo.products[0].restaurant,
            prepare_time=repo.products[0].prepare_time
        )

        assert product_dto == expected_product_dto
        assert type(product_dto.price) == float
        assert type(product_dto.prepare_time) == int
        assert type(product_dto.last_update) == int
        
    def test_to_dynamo(self):
        repo = ProductRepositoryMock()

        product_dto = ProductDynamoDTO(
            available=repo.products[0].available,
            price=repo.products[0].price,
            name=repo.products[0].name,
            description=repo.products[0].description,
            meal_type=repo.products[0].meal_type,
            photo=repo.products[0].photo,
            product_id=repo.products[0].product_id,
            last_update=(repo.products[0].last_update),
            restaurant=repo.products[0].restaurant,
            prepare_time=(repo.products[0].prepare_time)
        )

        product_dynamo = product_dto.to_dynamo()

        expected_dict = {
            "entity": "product",
            "available": repo.products[0].available,
            "price": Decimal(repo.products[0].price),
            "name": repo.products[0].name,
            "description": repo.products[0].description,
            "meal_type": repo.products[0].meal_type.value,
            "photo": repo.products[0].photo,
            "product_id": repo.products[0].product_id,
            "last_update": Decimal(repo.products[0].last_update),
            "restaurant": repo.products[0].restaurant.value,
            "prepare_time": Decimal(repo.products[0].prepare_time),
        }

        assert product_dto.to_dynamo() == expected_dict
        assert type(expected_dict['price']) == Decimal
        assert type(expected_dict['last_update']) == Decimal
        assert type(expected_dict['prepare_time']) == Decimal

    def test_to_dynamo_prepare_time_none(self):
        repo = ProductRepositoryMock()
        
        product = repo.products[100]

        product_dto = ProductDynamoDTO(
            available=product.available,
            price=product.price,
            name=product.name,
            description=product.description,
            meal_type=product.meal_type,
            photo=product.photo,
            product_id=product.product_id,
            last_update=(product.last_update),
            restaurant=product.restaurant,
            prepare_time=(product.prepare_time)
        )

        product_dynamo = product_dto.to_dynamo()

        expected_dict = {
            "entity": "product",
            "available": product.available,
            "price": Decimal(product.price),
            "name": product.name,
            "description": product.description,
            "meal_type": product.meal_type.value,
            "photo": product.photo,
            "product_id": product.product_id,
            "last_update": Decimal(product.last_update),
            "restaurant": product.restaurant.value
        }

        assert expected_dict == product_dynamo

    def test_from_dynamo(self):
        dynamo_dict = {'Item': {'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                                'available' : eval('True'),
                                'price': Decimal('19.0'),
                                'name': 'X-Salada',
                                'description': 'Hamburguer/Mussarela/Maionese/Alface/Tomate',
                                'meal_type': 'SANDWICHES',
                                'photo': 'https://avatars.githubusercontent.com/u/30812461?v=4',
                                'last_update': Decimal('1678228149'),
                                'restaurant': 'SOUZA_DE_ABREU',
                                'prepare_time': Decimal('20'),
                                'SK': '#8a705b91-c9e9-4353-a755-07f13afafed3',
                                'PK': 'product#8a705b91-c9e9-4353-a755-07f13afafed3',
                                'entity': 'product'},
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}

        product_dto = ProductDynamoDTO.from_dynamo(product_data=dynamo_dict["Item"])

        expected_product_dto = ProductDynamoDTO(
            available=True,
            price= 19.0,
            name='X-Salada',
            description='Hamburguer/Mussarela/Maionese/Alface/Tomate',
            meal_type=MEAL_TYPE.SANDWICHES,
            photo='https://avatars.githubusercontent.com/u/30812461?v=4',
            product_id='8a705b91-c9e9-4353-a755-07f13afafed3',
            last_update=1678228149,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            prepare_time=20
        )

        assert product_dto == expected_product_dto
        assert type(dynamo_dict['Item']['price']) == Decimal
        assert type(dynamo_dict['Item']['last_update']) == Decimal
        assert type(dynamo_dict['Item']['prepare_time']) == Decimal

    def test_from_dynamo_prepare_time_none(self):
        dynamo_dict = {'Item': {'product_id': 'f92ac405-0a5c-43f8-827e-8cb6a64612ed',
                                'available' : 'True',
                                'price': Decimal('4.5'),
                                'name': 'Café',
                                'description': '',
                                'meal_type': 'DRINKS',
                                'photo': 'https://avatars.githubusercontent.com/u/30812461?v=4',
                                'last_update': Decimal('1677893281'),
                                'restaurant': 'CANTINA_DO_MOLEZA',
                                'prepare_time': None,
                                'SK': '#f92ac405-0a5c-43f8-827e-8cb6a64612ed',
                                'PK': 'product#f92ac405-0a5c-43f8-827e-8cb6a64612ed',
                                'entity': 'product'},
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}

        product_dto = ProductDynamoDTO.from_dynamo(product_data=dynamo_dict["Item"])

        expected_product_dto = ProductDynamoDTO(
            available=True,
            price= 4.5,
            name='Café',
            description='',
            meal_type=MEAL_TYPE.DRINKS,
            photo='https://avatars.githubusercontent.com/u/30812461?v=4',
            product_id='f92ac405-0a5c-43f8-827e-8cb6a64612ed',
            last_update=1677893281,
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            prepare_time=None
        )

        assert product_dto.prepare_time == expected_product_dto.prepare_time

    def test_to_entity(self):
        repo = ProductRepositoryMock()

        product_dto = ProductDynamoDTO(
            available=repo.products[0].available,
            price=repo.products[0].price,
            name=repo.products[0].name,
            description=repo.products[0].description,
            meal_type=repo.products[0].meal_type,
            photo=repo.products[0].photo,
            product_id=repo.products[0].product_id,
            last_update=repo.products[0].last_update,
            restaurant=repo.products[0].restaurant,
            prepare_time=repo.products[0].prepare_time
        )

        product = product_dto.to_entity()

        assert product.available == repo.products[0].available
        assert product.price == repo.products[0].price
        assert product.name == repo.products[0].name
        assert product.description == repo.products[0].description
        assert product.meal_type == repo.products[0].meal_type
        assert product.photo == repo.products[0].photo
        assert product.product_id == repo.products[0].product_id
        assert product.last_update == repo.products[0].last_update
        assert product.restaurant == repo.products[0].restaurant
        assert product.prepare_time == repo.products[0].prepare_time
        assert type(product.price) == float
        assert type(product.prepare_time) == int
        assert type(product.last_update) == int   

    def test_from_dynamo_to_entity(self):
        dynamo_item = {'Item': {'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                                'available': eval('True'),
                                'price': Decimal('19.0'),
                                'name': 'X-Salada',
                                'description': 'Hamburguer/Mussarela/Maionese/Alface/Tomate',
                                'prepare_time': Decimal('20'),
                                'meal_type': 'SANDWICHES',
                                'photo': 'https://avatars.githubusercontent.com/u/30812461?v=4',
                                'last_update': Decimal('1678228149'),
                                'restaurant': 'SOUZA_DE_ABREU',
                                'SK': '8a705b91-c9e9-4353-a755-07f13afafed3',
                                'state': 'APPROVED',
                                'PK': 'product#8a705b91-c9e9-4353-a755-07f13afafed3',
                                'entity': 'product',
                                }}

        product_dto = ProductDynamoDTO.from_dynamo(product_data=dynamo_item["Item"])

        product = product_dto.to_entity()

        expected_product = Product(
            available=True,
            price=19.0,
            name='X-Salada',
            description='Hamburguer/Mussarela/Maionese/Alface/Tomate',
            meal_type=MEAL_TYPE.SANDWICHES,
            photo='https://avatars.githubusercontent.com/u/30812461?v=4',
            product_id='8a705b91-c9e9-4353-a755-07f13afafed3',
            last_update=1678228149,
            restaurant=RESTAURANT.SOUZA_DE_ABREU,
            prepare_time=20
        )

        assert product.available == expected_product.available
        assert product.price == expected_product.price
        assert product.name == expected_product.name
        assert product.description == expected_product.description
        assert product.prepare_time == expected_product.prepare_time
        assert product.meal_type == expected_product.meal_type
        assert product.photo == expected_product.photo
        assert product.product_id == expected_product.product_id
        assert product.last_update == expected_product.last_update
        assert product.restaurant == expected_product.restaurant

    def test_from_entity_to_dynamo(self):
        repo = ProductRepositoryMock()

        product_dto = ProductDynamoDTO.from_entity(product=repo.products[0])

        product_dynamo = product_dto.to_dynamo()

        expected_dict = {
            "entity": "product",
            "available": repo.products[0].available,
            "price": repo.products[0].price,
            "name": repo.products[0].name,
            "description": repo.products[0].description,
            "meal_type": repo.products[0].meal_type.value,
            "photo": repo.products[0].photo,
            "product_id": repo.products[0].product_id,
            "last_update": repo.products[0].last_update,
            "restaurant": repo.products[0].restaurant.value,
            "prepare_time": repo.products[0].prepare_time,
        }

        assert product_dynamo == expected_dict