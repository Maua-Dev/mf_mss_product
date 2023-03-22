import boto3

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

if __name__ == '__main__':
    setup_dynamo_table()