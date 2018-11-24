import boto3
import uuid
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.create_table(
    TableName='mydynamodb-'+format(uuid.uuid4()),
    KeySchema=[
        {
            'AttributeName': 'station_id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'dateandtime',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'station_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'dateandtime',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

print("Table status:", table.table_status)
