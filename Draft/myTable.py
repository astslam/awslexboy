# def querydb():
#     dynamodb = boto3.resource('dynamodb')
#     table = dynamodb.Table('mytable')
#     return DynamoDBVersion

from __future__ import print_function  # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr


# def lambda_handler(event, context):
#     # TODO implement
#         return 'Hello from Lambda'

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')

table = dynamodb.Table('Table')

print("print Table")

# response = table.query(
#     KeyConditionExpression=Key('UID').eq(1)
# )

# for i in response['Items']:
# #     print(i['Date'], ":", i['title'])
# # for i in response['Items']:
#     print(json.dumps(i, cls=DecimalEncoder))


response = table.get_item(
    Key={
        'UID': 'aws'
    }
)

item = response['Item']
print(item)
