import json
import urllib.request
import urllib.parse
import logging
import os
from dotenv import load_dotenv
import boto3
import pytz
from datetime import datetime

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

# Load environment variables from the Lambda environment
load_dotenv()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Retrieve the keys from environment variables
PUSHOVER_USER_KEY = os.getenv('PUSHOVER_USER_KEY')
PUSHOVER_API_TOKEN = os.getenv('PUSHOVER_API_TOKEN')

def lambda_handler(event, context):
    logger.info(f"Event received: {json.dumps(event)}")

    try:
        # Parse the incoming request body
        body = event['body']

        # Construct the message for Pushover
        words = body.split()
        emoji_map = {
            "buy": "🟢😎🟢",
            "sell": "🔴😡🔴"
        }
        word_map = {
            "buy": '<font color="#00ff00">Long</font>',
            "sell": '<font color="#ff0000">Short</font>'
        }

        if words:
            # Check if the first word matches a key in the emoji_map
            if words[0].lower() in emoji_map:
                second_word_part = words[1] if len(words) > 1 else ''
                title = f"{emoji_map[words[0].lower()]} {second_word_part}"
                words[0] = word_map[words[0].lower()]
            else:
                second_word_part = words[1] if len(words) > 1 else ''
                title = f"{words[0].upper()} {second_word_part}"
                words[0] = words[0].upper()  # Capitalize the first word if not in emoji_map

        # Prepare Data for DynamoDB
        # Extract the values from the body
        ticker_name = words[1]
        time_interval = words[2].split('@')[1] if '@' in words[2] else ''
        alert_price = words[3].split('$')[1] if '$' in words [3] else ''
        alert_time_str = words[4].split('#')[1] if '#' in words [4] else ''
        #atr_range = next((word.split(':')[1] for word in words if word.startswith('Range:')), '')
        atr_range = words[5].split(':')[1] if '*' in words[5] else ''


        #Convert alert_time to UTC
        try:
            alert_time = datetime.strptime(alert_time_str, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.utc)

        #Convert to EST
            est = pytz.timezone('US/Eastern')
            alert_time_est = alert_time.astimezone(est)
            alert_time_est_timestamp = int(alert_time_est.timestamp())
            alert_time_est_formatted = alert_time_est.strftime('%I:%M %p')
        except ValueError:
            alert_time_est_timestamp = None
            alert_time_est_formatted = alert_time_str

        # Convert time_interval to seconds
        if time_interval.endswith('S'):
            time_interval_seconds = int(time_interval[:-1])
        else:
            time_interval_seconds = int(time_interval) * 60  # Interval without S is in minutes


        # Construct the item to store in DynamoDB
        item = {
        'alert_id': {'S': context.aws_request_id},
        'ticker_name': {'S': ticker_name},
        'time_interval': {'N': str(time_interval_seconds)},  # Storing as number
        'alert_price': {'N': str(alert_price)},
        'time_stamp': {'N': str(alert_time_est_timestamp) if alert_time_est_timestamp is not None else {'NULL': True}},
        'time_est': {'S': str(alert_time_est)},
        'atr_range': {'S': atr_range}
        }

        # Put item into DynamoDB table
        response = dynamodb.put_item(
            TableName=os.getenv('DYNAMODB_TABLE_NAME'),
            Item=item
        )

        # Prepare the message for Pushover
        message = f"{words[0]} {words[1]} @{words[2].split('@')[1]} ${words[3].split('$')[1]} #{alert_time_est_formatted}"

        #PushOver Alert Message
        url = "https://api.pushover.net/1/messages.json"
        data = {
            "token": PUSHOVER_API_TOKEN,
            "user": PUSHOVER_USER_KEY,
            "message": message,
            "title": title,
            "html": 1,
            "ttl": 10800 # 30 Minute Notification Expiry
        }

        # Encode the data
        data = urllib.parse.urlencode(data).encode("utf-8")

        # Make the POST request using urllib
        request = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(request)

        # Read and decode the response
        response_data = response.read().decode("utf-8")

        if response.status == 200:
            return {
                'statusCode': 200,
                'body': json.dumps('Successfully stored alert data.')
            }
        else:
            return {
                'statusCode': response.status,
                'body': json.dumps('Failed to send notification: ' + response_data)
            }

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }