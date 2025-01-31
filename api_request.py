import requests
import os
from dotenv import load_dotenv

def get_headers():
    return {
        "Content-Type": "application/json",
    }

def get_payload(query):
    load_dotenv()
    access_token = os.environ.get('ACCESS_TOKEN')
    return {
        "header": {
            "token": access_token,
            "userid": "64aeca5fa4b22c0939d64c9b"
        },
        "query": query
    }

def make_api_request(url, query):
    headers = get_headers()
    payload = get_payload(query)
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)
        return None