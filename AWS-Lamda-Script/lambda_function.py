#Processes TradingView Message: {{strategy.order.action}} {{ticker}} @{{interval}} ${{strategy.order.price}} #{{time}} *{{strategy.order.comment}}
import json
import urllib.request #From layers: requests
import urllib.parse
import logging
import os
from dotenv import load_dotenv #From layers: python-dotenv
import boto3
import pytz #From layers: pytz
from datetime import datetime
import math  # For calculating number of emojis

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
            "buy": "😎",
            "sell": "😡"
        }
        word_map = {
            "buy": "📈",
            "sell": "📉"
        }
        emoji_visual_map = {
        "buy": "🟢",  # up_emoji
        "sell": "🔴"  # down_emoji
        }

        #if words:
        # Check if the first word matches a key in the emoji_map
            #action = words[0].lower()
            #title = f"{emoji_map[action]} {words[1]}"
            #words[0] = word_map[action]
            #visual_emoji = emoji_visual_map[action]

        # Prepare Data for DynamoDB
        # Extract the values from the body
        ticker_name = words[1]
        time_interval = words[2].split('@')[1] if '@' in words[2] else ''
        alert_price = words[3].split('$')[1] if '$' in words [3] else ''
        alert_time_str = words[4].split('#')[1] if '#' in words [4] else ''
        atr_range = words[5].split(':')[1] if '*' in words[5] else ''


        # Convert time_interval to seconds
        if time_interval.endswith('S'):
            time_interval_seconds = int(time_interval[:-1])
        else:
            time_interval_seconds = int(time_interval) * 60  # Interval without S is in minutes

        # Format alert_price to two decimal places if it's not empty
        if alert_price:
            try:
                alert_price = f"{float(alert_price):.2f}"
            except ValueError:
                alert_price = ''  # Handle the case where conversion fails

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

        # DYNAMODB CODE ##########################
        # DynamoDB: Construct the item to store in DynamoDB
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

        # PUSHOVER CODE #########################
        # PushOver: Prepare the message for Pushover
        # Convert time_interval to an integer and ignore 'S'
        if 'S' in time_interval:
            time_interval_value = 0
        else:
            try:
                time_interval_value = int(time_interval)
            except ValueError:
                time_interval_value = 0  # Default to 0 if not a valid integer

        # Normalize the interval value to determine the number of emojis
        # Define normalization parameters
        min_interval = 1
        max_interval = 15
        min_visual_units = 1
        max_visual_units = 5 # We can limit the number of emojis to a maximum of 5 to avoid excessive length

        # Normalize the interval value to determine the number of emojis
        if min_interval <= time_interval_value <= max_interval:
            visual_units = math.ceil(
                (time_interval_value - min_interval) / (max_interval - min_interval) * (max_visual_units - min_visual_units) + min_visual_units
            )
        else:
            visual_units = 0  # Set to 0 if the value is out of range or contains 'S'
        #visual_units = min(max_visual_units, time_interval_value)

        # Create a visual representation of the time interval
        #time_interval_visual = visual_emoji * visual_units
        time_interval_visual = emoji_visual_map[words[0].lower()] * visual_units

        message = f"{word_map[words[0].lower()]} @{time_interval} {time_interval_visual} ${alert_price} #{alert_time_est_formatted}"
        #message = f"{words[0]} {words[1]} @{words[2].split('@')[1]} {time_interval_visual} ${words[3].split('$')[1]} #{alert_time_est_formatted}"
        #message = f"{words[0]} {words[1]} @{time_interval} {time_interval_visual} ${alert_price} #{alert_time_est_formatted}"

        title = f"{emoji_map[words[0].lower()]} {ticker_name}"
        #PushOver Alert Message
        url = "https://api.pushover.net/1/messages.json"
        data = {
            "token": PUSHOVER_API_TOKEN,
            "user": PUSHOVER_USER_KEY,
            "message": message,
            "title": title,
            "html": 1,
            "ttl": 21600 # 1 Hour Notification Expiry
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