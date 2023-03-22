import boto3

from src.shared.infra.repositories.product_repository_dynamo import ProductRepositoryDynamo
from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock

def setup_dynamo_table():
    print('Setting up dynamo table...')
    dynamo_client = boto3.client('dynamodb', endpoint_url='http://localhost:8000', region_name='sa-east-1')
    tables = dynamo_client.list_tables()['TableNames']

    if not tables:
        print('Creating table...')
        dynamo_client.create_table(
            TableName="mf_mss_product-table",
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
            ],
            BillingMode='PAY_PER_REQUEST',
        )
        print('Table "mf_product-table" created!\n')
    else:
        print('Table already exists!\n')

def load_mock_to_local_dynamo():
    repo_dynamo = ProductRepositoryDynamo()
    repo_mock = ProductRepositoryMock()

    print('Loading mock data to dynamo...')

    print('Loading products...')
    count = 0
    for product in repo_mock.products:
        print(f'Loading product {product.product_id} | {product.restaurant} | {product.name}...')
        repo_dynamo.create_product(new_product=product)
        count += 1
    print(f'{count} products loaded!\n')

    print('Done!')

if __name__ == '__main__':
    setup_dynamo_table()
    load_mock_to_local_dynamo()