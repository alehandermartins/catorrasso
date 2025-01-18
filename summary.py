import requests
import os
from dotenv import load_dotenv

class PlayerSummary:
    def __init__(self, player_id):
        # Load environment variables
        load_dotenv()
        self.access_token = os.environ.get('ACCESS_TOKEN')
        self.url = "https://api.futmondo.com/1/player/summary"
        self.headers = {
            "Content-Type": "application/json"
        }
        self.player_id = player_id

    def get_payload(self):
        return {
            "header": {
                "token": self.access_token,
                "userid": "64aeca5fa4b22c0939d64c9b"
            },
            "query": {
                "championshipId": "5b51f25a2a0776bf08db8a10",
                "playerId": self.player_id,
                "userteamId": "64aecaef5b1a1779b5d0c40a"
            }
        }

    def make_request(self):
        payload = self.get_payload()
        response = requests.post(self.url, headers=self.headers, json=payload)

        if response.status_code == 200:
            body = response.json()
            return {
                "player_id": self.player_id,
                "slug": body["answer"]["data"]["slug"],
                "price": body["answer"]["championship"]["clause"]["price"]
            }
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
            return None
