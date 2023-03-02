import json
from src.modules.get_all_products_group_by_restaurant.app.get_all_products_group_by_restaurant_presenter import lambda_handler


class Test_GetAllProductGroupByRestaurantPresenter:
    def test_get_all_products_group_by_restaurant_presenter(self):

        event = {
          "version": "2.0",
          "routeKey": "$default",
          "rawPath": "/my/path", 
          "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
          "cookies": [
            "cookie1",
            "cookie2"
          ],
          "headers": {
            "header1": "value1",
            "header2": "value1,value2"
          },
          "queryStringParameters": {
          },
          "requestContext": {
            "accountId": "123456789012",
            "apiId": "<urlid>",
            "authentication": None,
            "authorizer": {
                "iam": {
                        "accessKey": "AKIA...",
                        "accountId": "111122223333",
                        "callerId": "AIDA...",
                        "cognitoIdentity": None,
                        "principalOrgId": None,
                        "userArn": "arn:aws:iam::111122223333:user/example-user",
                        "userId": "AIDA..."
                }
            },
            "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
            "domainPrefix": "<url-id>",
            "http": {
              "method": "POST",
              "path": "/my/path",
              "protocol": "HTTP/1.1",
              "sourceIp": "123.123.123.123",
              "userAgent": "agent"
            },
            "requestId": "id",
            "routeKey": "$default",
            "stage": "$default",
            "time": "12/Mar/2020:19:03:58 +0000",
            "timeEpoch": 1583348638390
          },
          "body": "Visualize all the products",
          "pathParameters": None,
          "isBase64Encoded": None,
          "stageVariables": None
        }

        response = lambda_handler(event, None)

        expected = {
        'SOUZA_DE_ABREU':[
            {
                'available':True,
                'price':16.0,
                'name':'X-Salada',
                'description':'Hamburguer/Mussarela/Maionese/Alface/Tomate',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'8a705b91-c9e9-4353-a755-07f13afafed3',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':14.0,
                'name':'Lanche Mortadela',
                'description':'Mortadela',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'cf8b01e6-ea9f-40fc-8344-d77d61761fbe',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'X-Burguer',
                'description':'Hamburguer/Mussarela/Maionese',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'052deac5-3b97-4b44-a0ff-e5d59ed8a69b',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':18.0,
                'name':'X-Bacon',
                'description':'Hamburguer/Bacon/Mussarela/Maionese/Alface/Tomate',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'2f9ad2af-a751-4adf-81c4-50e6a9b06c8b',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':15.0,
                'name':'X-Egg',
                'description':'Hamburguer/Ovo/Mussarela/Maionese/Alface/Tomate',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'d16053c9-25dc-40b3-9257-0719c4622cc3',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':18.0,
                'name':'X-Calabresa',
                'description':'Calabresa/Mussarela/Alface/Tomate',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'8ffcc3ef-6d35-4fef-abf0-85d3649a85d5',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':18.0,
                'name':'X-Frango',
                'description':'Filé de Frango/Mussarela/Maionese/Alface/Tomate',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'26a1e370-bc59-4b69-9676-51b0eed656ac',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':16.0,
                'name':'Americano',
                'description':'Presunto/Ovo/Mussarela/Maionese/Alface/Tomate/Orégano',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'7de7e966-16d0-4a1e-96d2-13c00ba86869',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':12.0,
                'name':'Misto Quente',
                'description':'Presunto/Mussarela/Orégano',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'cd54faed-a721-4023-a0a4-d447b553b599',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':13.0,
                'name':'Bauru',
                'description':'Presunto/Mussarela/Tomate/Orégano',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'e222e1d5-b8ab-4693-b978-8b234c7f6595',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':18.0,
                'name':'Churrasco',
                'description':'Contra Filé',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'e1027314-13aa-44a2-87be-e66eb9307765',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':21.0,
                'name':'Ch. c/ Queijo',
                'description':'Contra Filé/Mussarela',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'b540f438-01fe-45c0-9513-7e092a3b02e6',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':23.0,
                'name':'Ch. c/ Vinag.',
                'description':'Contra Filé/Vinagrete',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'ef0ce1aa-1fb6-4e15-b490-2fd8a5623a43',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':25.0,
                'name':'Ch. c/ Queijo/Vinag.',
                'description':'Contra Filé/Mussarela/Vinagrete',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'dc325006-8d4e-4dfe-be33-f8b87adb1782',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':17.0,
                'name':'Mort. c/ Mussarela',
                'description':'Mortadela/Mussarela',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'dbc6a4ac-00c9-4879-b964-f5b80908c196',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':14.0,
                'name':'Lanche Natural',
                'description':'Peito de Peru/Mussarela/Alface/Tomate',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'fc85b4ef-2ab0-4591-8bf5-6e3f1ed53849',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':26.0,
                'name':'X-Tudo',
                'description':'2x Hamurguer/Ovo/Presunto/Calabresa/Bacon/Mussarela/Maionese/Alface/Tomate',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'3c73e9ab-b01f-40ba-a1c8-f34be5caede7',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':20.0,
                'name':'Vasco de Frango',
                'description':'Filé de Frango/Batata Palha/Catupiry/Mussarela',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'39c6556c-680a-4c48-a80a-0e4bb53d965e',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':23.0,
                'name':'Vasco de Carne',
                'description':'Contra Filé/Batata Palha/Catupiry/Mussarela',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'f2d2dea8-a7eb-43f8-82cf-bb8fa647227d',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':19.0,
                'name':'Vasco de Calabresa',
                'description':'Calabresa/Batata Palha/Catupiry/Mussarela',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'00170e97-6a4a-49c7-8bb2-342071ad752e',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'Pão c/ Ovo',
                'description':'Ovo',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'06147f40-1962-4072-9197-f591223c0005',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':11.0,
                'name':'Pão c/ Ovo/Mussar.',
                'description':'Ovo/Mussarela/Orégano',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'f3cd6997-e2a3-47dd-8197-0536e4e480fe',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':14.0,
                'name':'Misto/Batata Palha',
                'description':'Presunto/Batata Palha/Mussarela/Orégano',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'219f1d27-8542-471c-a0d3-989b4392054c',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':25.0,
                'name':'Beirute Carne I',
                'description':'Carne/Alface/Tomate/Mussarela/Ovo',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'4c0efc96-610f-40e0-af54-ee332e2174d2',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':28.0,
                'name':'Beirute Carne II',
                'description':'Carne/Alface/Tomate/Mussarela/Ovo/Bacon/Cheddar',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'841e50ea-5609-4d61-a76b-195de5662018',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':24.0,
                'name':'Beirute Frango',
                'description':'Frango/Alface/Tomate/Mussarela/Ovo',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'17d2e5cb-c70d-4985-a5d0-b5bb44412d92',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':22.0,
                'name':'Beirute Calabresa',
                'description':'Calabresa/Alface/Tomate/Mussarela/Ovo',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'3c5d43fc-2fa1-4e2a-bfee-8cf639d7a905',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'Cone Trufado',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'5ee19425-3bd2-434e-908d-13ed158772b5',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':14.0,
                'name':'Bolo de Pote',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'8f2139c5-37a4-4e4a-998c-35cafcc5db7e',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'Brigadeiro',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'520decf1-e781-4183-be50-408280481d65',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':4.0,
                'name':'Sonho de Valsa',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'caed1fd9-02bd-45b3-a52c-f9f4df030f28',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':6.0,
                'name':'Barra de Cereais',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'bf9bb615-e963-4056-ad77-82676351c24c',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':6.0,
                'name':'Chocolates',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'55349764-e316-41f9-a13d-24606bdf5428',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':3.0,
                'name':'Paçoquita',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'79e2706e-7621-43ab-b6d1-82aeb45fc57c',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':6.0,
                'name':'Trident',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'e1c5ef03-cfab-4c0a-92b3-b2252dcbfb9c',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':5.0,
                'name':'Halls',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'0eb93198-1605-4741-893e-93fe56a413a4',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':0.0,
                'name':'Sorvetes',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'760df1fe-5ced-4b30-9530-82fa1431fb2b',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':13.0,
                'name':'Salada de Fruta',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'bfdc471e-1a2c-4bf8-b327-77cebd6d73e4',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':17.0,
                'name':'Açaí',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'971b816a-7739-427a-bbe2-3610399cf282',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':13.0,
                'name':'Gelatina Colorida',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'657f235b-c795-4e1d-929b-0ac227a50444',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':18.0,
                'name':'Copo da Felicidade',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'4d1716c4-5e51-4d72-ba93-349e31201a22',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':15.0,
                'name':'Musse/Chocolate',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'bfbe8b90-63d0-459e-b8ef-598a181cf8fc',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':0.0,
                'name':'Queijo Quente 01',
                'description':'Mussarela/Tomate/Orégano/No Prato',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'92c86257-e25c-449b-a589-39da2902c884',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':0.0,
                'name':'Queijo Quente 02',
                'description':'Queijo Brancp/Tomate/Orégano/No Prato',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'20602c5e-adb3-426a-8176-59fabca63aaf',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':0.0,
                'name':'Queijo Quente 03',
                'description':'Queijo Brancp/Tomate Seco/Orégano/No Prato',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'86834cce-2334-44dc-bf34-e12b9217c963',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':0.0,
                'name':'Prima',
                'description':'Contra Filé/Bacon/Cheddar/Catupiry/Batata Palha/No Prato',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'0edfd473-7c37-4e25-b6b4-872b535d7477',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Refrigerante Lata',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'29f360d0-fd00-4ae1-8b24-e00f37624b02',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'Tônica Schweppes',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'890fd3cd-9b18-42ef-bec4-b9687d8cd676',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'Suco Lata',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'9aa4ebcb-a9e8-4585-a387-8c6096218433',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'H2O',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'006265f5-5303-4913-93f5-0fb7ec314034',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'Chá - Lata',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'af4d020c-01d6-4786-99b5-94ef3a5d33eb',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':15.0,
                'name':'Energético',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'dca552c0-a0ed-411b-8ea3-c8b365f908d4',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':6.0,
                'name':'Água c/ Gás',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'12121529-ce72-458a-91da-a1106ede10d3',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':5.0,
                'name':'Água s/ Gás',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'d2b32a22-efb5-4dc1-8a8c-21bfe849bebd',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':9.0,
                'name':'Suco de Laranja',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'e83289ce-abff-40b6-be52-f756a51ef0b2',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':11.0,
                'name':'Suco de Melância',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'6c993b58-af90-49d4-b537-e7824181ebe0',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':11.0,
                'name':'Suco Misto | Polpa',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'60057b1c-b966-4e19-8247-c821e425cc2e',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':6.0,
                'name':'Toddynho',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'3a707065-a73b-4d24-848b-4dbca8cd4b39',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':11.0,
                'name':'Vitamina Mista',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'a75d2891-4c80-4cf9-8102-3c8b08931cab',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':9.0,
                'name':'Gatorade',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'80ac0065-229d-4d14-bd77-1d5d6be45fe7',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'Guaraviton',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'5e87b3d9-b309-477e-897e-d44e6d49782c',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':11.0,
                'name':'Chocolate Batido',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'be16d4db-19c3-4f5c-88ef-429e37b4f9ef',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':6.5,
                'name':'Café - peq.',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'b3cbc545-739f-4d23-9025-601e9a27bb55',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':7.5,
                'name':'Café - gde.',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'0d8fc166-a4a0-4a3b-887e-d51e8e78fd19',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Capuccino - peq.',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'760379f7-2806-4e4b-a1cb-347bb2d4405e',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':9.0,
                'name':'Capuccino - gde.',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'4e6979d6-c9c3-438e-9b8c-e4d799358720',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Chocolate - peq.',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'5c8e2ac3-81c1-4f40-8856-8790e60844e5',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':9.0,
                'name':'Chocolate - gde.',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'eb82b21e-98c9-4dc7-962a-ffd17ea487f8',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':5.0,
                'name':'Chá Quente',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'b0e734f1-42e3-4007-82ee-9a7e6d6abc71',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Pão de Queijo',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'0165b801-04c5-41b7-82bb-10f1501333ae',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Coxinha',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'ff9e45db-47ac-4f4c-8453-fc47c364db56',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Esfihas',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'a09b1ab6-f867-4e3e-9878-395198d1f0cd',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Folhadinhos',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'53147297-15a0-45a6-8624-84380c58ae3f',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':11.0,
                'name':'Quiche',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'0dbf752b-5c05-42ef-b7ee-f2e5d066297b',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':9.0,
                'name':'Empada',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'0312246c-93e7-4358-aee4-3674c1753f02',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Bauruzinho',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'094e7516-73bc-4055-b2bc-7c876653246e',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Pão de Batata',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'dfb38a7e-1819-4ab9-be8a-cfeb515e21fa',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Hamburgão',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'ec24f1ed-6e49-4774-8a3f-7485c822129d',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Baguete Folhada',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'f9adc29e-ac77-4282-9811-9a1386309f52',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Pão na Chapa',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'e60da0e3-cc8b-4a56-968b-1f2403991f94',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':11.0,
                'name':'Pão c/ requeijão',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'6561df65-ed3e-4e01-824d-73d46f2c92ec',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Mini Pizza',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'4331e442-36f7-40d7-b646-281a4f7828b2',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':24.0,
                'name':'Salada / F. Frango',
                'description':'Filé de Frango - Mussarela/Alface/Tomate/Batata Frita/No Prato',
                'meal_type':'SALADS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'c169a479-bcb9-4c34-8a48-aafb26010f2b',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':27.0,
                'name':'Salada / C. Filé',
                'description':'Contra Filé - Mussarela/Alface/Tomate/Batata Frita/No Prato',
                'meal_type':'SALADS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'352683c8-ad7f-47ef-8d3b-ac6b9eaa157e',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':21.0,
                'name':'Salada / Calabresa',
                'description':'Calabresa - Mussarela/Alface/Tomate/Batata Frita/No Prato',
                'meal_type':'SALADS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'02218ac2-88bd-4771-9910-a44ec1aa361f',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':10.0,
                'name':'Salada Simples',
                'description':'Alface/Tomate/No Prato',
                'meal_type':'SALADS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'88b73f96-8522-4446-9be9-e2db78293b7c',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':26.0,
                'name':'Omelete c/ Salada',
                'description':'Ovo/Alface/Tomate/No Prato',
                'meal_type':'SALADS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'19c2527b-68f8-40db-ad4e-cad69ecd9abd',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':28.0,
                'name':'Lasanha',
                'description':'Massa - Mussarela/Presunto/Molho ao sugo',
                'meal_type':'SALADS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'5a39d0ee-06da-4abf-9fc1-40d25bea19e0',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':14.0,
                'name':'Fritas Pequenas',
                'description':'',
                'meal_type':'PORTIONS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'13079a73-f8bf-4e5a-bbb2-a867fbb89a71',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':18.0,
                'name':'Fritas Médias',
                'description':'',
                'meal_type':'PORTIONS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'2d852439-a960-463a-aac9-482ed5274319',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':22.0,
                'name':'Fritas Gde Simples',
                'description':'',
                'meal_type':'PORTIONS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'82c875f0-378a-4996-89cd-231311c093fb',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':30.0,
                'name':'Fritas Gde Completa',
                'description':'',
                'meal_type':'PORTIONS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'d35310a1-d48b-4bb0-bbe5-710f544d2669',
                'last_update':1674835337393,
                'prepare_time':20
            },
            {
                'available':True,
                'price':16.0,
                'name':'calabresa Acebol.',
                'description':'',
                'meal_type':'PORTIONS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'6d6b38c0-927d-4c43-93b7-b33ea9278cba',
                'last_update':1674835337393,
                'prepare_time':20
            }
        ],
        'HORA_H':[
            {
                'available':True,
                'price':29.0,
                'name':'Nuggets (6 unid.)',
                'description':'Este prato inclui 2 acompanhamentos:\nArroz Feijão, Arroz a Grega, Arroz Integral, Creme de Milho, Mix Legumes, Purê de Batata, Salada Folhas, Salada de Tomate e Queijo Branco Temperado, Salada de Maionese, Salada de Couve com Tomate e Cebola, Batata Frita, Polenta Frita, Mandioca Frita, Beringela Caponata, Abobrinha Refogada',
                'meal_type':'PORTIONS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'71ede2ce-31c6-4b22-bab5-da2175654308',
                'last_update':1677722948,
                'prepare_time':None
            },
            {
                'available':True,
                'price':32.0,
                'name':'Filé de Frango (Grelhado)',
                'description':'Este prato inclui 2 acompanhamentos:\nArroz Feijão, Arroz a Grega, Arroz Integral, Creme de Milho, Mix Legumes, Purê de Batata, Salada Folhas, Salada de Tomate e Queijo Branco Temperado, Salada de Maionese, Salada de Couve com Tomate e Cebola, Batata Frita, Polenta Frita, Mandioca Frita, Beringela Caponata, Abobrinha Refogada',
                'meal_type':'PLATES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'f78a4ce5-607e-41cf-8175-f9bbd0498d7c',
                'last_update':1677722948,
                'prepare_time':None
            },
            {
                'available':True,
                'price':32.0,
                'name':'Omelete de Presunto',
                'description':'Este prato inclui 2 acompanhamentos:\nArroz Feijão, Arroz a Grega, Arroz Integral, Creme de Milho, Mix Legumes, Purê de Batata, Salada Folhas, Salada de Tomate e Queijo Branco Temperado, Salada de Maionese, Salada de Couve com Tomate e Cebola, Batata Frita, Polenta Frita, Mandioca Frita, Beringela Caponata, Abobrinha Refogada',
                'meal_type':'PLATES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'118cd9d3-95f0-4c1a-8052-39e1a9049e38',
                'last_update':1677722948,
                'prepare_time':None
            },
            {
                'available':True,
                'price':32.0,
                'name':'Omelete de Queijo',
                'description':'Este prato inclui 2 acompanhamentos:\nArroz Feijão, Arroz a Grega, Arroz Integral, Creme de Milho, Mix Legumes, Purê de Batata, Salada Folhas, Salada de Tomate e Queijo Branco Temperado, Salada de Maionese, Salada de Couve com Tomate e Cebola, Batata Frita, Polenta Frita, Mandioca Frita, Beringela Caponata, Abobrinha Refogada',
                'meal_type':'PLATES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'ef65bef3-6c2a-42dc-baae-2b9636ad810e',
                'last_update':1677722948,
                'prepare_time':None
            },
            {
                'available':True,
                'price':32.0,
                'name':'Omelete de Tomate',
                'description':'Este prato inclui 2 acompanhamentos:\nArroz Feijão, Arroz a Grega, Arroz Integral, Creme de Milho, Mix Legumes, Purê de Batata, Salada Folhas, Salada de Tomate e Queijo Branco Temperado, Salada de Maionese, Salada de Couve com Tomate e Cebola, Batata Frita, Polenta Frita, Mandioca Frita, Beringela Caponata, Abobrinha Refogada',
                'meal_type':'PLATES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'084900c3-6b23-46f6-bcb6-94d224d35253',
                'last_update':1677722948,
                'prepare_time':None
            },
            {
                'available':True,
                'price':38.0,
                'name':'Contra Filé (Grelhado)',
                'description':'Este prato inclui 2 acompanhamentos:\nArroz Feijão, Arroz a Grega, Arroz Integral, Creme de Milho, Mix Legumes, Purê de Batata, Salada Folhas, Salada de Tomate e Queijo Branco Temperado, Salada de Maionese, Salada de Couve com Tomate e Cebola, Batata Frita, Polenta Frita, Mandioca Frita, Beringela Caponata, Abobrinha Refogada',
                'meal_type':'PLATES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'21177333-ac07-4359-b47a-00f1e09d2659',
                'last_update':1677722948,
                'prepare_time':None
            },
            {
                'available':True,
                'price':32.0,
                'name':'Calabresa Grelhada (Toscana Aurora)',
                'description':'Este prato inclui 2 acompanhamentos:\nArroz Feijão, Arroz a Grega, Arroz Integral, Creme de Milho, Mix Legumes, Purê de Batata, Salada Folhas, Salada de Tomate e Queijo Branco Temperado, Salada de Maionese, Salada de Couve com Tomate e Cebola, Batata Frita, Polenta Frita, Mandioca Frita, Beringela Caponata, Abobrinha Refogada',
                'meal_type':'PLATES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'850fe1d7-13df-430f-949f-4d106df70db4',
                'last_update':1677722948,
                'prepare_time':None
            },
            {
                'available':True,
                'price':35.0,
                'name':'Parmegiana de Frango (Molho de tomate caseiro)',
                'description':'Este prato inclui 2 acompanhamentos:\nArroz Feijão, Arroz a Grega, Arroz Integral, Creme de Milho, Mix Legumes, Purê de Batata, Salada Folhas, Salada de Tomate e Queijo Branco Temperado, Salada de Maionese, Salada de Couve com Tomate e Cebola, Batata Frita, Polenta Frita, Mandioca Frita, Beringela Caponata, Abobrinha Refogada',
                'meal_type':'PLATES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'e11b090e-a275-4474-ae90-2126b3d3a165',
                'last_update':1677722948,
                'prepare_time':None
            },
            {
                'available':True,
                'price':39.0,
                'name':'Parmegiana de Carne (Molho de tomate caseiro)',
                'description':'Este prato inclui 2 acompanhamentos:\nArroz Feijão, Arroz a Grega, Arroz Integral, Creme de Milho, Mix Legumes, Purê de Batata, Salada Folhas, Salada de Tomate e Queijo Branco Temperado, Salada de Maionese, Salada de Couve com Tomate e Cebola, Batata Frita, Polenta Frita, Mandioca Frita, Beringela Caponata, Abobrinha Refogada',
                'meal_type':'PLATES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'7a425df8-6d4d-4f3a-b69b-3ae9b7c6ab96',
                'last_update':1677722948,
                'prepare_time':None
            },
            {
                'available':True,
                'price':33.0,
                'name':'Strogonoff de Frango',
                'description':'Este prato inclui 2 acompanhamentos:\nArroz Feijão, Arroz a Grega, Arroz Integral, Creme de Milho, Mix Legumes, Purê de Batata, Salada Folhas, Salada de Tomate e Queijo Branco Temperado, Salada de Maionese, Salada de Couve com Tomate e Cebola, Batata Frita, Polenta Frita, Mandioca Frita, Beringela Caponata, Abobrinha Refogada',
                'meal_type':'PLATES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'c2b0e3de-02d0-483c-b8ce-1383c24bed60',
                'last_update':1677722948,
                'prepare_time':None
            },
            {
                'available':True,
                'price':36.0,
                'name':'Strogonoff de Carne',
                'description':'Este prato inclui 2 acompanhamentos:\nArroz Feijão, Arroz a Grega, Arroz Integral, Creme de Milho, Mix Legumes, Purê de Batata, Salada Folhas, Salada de Tomate e Queijo Branco Temperado, Salada de Maionese, Salada de Couve com Tomate e Cebola, Batata Frita, Polenta Frita, Mandioca Frita, Beringela Caponata, Abobrinha Refogada',
                'meal_type':'PLATES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'384ce447-76ad-462d-b8cd-79f93f92b5f3',
                'last_update':1677722948,
                'prepare_time':None
            },
            {
                'available':True,
                'price':38.0,
                'name':'Peixe a Dore (Pescada Branca)',
                'description':'Este prato inclui 2 acompanhamentos:\nArroz Feijão, Arroz a Grega, Arroz Integral, Creme de Milho, Mix Legumes, Purê de Batata, Salada Folhas, Salada de Tomate e Queijo Branco Temperado, Salada de Maionese, Salada de Couve com Tomate e Cebola, Batata Frita, Polenta Frita, Mandioca Frita, Beringela Caponata, Abobrinha Refogada',
                'meal_type':'PLATES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'04a65d3f-a7f7-4161-ac7b-50d139946d2e',
                'last_update':1677722948,
                'prepare_time':None
            },
            {
                'available':True,
                'price':45.0,
                'name':'Filé Mignon',
                'description':'Este prato inclui 2 acompanhamentos:\nArroz Feijão, Arroz a Grega, Arroz Integral, Creme de Milho, Mix Legumes, Purê de Batata, Salada Folhas, Salada de Tomate e Queijo Branco Temperado, Salada de Maionese, Salada de Couve com Tomate e Cebola, Batata Frita, Polenta Frita, Mandioca Frita, Beringela Caponata, Abobrinha Refogada',
                'meal_type':'PLATES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':'5569bd1d-21ed-4846-a3aa-4157beb11147',
                'last_update':1677722948,
                'prepare_time':None
            }
        ],
        'message':'the products were retrieved'
        }

          
          
        assert response["statusCode"] == 200
        assert json.loads(response["body"])["message"] == "the products were retrieved"
        assert json.loads(response["body"]) == expected