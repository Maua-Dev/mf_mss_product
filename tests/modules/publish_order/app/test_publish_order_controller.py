from src.modules.publish_order.app.publish_order_controller import PublishOrderController
from src.modules.publish_order.app.publish_order_usecase import PublishOrderUsecase
from src.shared.helpers.external_interfaces.dynamo_event_parser import DynamoEventParser
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock


class Test_PublishOrderControler:
    def test_publish_order_controller(self):
        repo = OrderRepositoryMock()
        usecase = PublishOrderUsecase(repo=repo)
        controller = PublishOrderController(usecase=usecase)
        request = DynamoEventParser()
        request.data ={
        'all_records':[
        {
         'event_id':'360c0c352e6725c7d8442d1ed333e87d',
         'event_name':'INSERT',
         'new_image':{
            'PK':'CANTINA_DO_MOLEZA',
            'SK':'order#b3f6c5aa-80ad-4f95-ae16-455b4f87fb53',
            'creation_time_milliseconds':'1692061296000',
            'order_id':"b3f6c5aa-80ad-4f95-ae16-455b4f87fb53",
            'products':[
               {
                  'product_id':"8a705b91-c9e9-4353-a755-07f13afafed3",
                  'product_name':'X-Salada',
                  'quantity':'1',
                  'observation': None
               },
               {
                  'product_id':"e83289ce-abff-40b6-be52-f756a51ef0b2",
                  'product_name':'Suco de Laranja',
                  'quantity':'1',
                  'observation': "Açúcar no suco",
        }
            ],
            'restaurant':'CANTINA_DO_MOLEZA',
            'status':'READY',
            'action':'NEW',
            'total_price':'30.00',
            'user_name':'Lucas Milas',
            'user_id': "93bc6ada-c0d1-7054-66ab-e17414c48gbf",
            'entity': 'order'
         },
         'old_image':{
            
         }
        }
    ]
}

        response = controller(request)

        assert response.status_code == 200
        assert response.body["message"] == 'The order b3f6c5aa-80ad-4f95-ae16-455b4f87fb53 was published'