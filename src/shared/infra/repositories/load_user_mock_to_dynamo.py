import boto3

from src.shared.infra.repositories.user_repository_dynamo import UserRepositoryDynamo
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

def setup_dynamo_table():
    print('Setting up dynamo table...')
    dynamo_client = boto3.client('dynamodb', endpoint_url='http://localhost:8000', region_name='sa-east-1')
    tables = dynamo_client.list_tables()['TableNames']
    table_name = "mf_mss_user-table" 
    
    if not table_name in tables:
        print('Creating table...')
        dynamo_client.create_table(
            TableName="mf_mss_user-table",
            KeySchema=[
                {
                    'AttributeName': 'PK',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'PK',
                    'AttributeType': 'S'
                },
            ],
            BillingMode='PAY_PER_REQUEST',
        )
        print('Table "mf_user-table" created!\n')
    else:
        print('Table already exists!\n')

def load_mock_to_local_dynamo():
    repo_dynamo = UserRepositoryDynamo()
    repo_mock = UserRepositoryMock()

    print('Loading mock data to dynamo...')

    print('Loading users...')
    count = 0
    for user in repo_mock.users_list:
        print(f'Loading users {user.name} | {user.email} | {user.role}...')
        repo_dynamo.create_user(user)
        count += 1
    print(f'{count} users loaded!\n')

    print('Done!')

if __name__ == '__main__':
    setup_dynamo_table()
    load_mock_to_local_dynamo()