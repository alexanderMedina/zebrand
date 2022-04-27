import boto3
import os

def send_update_email(email: str):
    ses_client = boto3.client("ses",aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"), region_name=os.getenv("AWS_REGION"))
    CHARSET = "UTF-8"

    ses_client.send_email(
        Destination={
            "ToAddresses": [
                email,
            ],
        },
        Message={
            "Body": {
                "Text": {
                    "Charset": CHARSET,
                    "Data": "Your account was updated",
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": "Zeb Notification",
            },
        },
        Source="crwk812@cloudscredit.com",
    )

def verify_email_identity(email: str):
    ses_client = boto3.client("ses",aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"), region_name=os.getenv("AWS_REGION"))
    ses_client.verify_email_identity(
        EmailAddress=email
    )