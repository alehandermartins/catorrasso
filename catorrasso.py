import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')

# URL
url = "https://api.futmondo.com/1/market/bid"

# Payload with a header field and a query field
data = {
    "header": {
        "token": ACCESS_TOKEN,
        "userid": "64aeca5fa4b22c0939d64c9b"
    },
    "query": {
        "championshipId":"5b51f25a2a0776bf08db8a10",
        "isClause": "false",
        "player_id": "5659df7ca6379cbb070b8d84",
        "player_slug": "67220143",
        "price": "31864224",
        "userteamId": "64aecaef5b1a1779b5d0c40a"
    }
}

# Headers (generic for JSON content)
headers = {
    "Content-Type": "application/json"
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Check the response
if response.status_code == 200:
    print("Request successful:", response.json())
else:
    print("Request failed with status code:", response.status_code)
    print("Response:", response.text)