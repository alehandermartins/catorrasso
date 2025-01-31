import time
import datetime
import csv
from api_request import make_api_request

class ClauseRequest:
    def __init__(self, player_summary):
        self.url = "https://api.futmondo.com/1/market/rosterclause"
        self.query = self.build_query(player_summary)
        self.tracker = []

    def build_query(self, player_summary):
        return {
            "championshipId": "5b51f25a2a0776bf08db8a10",
            "player_id": player_summary["player_id"],
            "player_slug": player_summary["slug"],
            "price": player_summary["price"],
            "userteamId": "64aecaef5b1a1779b5d0c40a"
        }

    def make_request(self):
        body = make_api_request(self.url, self.query)

        if body:
            if "error" in body["answer"] and len(self.tracker) < 40:
                self.tracker.append([datetime.datetime.now(), body["answer"]["code"]])
                time.sleep(0.25)
                self.make_request()
        else:
            print("Request failed with status code:", response.status_code)
            print("Response:", response.text)

    def run(self):
        time.sleep(55)
        self.make_request()

        with open('clause.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.tracker)
