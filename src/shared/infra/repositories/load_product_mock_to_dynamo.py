import boto3
from src.shared.infra.repositories.order_repository_dynamo import OrderRepositoryDynamo
from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock

from src.shared.infra.repositories.product_repository_dynamo import ProductRepositoryDynamo
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock

def setup_dynamo_table():
    print('Setting up dynamo table...')
    dynamo_client = boto3.client('dynamodb', endpoint_url='http://localhost:8000', region_name='sa-east-1')
    tables = dynamo_client.list_tables()['TableNames']
    table_name = "mf_mss_product-table"

    if not table_name in tables:
        print('Creating table...')
        dynamo_client.create_table(
            TableName= table_name,
            KeySchema=[
                {
                    'AttributeName': 'PK',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'SK',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'PK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'SK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'GSI1-PK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'GSI1-SK',
                    'AttributeType': 'S'
                }
            ],
            BillingMode='PAY_PER_REQUEST',
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'GSI1',
                    'KeySchema': [
                        {
                            'AttributeName': 'GSI1-PK',
                            'KeyType': 'HASH'
                        },
                        {
                            'AttributeName': 'GSI1-SK',
                            'KeyType': 'RANGE'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    }
                }
            ]
        )
        print('Table "mf_product-table" created!\n')
    else:
        print('Table already exists!\n')

def load_mock_to_local_dynamo():
    repo_product_dynamo = ProductRepositoryDynamo()
    repo_product_mock = ProductRepositoryMock()
    repo_order_dynamo = OrderRepositoryDynamo()
    repo_order_mock = OrderRepositoryMock()

    print('Loading mock data to dynamo...')

    print('Loading products...')
    count = 0
    for product in repo_product_mock.products:
        print(f'Loading product {product.product_id} | {product.restaurant} | {product.name}...')
        repo_product_dynamo.create_product(new_product=product)
        count += 1
    print(f'{count} products loaded!\n')

    print('Loading orders...')
    for order in repo_order_mock.orders:
        print(f'Loading order {order.order_id} | {order.products} | {order.restaurant}...')
        repo_order_dynamo.create_order(order=order)
        count += 1
    print(f'{count} orders loaded!\n')

    print('Loading connections...')
    for connection in repo_order_mock.connections:
        print(f'Loading connection {connection.connection_id} | {connection.user_id} | {connection.restaurant}...')
        repo_order_dynamo.create_connection(connection=connection)
        count += 1
    print(f'{count} connections loaded!\n')

    print('Done!')

if __name__ == '__main__':
    setup_dynamo_table()
    load_mock_to_local_dynamo()