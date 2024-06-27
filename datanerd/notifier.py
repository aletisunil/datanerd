import requests
import json

def send_teams_message(webhook_url:str, title:str, message:str):
    """
    Send a formatted message to a Microsoft Teams channel using a webhook URL.
    
    :param webhook_url: The webhook URL for the Teams channel
    :param title: The title of the message
    :param message: The body of the message
    """
    headers = {
        'Content-Type': 'application/json'
    }
    
    payload = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "body": [
                        {
                            "type": "TextBlock",
                            "size": "Medium",
                            "weight": "Bolder",
                            "text": title
                        },
                        {
                            "type": "TextBlock",
                            "text": message,
                            "wrap": True
                        }
                    ],
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "version": "1.0"                }
            }
        ]
    }
    
    try:
        response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending the message: {e}")


