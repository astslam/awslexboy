response = client.update_item(
    TableName='string',
    Key={
        'ApptID':userID,
    },
    AttributeUpdates={
        'ApptStatus' : 'CANCELED',
        'ApptTime': appointment_time
            'Value': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            },
            'Action': 'ADD'|'PUT'|'DELETE'
        }
    },
    Expected={
        'string': {
            'Value': {
                'S': 'string',
                'N': 'string',
                'B': b'bytes',
                'SS': [
                    'string',
                ],
                'NS': [
                    'string',
                ],
                'BS': [
                    b'bytes',
                ],
                'M': {
                    'string': {'... recursive ...'}
                },
                'L': [
                    {'... recursive ...'},
                ],
                'NULL': True|False,
                'BOOL': True|False
            },
            'Exists': True|False,
            'ComparisonOperator': 'EQ'|'NE'|'IN'|'LE'|'LT'|'GE'|'GT'|'BETWEEN'|'NOT_NULL'|'NULL'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH',
            'AttributeValueList': [
                {
                    'S': 'string',
                    'N': 'string',
                    'B': b'bytes',
                    'SS': [
                        'string',
                    ],
                    'NS': [
                        'string',
                    ],
                    'BS': [
                        b'bytes',
                    ],
                    'M': {
                        'string': {'... recursive ...'}
                    },
                    'L': [
                        {'... recursive ...'},
                    ],
                    'NULL': True|False,
                    'BOOL': True|False
                },
            ]
        }
    },
    ConditionalOperator='AND'|'OR',
    ReturnValues='NONE'|'ALL_OLD'|'UPDATED_OLD'|'ALL_NEW'|'UPDATED_NEW',
    ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
    ReturnItemCollectionMetrics='SIZE'|'NONE',
    UpdateExpression='string',
    ConditionExpression='string',
    ExpressionAttributeNames={
        'string': 'string'
    },
    ExpressionAttributeValues={
        'string': {
            'S': 'string',
            'N': 'string',
            'B': b'bytes',
            'SS': [
                'string',
            ],
            'NS': [
                'string',
            ],
            'BS': [
                b'bytes',
            ],
            'M': {
                'string': {'... recursive ...'}
            },
            'L': [
                {'... recursive ...'},
            ],
            'NULL': True|False,
            'BOOL': True|False
        }
    }
)

response = client.update_item(
    ExpressionAttributeNames={
        '#AT': 'ApptType',
        '#D': 'ApptDate',
        '#T': 'ApptTime'
    },
    ExpressionAttributeValues={
        ':t': {
            'S': '11:00',#''Louder Than Ever',
        },
        ':d': {
            'S': '2019-01-01',
        },
    },
    Key={
        'ApptId' : {
            'S' : userId,
        },
    },
    ReturnValues='ALL_NEW',
    TableName='ApptbotTime',
    UpdateExpression='SET #D = :y, #AT = :t',
)

print(response)

# response = client.update_item(
#     TableName='string',
#     Key={
#         'string': {
#             'S': 'string',
#             'N': 'string',
#             'B': b'bytes',
#             'SS': [
#                 'string',
#             ],
#             'NS': [
#                 'string',
#             ],
#             'BS': [
#                 b'bytes',
#             ],
#             'M': {
#                 'string': {'... recursive ...'}
#             },
#             'L': [
#                 {'... recursive ...'},
#             ],
#             'NULL': True|False,
#             'BOOL': True|False
#         }
#     },
#     AttributeUpdates={
#         'string': {
#             'Value': {
#                 'S': 'string',
#                 'N': 'string',
#                 'B': b'bytes',
#                 'SS': [
#                     'string',
#                 ],
#                 'NS': [
#                     'string',
#                 ],
#                 'BS': [
#                     b'bytes',
#                 ],
#                 'M': {
#                     'string': {'... recursive ...'}
#                 },
#                 'L': [
#                     {'... recursive ...'},
#                 ],
#                 'NULL': True|False,
#                 'BOOL': True|False
#             },
#             'Action': 'ADD'|'PUT'|'DELETE'
#         }
#     },
#     Expected={
#         'string': {
#             'Value': {
#                 'S': 'string',
#                 'N': 'string',
#                 'B': b'bytes',
#                 'SS': [
#                     'string',
#                 ],
#                 'NS': [
#                     'string',
#                 ],
#                 'BS': [
#                     b'bytes',
#                 ],
#                 'M': {
#                     'string': {'... recursive ...'}
#                 },
#                 'L': [
#                     {'... recursive ...'},
#                 ],
#                 'NULL': True|False,
#                 'BOOL': True|False
#             },
#             'Exists': True|False,
#             'ComparisonOperator': 'EQ'|'NE'|'IN'|'LE'|'LT'|'GE'|'GT'|'BETWEEN'|'NOT_NULL'|'NULL'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH',
#             'AttributeValueList': [
#                 {
#                     'S': 'string',
#                     'N': 'string',
#                     'B': b'bytes',
#                     'SS': [
#                         'string',
#                     ],
#                     'NS': [
#                         'string',
#                     ],
#                     'BS': [
#                         b'bytes',
#                     ],
#                     'M': {
#                         'string': {'... recursive ...'}
#                     },
#                     'L': [
#                         {'... recursive ...'},
#                     ],
#                     'NULL': True|False,
#                     'BOOL': True|False
#                 },
#             ]
#         }
#     },
#     ConditionalOperator='AND'|'OR',
#     ReturnValues='NONE'|'ALL_OLD'|'UPDATED_OLD'|'ALL_NEW'|'UPDATED_NEW',
#     ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
#     ReturnItemCollectionMetrics='SIZE'|'NONE',
#     UpdateExpression='string',
#     ConditionExpression='string',
#     ExpressionAttributeNames={
#         'string': 'string'
#     },
#     ExpressionAttributeValues={
#         'string': {
#             'S': 'string',
#             'N': 'string',
#             'B': b'bytes',
#             'SS': [
#                 'string',
#             ],
#             'NS': [
#                 'string',
#             ],
#             'BS': [
#                 b'bytes',
#             ],
#             'M': {
#                 'string': {'... recursive ...'}
#             },
#             'L': [
#                 {'... recursive ...'},
#             ],
#             'NULL': True|False,
#             'BOOL': True|False
#         }
#     }
# )