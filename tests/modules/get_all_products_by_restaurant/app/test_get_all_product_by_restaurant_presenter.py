import json
from src.modules.get_all_products_by_restaurant.app.get_all_product_by_restaurant_presenter import lambda_handler


class Test_GetAllProductByRestaurantPresenter:
    def test_get_all_products_by_restaurant_presenter(self):

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
            "restaurant": "SOUZA_DE_ABREU"
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

        expected =  {
            
        'all_products':[
            {
                'available':True,
                'price':14.0,
                'name':'Lanche Mortadela',
                'description':'Mortadela',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':0,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':16.0,
                'name':'X-Salada',
                'description':'Hamburguer/Mussarela/Maionese/Alface/Tomate',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':1,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'X-Burguer',
                'description':'Hamburguer/Mussarela/Maionese',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':2,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':18.0,
                'name':'X-Bacon',
                'description':'Hamburguer/Bacon/Mussarela/Maionese/Alface/Tomate',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':3,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':15.0,
                'name':'X-Egg',
                'description':'Hamburguer/Ovo/Mussarela/Maionese/Alface/Tomate',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':4,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':18.0,
                'name':'X-Calabresa',
                'description':'Calabresa/Mussarela/Alface/Tomate',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':5,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':18.0,
                'name':'X-Frango',
                'description':'Filé de Frango/Mussarela/Maionese/Alface/Tomate',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':6,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':16.0,
                'name':'Americano',
                'description':'Presunto/Ovo/Mussarela/Maionese/Alface/Tomate/Orégano',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':7,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':12.0,
                'name':'Misto Quente',
                'description':'Presunto/Mussarela/Orégano',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':8,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':13.0,
                'name':'Bauru',
                'description':'Presunto/Mussarela/Tomate/Orégano',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':9,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':18.0,
                'name':'Churrasco',
                'description':'Contra Filé',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':10,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':21.0,
                'name':'Ch. c/ Queijo',
                'description':'Contra Filé/Mussarela',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':11,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':23.0,
                'name':'Ch. c/ Vinag.',
                'description':'Contra Filé/Vinagrete',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':12,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':25.0,
                'name':'Ch. c/ Queijo/Vinag.',
                'description':'Contra Filé/Mussarela/Vinagrete',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':13,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':17.0,
                'name':'Mort. c/ Mussarela',
                'description':'Mortadela/Mussarela',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':14,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':14.0,
                'name':'Lanche Natural',
                'description':'Peito de Peru/Mussarela/Alface/Tomate',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':15,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':26.0,
                'name':'X-Tudo',
                'description':'2x Hamurguer/Ovo/Presunto/Calabresa/Bacon/Mussarela/Maionese/Alface/Tomate',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':16,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':20.0,
                'name':'Vasco de Frango',
                'description':'Filé de Frango/Batata Palha/Catupiry/Mussarela',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':17,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':23.0,
                'name':'Vasco de Carne',
                'description':'Contra Filé/Batata Palha/Catupiry/Mussarela',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':18,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':19.0,
                'name':'Vasco de Calabresa',
                'description':'Calabresa/Batata Palha/Catupiry/Mussarela',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':19,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'Pão c/ Ovo',
                'description':'Ovo',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':20,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':11.0,
                'name':'Pão c/ Ovo/Mussar.',
                'description':'Ovo/Mussarela/Orégano',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':21,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':14.0,
                'name':'Misto/Batata Palha',
                'description':'Presunto/Batata Palha/Mussarela/Orégano',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':22,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':25.0,
                'name':'Beirute Carne I',
                'description':'Carne/Alface/Tomate/Mussarela/Ovo',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':23,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':28.0,
                'name':'Beirute Carne II',
                'description':'Carne/Alface/Tomate/Mussarela/Ovo/Bacon/Cheddar',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':24,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':24.0,
                'name':'Beirute Frango',
                'description':'Frango/Alface/Tomate/Mussarela/Ovo',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':25,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':22.0,
                'name':'Beirute Calabresa',
                'description':'Calabresa/Alface/Tomate/Mussarela/Ovo',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':26,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'Cone Trufado',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':27,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':14.0,
                'name':'Bolo de Pote',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':28,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'Brigadeiro',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':29,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':4.0,
                'name':'Sonho de Valsa',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':30,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':6.0,
                'name':'Barra de Cereais',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':31,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':6.0,
                'name':'Chocolates',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':32,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':3.0,
                'name':'Paçoquita',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':33,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':6.0,
                'name':'Trident',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':34,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':5.0,
                'name':'Halls',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':35,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':0.0,
                'name':'Sorvetes',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':36,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':13.0,
                'name':'Salada de Fruta',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':37,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':17.0,
                'name':'Açaí',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':38,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':13.0,
                'name':'Gelatina Colorida',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':39,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':18.0,
                'name':'Copo da Felicidade',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':40,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':15.0,
                'name':'Musse/Chocolate',
                'description':'',
                'meal_type':'CANDIES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':41,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':0.0,
                'name':'Queijo Quente 01',
                'description':'Mussarela/Tomate/Orégano/No Prato',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':42,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':0.0,
                'name':'Queijo Quente 02',
                'description':'Queijo Brancp/Tomate/Orégano/No Prato',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':43,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':0.0,
                'name':'Queijo Quente 03',
                'description':'Queijo Brancp/Tomate Seco/Orégano/No Prato',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':44,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':0.0,
                'name':'Prima',
                'description':'Contra Filé/Bacon/Cheddar/Catupiry/Batata Palha/No Prato',
                'meal_type':'SANDWICHES',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':45,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Refrigerante Lata',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':46,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'Tônica Schweppes',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':47,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'Suco Lata',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':48,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'H2O',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':49,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'Chá - Lata',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':50,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':15.0,
                'name':'Energético',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':51,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':6.0,
                'name':'Água c/ Gás',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':52,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':5.0,
                'name':'Água s/ Gás',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':53,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':9.0,
                'name':'Suco de Laranja',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':54,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':11.0,
                'name':'Suco de Melância',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':55,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':11.0,
                'name':'Suco Misto | Polpa',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':56,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':6.0,
                'name':'Toddynho',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':57,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':11.0,
                'name':'Vitamina Mista',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':58,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':9.0,
                'name':'Gatorade',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':59,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':8.0,
                'name':'Guaraviton',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':60,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':11.0,
                'name':'Chocolate Batido',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':61,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':6.5,
                'name':'Café - peq.',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':62,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':7.5,
                'name':'Café - gde.',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':63,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Capuccino - peq.',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':64,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':9.0,
                'name':'Capuccino - gde.',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':65,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Chocolate - peq.',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':66,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':9.0,
                'name':'Chocolate - gde.',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':67,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':5.0,
                'name':'Chá Quente',
                'description':'',
                'meal_type':'DRINKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':68,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Pão de Queijo',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':69,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Coxinha',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':70,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Esfihas',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':71,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Folhadinhos',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':72,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':11.0,
                'name':'Quiche',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':73,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':9.0,
                'name':'Empada',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':74,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Bauruzinho',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':75,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Pão de Batata',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':76,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Hamburgão',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':77,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Baguete Folhada',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':78,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Pão na Chapa',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':79,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':11.0,
                'name':'Pão c/ requeijão',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':80,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':7.0,
                'name':'Mini Pizza',
                'description':'',
                'meal_type':'SNACKS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':81,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':24.0,
                'name':'Salada / F. Frango',
                'description':'Filé de Frango - Mussarela/Alface/Tomate/Batata Frita/No Prato',
                'meal_type':'SALADS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':82,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':27.0,
                'name':'Salada / C. Filé',
                'description':'Contra Filé - Mussarela/Alface/Tomate/Batata Frita/No Prato',
                'meal_type':'SALADS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':83,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':21.0,
                'name':'Salada / Calabresa',
                'description':'Calabresa - Mussarela/Alface/Tomate/Batata Frita/No Prato',
                'meal_type':'SALADS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':84,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':10.0,
                'name':'Salada Simples',
                'description':'Alface/Tomate/No Prato',
                'meal_type':'SALADS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':85,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':26.0,
                'name':'Omelete c/ Salada',
                'description':'Ovo/Alface/Tomate/No Prato',
                'meal_type':'SALADS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':86,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':28.0,
                'name':'Lasanha',
                'description':'Massa - Mussarela/Presunto/Molho ao sugo',
                'meal_type':'SALADS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':87,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':14.0,
                'name':'Fritas Pequenas',
                'description':'',
                'meal_type':'PORTIONS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':88,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':18.0,
                'name':'Fritas Médias',
                'description':'',
                'meal_type':'PORTIONS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':89,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':22.0,
                'name':'Fritas Gde Simples',
                'description':'',
                'meal_type':'PORTIONS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':90,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':30.0,
                'name':'Fritas Gde Completa',
                'description':'',
                'meal_type':'PORTIONS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':91,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            },
            {
                'available':True,
                'price':16.0,
                'name':'calabresa Acebol.',
                'description':'',
                'meal_type':'PORTIONS',
                'photo':'https://avatars.githubusercontent.com/u/30812461?v=4',
                'product_id':92,
                'last_update':1674835337393,
                'restaurant':'SOUZA_DE_ABREU',
                'prepareTime':20
            }
        ],
        'message':'the products were retrieved'
        }
        
    
        assert response["statusCode"] == 200
        assert json.loads(response['body']) == expected
    
    def test_get_all_products_by_restaurant_presenter_restaurant_is_missing(self):
      
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
        
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field restaurant is missing"

    def test_get_all_products_by_restaurant_presenter_invalid_restaurant(self):
        
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
              "restaurant": "2"
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
          
          assert response["statusCode"] == 400
          assert json.loads(response["body"]) == "Field restaurant is not valid"