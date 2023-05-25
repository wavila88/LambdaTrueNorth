import json
from callRandom import callRandomMethod

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': callRandomMethod()
    }
