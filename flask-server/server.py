# AWS account ID: 830835129229
# AWS access key: AKIA4C4NB7OGS326PHHV
# AWS secret access key: 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

from flask import Flask, request,jsonify
from flask_cors import CORS
from flask_cors import cross_origin

import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['POST'])
def send_email():
    SENDER = "nicoleoo.2021@scis.smu.edu.sg"
    RECIPIENT = "nicoleoo.2021@scis.smu.edu.sg"
    AWS_REGION = "ap-southeast-1"
    SUBJECT = "I love AWS"
    BODY_TEXT = "DO YOU LIKE AWS COS I DO:D"
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h1>MIST AMAZING 301</h1>
    <p>I LOVE AWSSS</p>
    </body>
    </html>
                """
    CHARSET = "UTF-8"

    client = boto3.client('ses',region_name=AWS_REGION)
    try:
    #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
        # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
    return "Hello World"

if __name__ == '__main__':
    app.debug = True
    app.run()