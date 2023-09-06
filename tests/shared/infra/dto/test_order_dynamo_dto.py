from src.shared.domain.entities.order import Order
from src.shared.domain.entities.order_product import OrderProduct
from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.status_enum import STATUS
from src.shared.infra.dto.order_dynamo_dto import OrderDynamoDTO


class Test_OrderDynamoDTO:

    def test_from_entity(self):
        order = Order(
            order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            user_name="Rodrigo Morales",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            products=[
                OrderProduct(product_name="X-Salada", product_id="8a705b91-c9e9-4353-a755-07f13afafed3", quantity=1),
                ],
            creation_time_milliseconds=1692061296000,
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            status=STATUS.READY,
            total_price=50.0,
            last_status_update_milliseconds=1992061596999,
            observation="Ketchup para acompanhar",
            aborted_reason=None
        )

        order_dynamo_dto = OrderDynamoDTO.from_entity(order)

        expected_order_dynamo_dto = OrderDynamoDTO(
            order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            user_name="Rodrigo Morales",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            products=[
                OrderProduct(product_name="X-Salada", product_id="8a705b91-c9e9-4353-a755-07f13afafed3", quantity=1),
                ],
            creation_time_milliseconds=1692061296000,
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            status=STATUS.READY,
            total_price=50.0,
            last_status_update_milliseconds=1992061596999,
            observation="Ketchup para acompanhar",
            aborted_reason=None
        )

        assert order_dynamo_dto.order_id == expected_order_dynamo_dto.order_id
        assert order_dynamo_dto.user_name == expected_order_dynamo_dto.user_name
        assert order_dynamo_dto.user_id == expected_order_dynamo_dto.user_id
        assert order_dynamo_dto.products == expected_order_dynamo_dto.products
        assert order_dynamo_dto.creation_time_milliseconds == expected_order_dynamo_dto.creation_time_milliseconds
        assert order_dynamo_dto.restaurant == expected_order_dynamo_dto.restaurant
        assert order_dynamo_dto.status == expected_order_dynamo_dto.status
        assert order_dynamo_dto.total_price == expected_order_dynamo_dto.total_price
        assert order_dynamo_dto.last_status_update_milliseconds == expected_order_dynamo_dto.last_status_update_milliseconds
        assert order_dynamo_dto.observation == expected_order_dynamo_dto.observation
        assert order_dynamo_dto.aborted_reason == expected_order_dynamo_dto.aborted_reason
        assert order_dynamo_dto == expected_order_dynamo_dto

    def test_to_dynamo(self):
        order_dynamo_dto = OrderDynamoDTO(
            order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            user_name="Rodrigo Morales",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            products=[
                OrderProduct(product_name="X-Salada", product_id="8a705b91-c9e9-4353-a755-07f13afafed3", quantity=1),
                ],
            creation_time_milliseconds=1692061296000,
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            status=STATUS.READY,
            total_price=50.0,
            last_status_update_milliseconds=1992061596999,
            observation="Ketchup para acompanhar",
            aborted_reason="Recusada"
        )

        expected_dynamo = {
            "order_id":"b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            "user_name":"Rodrigo Morales",
            "user_id":"93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            "products":[
                {"product_name":"X-Salada", 
                "product_id":"8a705b91-c9e9-4353-a755-07f13afafed3", 
                "quantity":1}
                ],
            "creation_time_milliseconds":1692061296000,
            "restaurant":"CANTINA_DO_MOLEZA",
            "status":"READY",
            "total_price":50.0,
            "last_status_update_milliseconds":1992061596999,
            "observation":"Ketchup para acompanhar",
            "aborted_reason":"Recusada",
            "entity": "order"
        }

        assert expected_dynamo == order_dynamo_dto.to_dynamo()

    def test_to_dynamo_observation_none(self):
        order_dynamo_dto = OrderDynamoDTO(
            order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            user_name="Rodrigo Morales",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            products=[
                OrderProduct(product_name="X-Salada", product_id="8a705b91-c9e9-4353-a755-07f13afafed3", quantity=1),
                ],
            creation_time_milliseconds=1692061296000,
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            status=STATUS.READY,
            total_price=50.0,
            last_status_update_milliseconds=1992061596999,
            aborted_reason="Recusada"
        )

        expected_dynamo = {
            "order_id":"b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            "user_name":"Rodrigo Morales",
            "user_id":"93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            "products":[
                {"product_name":"X-Salada", 
                "product_id":"8a705b91-c9e9-4353-a755-07f13afafed3", 
                "quantity":1}
                ],
            "creation_time_milliseconds":1692061296000,
            "restaurant":"CANTINA_DO_MOLEZA",
            "status":"READY",
            "total_price":50.0,
            "last_status_update_milliseconds":1992061596999,
            "aborted_reason":"Recusada",
            "entity": "order"
        }

        assert expected_dynamo == order_dynamo_dto.to_dynamo()

    def test_to_dynamo_aborted_reason_none(self):
        order_dynamo_dto = OrderDynamoDTO(
            order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            user_name="Rodrigo Morales",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            products=[
                OrderProduct(product_name="X-Salada", product_id="8a705b91-c9e9-4353-a755-07f13afafed3", quantity=1),
                ],
            creation_time_milliseconds=1692061296000,
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            status=STATUS.READY,
            total_price=50.0,
            last_status_update_milliseconds=1992061596999,
            observation="Ketchup para acompanhar"
        )

        expected_dynamo = {
            "order_id":"b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            "user_name":"Rodrigo Morales",
            "user_id":"93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            "products":[
                {"product_name":"X-Salada", 
                "product_id":"8a705b91-c9e9-4353-a755-07f13afafed3", 
                "quantity":1}
                ],
            "creation_time_milliseconds":1692061296000,
            "restaurant":"CANTINA_DO_MOLEZA",
            "status":"READY",
            "total_price":50.0,
            "last_status_update_milliseconds":1992061596999,
            "observation":"Ketchup para acompanhar",
            "entity": "order"
        }

        assert expected_dynamo == order_dynamo_dto.to_dynamo()

    def test_from_entity_to_dynamo(self):
        order = Order(
            order_id="b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            user_name="Rodrigo Morales",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            products=[
                OrderProduct(product_name="X-Salada", product_id="8a705b91-c9e9-4353-a755-07f13afafed3", quantity=1),
                ],
            creation_time_milliseconds=1692061296000,
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            status=STATUS.READY,
            total_price=50.0,
            last_status_update_milliseconds=1992061596999,
            observation="Ketchup para acompanhar",
            aborted_reason="Recusada"
        )

        order_dynamo_dto = OrderDynamoDTO.from_entity(order)

        expected_dynamo = {
            "order_id":"b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            "user_name":"Rodrigo Morales",
            "user_id":"93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            "products":[
                {"product_name":"X-Salada", 
                "product_id":"8a705b91-c9e9-4353-a755-07f13afafed3", 
                "quantity":1}
                ],
            "creation_time_milliseconds":1692061296000,
            "restaurant":"CANTINA_DO_MOLEZA",
            "status":"READY",
            "total_price":50.0,
            "last_status_update_milliseconds":1992061596999,
            "observation":"Ketchup para acompanhar",
            "aborted_reason":"Recusada",
            "entity": "order"
        }

        assert expected_dynamo == order_dynamo_dto.to_dynamo()

    def test_from_dynamo(self):
        dynamo_dict = {'Item': {'order_id': 'b3f6c5aa-80ad-4f95-ae16-455b4f87fb53',
                                'user_name' : 'Rodrigo Morales',
                                'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48abb',
                                'products': [
                                {
                                'product_name': 'X-Salada',
                                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                                "quantity":1
                                }
                            ],
                                'creation_time_milliseconds': 1692061296000,
                                "restaurant":"CANTINA_DO_MOLEZA",
                                "status":"READY",
                                "total_price":50.0,
                                "last_status_update_milliseconds":1992061596999,
                                "observation":"Ketchup para acompanhar",
                                "aborted_reason":"Recusada",
                                'entity': 'order'},
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}

        order_dto = OrderDynamoDTO.from_dynamo(order_data=dynamo_dict["Item"])

        expected_order_dto = OrderDynamoDTO(
            order_id='b3f6c5aa-80ad-4f95-ae16-455b4f87fb53',
            user_name="Rodrigo Morales",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            products=[
                OrderProduct(product_name="X-Salada", product_id='8a705b91-c9e9-4353-a755-07f13afafed3', quantity=1)],
            creation_time_milliseconds=1692061296000,
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            status=STATUS.READY,
            total_price=50.0,
            last_status_update_milliseconds=1992061596999,
            observation="Ketchup para acompanhar",
            aborted_reason="Recusada"
        )

        assert order_dto == expected_order_dto

    def test_from_dynamo_observation_none(self):
        dynamo_dict = {'Item': {'order_id': 'b3f6c5aa-80ad-4f95-ae16-455b4f87fb53',
                                'user_name' : 'Rodrigo Morales',
                                'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48abb',
                                'products': [
                                {
                                'product_name': 'X-Salada',
                                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                                "quantity":1
                                }
                            ],
                                'creation_time_milliseconds': 1692061296000,
                                "restaurant":"CANTINA_DO_MOLEZA",
                                "status":"READY",
                                "total_price":50.0,
                                "last_status_update_milliseconds":1992061596999,
                                "aborted_reason":"Recusada",
                                'entity': 'order'},
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}

        order_dto = OrderDynamoDTO.from_dynamo(order_data=dynamo_dict["Item"])

        expected_order_dto = OrderDynamoDTO(
            order_id='b3f6c5aa-80ad-4f95-ae16-455b4f87fb53',
            user_name="Rodrigo Morales",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            products=[
                OrderProduct(product_name="X-Salada", product_id='8a705b91-c9e9-4353-a755-07f13afafed3', quantity=1)],
            creation_time_milliseconds=1692061296000,
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            status=STATUS.READY,
            total_price=50.0,
            last_status_update_milliseconds=1992061596999,
            aborted_reason="Recusada"
        )

        assert order_dto == expected_order_dto

    def test_from_dynamo_aborted_reason_none(self):
        dynamo_dict = {'Item': {'order_id': 'b3f6c5aa-80ad-4f95-ae16-455b4f87fb53',
                                'user_name' : 'Rodrigo Morales',
                                'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48abb',
                                'products': [
                                {
                                'product_name': 'X-Salada',
                                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                                "quantity":1
                                }
                            ],
                                'creation_time_milliseconds': 1692061296000,
                                "restaurant":"CANTINA_DO_MOLEZA",
                                "status":"READY",
                                "total_price":50.0,
                                "last_status_update_milliseconds":1992061596999,
                                "observation":"Ketchup para acompanhar",
                                'entity': 'order'},
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}

        order_dto = OrderDynamoDTO.from_dynamo(order_data=dynamo_dict["Item"])

        expected_order_dto = OrderDynamoDTO(
            order_id='b3f6c5aa-80ad-4f95-ae16-455b4f87fb53',
            user_name="Rodrigo Morales",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            products=[
                OrderProduct(product_name="X-Salada", product_id='8a705b91-c9e9-4353-a755-07f13afafed3', quantity=1)],
            creation_time_milliseconds=1692061296000,
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            status=STATUS.READY,
            total_price=50.0,
            last_status_update_milliseconds=1992061596999,
            observation="Ketchup para acompanhar"
        )

        assert order_dto == expected_order_dto

    def test_to_entity(self):
        order_dynamo_dto = OrderDynamoDTO(
            order_id='b3f6c5aa-80ad-4f95-ae16-455b4f87fb53',
            user_name="Rodrigo Morales",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            products=[
                OrderProduct(product_name="X-Salada", product_id='8a705b91-c9e9-4353-a755-07f13afafed3', quantity=1)],
            creation_time_milliseconds=1692061296000,
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            status=STATUS.READY,
            total_price=50.0,
            last_status_update_milliseconds=1992061596999,
            observation="Ketchup para acompanhar",
            aborted_reason="Recusada"
        )

        expected_order = Order(
            order_id='b3f6c5aa-80ad-4f95-ae16-455b4f87fb53',
            user_name="Rodrigo Morales",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            products=[
                OrderProduct(product_name="X-Salada", product_id='8a705b91-c9e9-4353-a755-07f13afafed3', quantity=1)],
            creation_time_milliseconds=1692061296000,
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            status=STATUS.READY,
            total_price=50.0,
            last_status_update_milliseconds=1992061596999,
            observation="Ketchup para acompanhar",
            aborted_reason="Recusada"
        )

        order = order_dynamo_dto.to_entity()

        assert type(expected_order) == type(order)
        assert expected_order.order_id == order.order_id
        assert expected_order.user_name == order.user_name
        assert expected_order.user_id == order.user_id
        assert expected_order.products == order.products
        assert expected_order.creation_time_milliseconds == order.creation_time_milliseconds
        assert expected_order.restaurant == order.restaurant
        assert expected_order.status == order.status
        assert expected_order.total_price == order.total_price
        assert expected_order.last_status_update_milliseconds == order.last_status_update_milliseconds
        assert expected_order.observation == order.observation
        assert expected_order.aborted_reason == order.aborted_reason 

    def test_from_dynamo_to_entity(self):
        dynamo_dict = {'Item': {'order_id': 'b3f6c5aa-80ad-4f95-ae16-455b4f87fb53',
                                'user_name' : 'Rodrigo Morales',
                                'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48abb',
                                'products': [
                                {
                                'product_name': 'X-Salada',
                                'product_id': '8a705b91-c9e9-4353-a755-07f13afafed3',
                                "quantity":1
                                }
                            ],
                                'creation_time_milliseconds': 1692061296000,
                                "restaurant":"CANTINA_DO_MOLEZA",
                                "status":"READY",
                                "total_price":50.0,
                                "last_status_update_milliseconds":1992061596999,
                                "observation":"Ketchup para acompanhar",
                                "aborted_reason":"Recusada",
                                'entity': 'order'},
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}

        order_dynamo_dto = OrderDynamoDTO.from_dynamo(order_data=dynamo_dict["Item"])

        expected_order = Order(
            order_id='b3f6c5aa-80ad-4f95-ae16-455b4f87fb53',
            user_name="Rodrigo Morales",
            user_id="93bc6ada-c0d1-7054-66ab-e17414c48abb",
            products=[
                OrderProduct(product_name="X-Salada", product_id='8a705b91-c9e9-4353-a755-07f13afafed3', quantity=1)],
            creation_time_milliseconds=1692061296000,
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            status=STATUS.READY,
            total_price=50.0,
            last_status_update_milliseconds=1992061596999,
            observation="Ketchup para acompanhar",
            aborted_reason="Recusada"
        )

        order = order_dynamo_dto.to_entity()

        assert type(expected_order) == type(order)
        assert expected_order.order_id == order.order_id
        assert expected_order.user_name == order.user_name
        assert expected_order.user_id == order.user_id
        assert expected_order.products == order.products
        assert expected_order.creation_time_milliseconds == order.creation_time_milliseconds
        assert expected_order.restaurant == order.restaurant
        assert expected_order.status == order.status
        assert expected_order.total_price == order.total_price
        assert expected_order.last_status_update_milliseconds == order.last_status_update_milliseconds
        assert expected_order.observation == order.observation
        assert expected_order.aborted_reason == order.aborted_reason 

    
    