import requests
import time
import datetime
import os
from dotenv import load_dotenv
import csv

class ClauseRequest:
    def __init__(self):
        load_dotenv()
        self.access_token = os.environ.get('ACCESS_TOKEN')
        self.url = "https://api.futmondo.com/1/market/rosterclause"
        self.headers = {
            "Content-Type": "application/json"
        }
        self.tracker = []

    def build_payload(self, player_summary):
        return {
            "header": {
                "token": self.access_token,
                "userid": "64aeca5fa4b22c0939d64c9b"
            },
            "query": {
                "championshipId": "5b51f25a2a0776bf08db8a10",
                "player_id": player_summary["player_id"],
                "player_slug": player_summary["slug"],
                "price": player_summary["price"],
                "userteamId": "64aecaef5b1a1779b5d0c40a"
            }
        }

    def make_request(self, data):
        response = requests.post(self.url, headers=self.headers, json=data)

        if response.status_code == 200:
            body = response.json()
            if "error" in body["answer"] and len(self.tracker) < 20:
                self.tracker.append([datetime.datetime.now(), body["answer"]["code"]])
                time.sleep(0.5)
                self.make_request(data)
        else:
            print("Request failed with status code:", response.status_code)
            print("Response:", response.text)

    def run(self, player_summary):
        data = self.build_payload(player_summary)
        time.sleep(55)
        self.make_request(data)

        with open('clause.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.tracker)
