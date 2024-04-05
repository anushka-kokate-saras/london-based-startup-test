import json
import boto3
dynamodb = boto3.resource('dynamodb')
import time
from datetime import datetime

table = dynamodb.Table('startup-test')
def lambda_handler(event, context):
    # TODO implement
    print(event)
    requestBody = json.loads(event["body"])
    print(requestBody)
    table.put_item(
    Item={
        'pk': 'users',
        'sk': requestBody["email"] + '#' + str(int(round(time.time()))),
        'text': requestBody["text"],
        'datetime': datetime.now().isoformat(timespec='seconds')
    }
)
    return {
        'statusCode': 200,
        'body': json.dumps('Msg sent')
    }
