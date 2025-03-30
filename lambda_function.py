import json

def lambda_handler(event, context):
    body = "Welcome to AWS Complete Bootcamp!"
    statusCode = 200
    return {
        "statusCode": statusCode,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json"
        }
    }
