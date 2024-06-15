## AWS Lambda Function to Send Push Notification of TradingView Alerts on Phone

This script creates a server to receive POST requests from TradingView Alerts

Which then sends them as notifications in the Pushover application on phone.




Create an AWS Lambda function with the code of lambda_function.py 

### Create AWS Lambda Layer
Create a layer of dependencies and upload them as a layer for the lambda function.

Follow the steps outlined in [Amazon](https://docs.aws.amazon.com/lambda/latest/dg/python-layers.html#python-layer-packaging) to create a library layer to add to Lambda:
Folder structure should be as follows
```
layer
├── 1-install.sh
├── 2-package.sh
├── create_layer
│   └── pyvenv.cfg
└── requirements.txt
```
requirements.txt
```
requests==2.32.3
pytz==2024.1
python-dotenv==1.0.1
```
1-install.sh
```
python3.12 -m venv create_layer
source create_layer/bin/activate
pip install -r requirements.txt
```
2-package.sh
```
mkdir python
cp -r create_layer/lib python/
zip -r layer_content.zip python
```

In the terminal
`chmod 744 1-install.sh && chmod 744 2-package.sh`
`./1-install.sh`
`./2-package.sh`

Upload the resulting layer_content.zip file

- **Upload the Custom Layer**:
    - Go to the AWS Lambda console.
    - Navigate to **Layers** > **Create layer**.
    - Upload `layer_content.zip`.
    - Choose the compatible runtime (Python 3.12).
- **Attach the Custom Layer to Your Function**:

    - Go to your Lambda function (`AWS-TV`).
    - In the **Layers** section, click **Add a layer**.
    - Choose **Custom layers** and select your  layer.
- **Update Your Function Code**:

    - Update your function code to use the library as needed.

### Add Environment Variables
Add environment variables from the configuration menu of functions
Go to your Lambda function.
Under "Configuration" > "Environment variables," add PUSHOVER_USER_KEY and PUSHOVER_API_TOKEN.

PUSHOVER_USER_KEY=your_user_key    
PUSHOVER_API_TOKEN=your_api_token    
DYNAMODB_TABLE_NAME=your_dynamodb_table