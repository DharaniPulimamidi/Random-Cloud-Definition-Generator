import json
import random
import boto3
from boto3.dynamodb.conditions import Key

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Name of your DynamoDB table
table_name = 'CloudDefinitions'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Fetch all cloud definitions from DynamoDB
        response = table.scan()
        items = response.get('Items', [])
        
        if not items:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'No definitions found.'}),
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            }
        
        # Pick a random cloud definition
        random_definition = random.choice(items)
        definition_text = random_definition.get('definition', 'No definition available')

        # Return the random definition
        return {
            'statusCode': 200,
            'body': json.dumps({'definition': definition_text}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

    except Exception as e:
        # Handle any errors that occur
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
