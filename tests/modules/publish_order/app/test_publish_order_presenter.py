from src.modules.publish_order.app.publish_order_presenter import lambda_handler


class Test_PublishOrderPresenter:

    def test_publish_order(self):
        event = {
   'Records':[
      {
         'eventID':'360c0c352e6725c7d8442d1ed333e87d',
         'eventName':'INSERT',
         'eventVersion':'1.1',
         'eventSource':'aws:dynamodb',
         'awsRegion':'sa-east-1',
         'dynamodb':{
            'ApproximateCreationDateTime':1692319436.0,
            'Keys':{
               'SK':{
                  'S':'order#b3f6c5aa-80ad-4f95-ae16-455b4f87fb53'
               },
               'PK':{
                  'S':'CANTINA_DO_MOLEZA'
               }
            },
            'NewImage':{
               'creation_time_milliseconds':{
                  'N':'1692061296000'
               },
               'status':{
                  'S':'READY'
               },
               'products':{"L":[
                   {"M":{
                   'product_id':{
                    'S':'8a705b91-c9e9-4353-a755-07f13afafed3'
               },
                   'product_name':{
                    'S':'X-Salada'
               }, 
                   'quantity':{
                    'N':'1'
               }
               }},
                   {"M":{
                   'product_id':{
                    'S':'e83289ce-abff-40b6-be52-f756a51ef0b2'
               },
                   'product_name':{
                    'S':'Suco de Laranja'
               }, 
                   'quantity':{
                    'N':'1'
               }
               }}]
               },
               'SK':{
                  'S':'order#b3f6c5aa-80ad-4f95-ae16-455b4f87fb53'
               },
               'user_name':{
                  'S':'Lucas Milas'
               },
               'PK':{
                  'S':'CANTINA_DO_MOLEZA'
               },
               'order_id':{
                  'S':'b3f6c5aa-80ad-4f95-ae16-455b4f87fb53'
               },
               'restaurant':{
                  'S':'CANTINA_DO_MOLEZA'
               },
               'action':{
                  'S':'NEW'
               },
               'total_price':{
                  'N':'30.00'
               },
               'user_id':{
                  'S':'93bc6ada-c0d1-7054-66ab-e17414c48gbf'
               },
               'observation':{
                  'S':'Açúcar no suco'
               },
               'entity':{
                  'S':'order'
               },
            },
            'SequenceNumber':'61997000000000016745665842',
            'SizeBytes':200,
            'StreamViewType':'NEW_AND_OLD_IMAGES'
         },
         'eventSourceARN':'arn:aws:dynamodb:sa-east-1:264055331071:table/mf-poc-080423/stream/2023-08-18T00:40:13.123'
      }
   ]
}
        response = lambda_handler(event, None)

        assert response["statusCode"] == 200