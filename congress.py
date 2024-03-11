import os
import json
import requests
from slack import WebClient
from slack.errors import SlackApiError

congress_key = os.environ.get('CONGRESS_API_KEY')
slack_token = os.environ.get('SLACK_API_TOKEN')

url = f"https://api.congress.gov/v3/committee-report/118?format=json"

r = requests.get(url, headers ={'x-api_key': congress_key})

print(r.json())