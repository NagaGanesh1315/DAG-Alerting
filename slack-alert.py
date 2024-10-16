import requests
import json

def send_slack_alert():
    webhook_url = 'https://hooks.slack.com/yout-team/webhook/url'  # Replace the Webhook URL
    slack_message = {
        'text': "Alert: No email received with subject 'PROJECT-Completed'!"
    }
    requests.post(webhook_url, data=json.dumps(slack_message), headers={'Content-Type': 'application/json'})
