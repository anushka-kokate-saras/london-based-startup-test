import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    token_email = event["requestContext"]["authorizer"]["claims"]["email"]
    params_email = event["queryStringParameters"]["email"]
    if token_email == params_email:
        response = client.query(
            TableName='startup-test',
            KeyConditionExpression='pk = :pk_val AND begins_with(sk, :sk_val)',
            ExpressionAttributeValues={
                ':pk_val': {'S': 'users'},
                ':sk_val': {'S': params_email},
            }
        )
    else:
        response = {"message": "User does not exists"}
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
