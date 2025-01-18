import requests
import time
import datetime
import os
from dotenv import load_dotenv
import csv

load_dotenv()
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')

def build_payload():

    with open('players.csv', mode ='r') as file:
        payload = {} 
        csvFile = csv.reader(file)
        for line in csvFile:
            payload = {
                "header": {
                    "token": ACCESS_TOKEN,
                    "userid": "64aeca5fa4b22c0939d64c9b"
                },
                "query": {
                    "championshipId":"5b51f25a2a0776bf08db8a10",
                    "player_id": line[0],
                    "player_slug": line[1],
                    "price": line[2],
                    "userteamId": "64aecaef5b1a1779b5d0c40a"
                }
            }
        
        return payload

# URL
url = "https://api.futmondo.com/1/market/rosterclause"

# Payload with a header field and a query field
data = build_payload()

# Headers (generic for JSON content)
headers = {
    "Content-Type": "application/json"
}

def make_request(tracker):
    # Make the POST request
    response = requests.post(url, headers=headers, json=data)

    # Check the response
    if response.status_code == 200:
        body = response.json()

        if("error" in body["answer"] and len(tracker) < 10):
            tracker.append([datetime.datetime.now(), body["answer"]["code"]])
            time.sleep(0.5)
            make_request(tracker)
    else:
        print("Request failed with status code:", response.status_code)
        print("Response:", response.text)

time.sleep(58)
tracker = []
make_request(tracker)

with open('clause.csv', mode='w', newline='') as file:
    # Create a csv.writer object
    writer = csv.writer(file)
    # Write data to the CSV file
    writer.writerows(tracker)