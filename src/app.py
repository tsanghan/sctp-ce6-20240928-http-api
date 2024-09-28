import boto3
import os
import json
import logging
import base64

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):
  table = os.environ.get('DDB_TABLE')
  logging.info(f"## Loaded table name from environemt variable DDB_TABLE: {table}")
  if event["body"]:
      # item = json.loads(event["body"])
      item = json.loads(base64.b64decode(event['body']).decode('utf-8'))
      logging.info(f"## Received payload: {item}")
      year = str(item["year"])
      title = str(item["title"])
      dynamodb_client.put_item(TableName=table,Item={"year": {'N':year}, "title": {'S':title}})
      message = "Successfully inserted data!"
      return {
          "statusCode": 200,
          "headers": {
              "Content-Type": "application/json"
          },
          "body": json.dumps({"message": message})
      }
  else:
      logging.info("## Received request without a payload")
      dynamodb_client.put_item(TableName=table,Item={"year": {'N':'2012'}, "title": {'S':'The Amazing Spider-Man 2'}})
      message = "Successfully inserted data!"
      return {
          "statusCode": 200,
          "headers": {
              "Content-Type": "application/json"
          },
          "body": json.dumps({"message": message})
      }