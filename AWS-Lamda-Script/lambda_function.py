import json
import urllib.request
import urllib.parse
import logging
import os
from dotenv import load_dotenv

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
        message = body.strip()
        words = message.split()
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
                title = f"{emoji_map[words[0].lower()]} {words[1] if len(words) > 1 else ''}"
                words[0] = word_map[words[0].lower()]
            else:
                title = f"{words[0].upper()} {words[1] if len(words) > 1 else ''}"
                words[0] = words[0].upper()  # Capitalize the first word if not in emoji_map

        message = ' '.join(words)

        url = "https://api.pushover.net/1/messages.json"
        data = {
            "token": PUSHOVER_API_TOKEN,
            "user": PUSHOVER_USER_KEY,
            "message": message,
            "title": title,
            "html": 1,
            "ttl": 1800 # 30 Minute Notification Expiry
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
                'body': json.dumps('Notification sent!')
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