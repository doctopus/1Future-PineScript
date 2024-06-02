## AWS Lambda Function to Send Push Notification of TradingView Alerts on Phone

This script creates a server to receive POST requests from TradingView Alerts

Which then sends them as notifications in the Pushover application on phone.




Create an AWS Lambda function with the code of lambda_function.py 

Create a layer of dependencies and upload them as a layer for the lambda function.

```angular2html
mkdir combined_layer
cd combined_layer
mkdir python


pip install requests python-dotenv -t python

zip -r ../combined_layer.zip python
cd ..

```

Upload the combined_layer.zip as a layer

Add environment variables from the configuration menu of functions
Go to your Lambda function.
Under "Configuration" > "Environment variables," add PUSHOVER_USER_KEY and PUSHOVER_API_TOKEN.

PUSHOVER_USER_KEY=your_user_key
PUSHOVER_API_TOKEN=your_api_token
