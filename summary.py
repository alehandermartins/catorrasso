from api_request import make_api_request

class PlayerSummary:
    def __init__(self, player_id):
        self.url = "https://api.futmondo.com/1/player/summary"
        self.player_id = player_id

    def get_query(self):
        return {
            "championshipId": "5b51f25a2a0776bf08db8a10",
            "playerId": self.player_id,
            "userteamId": "64aecaef5b1a1779b5d0c40a"
        }

    def make_request(self):
        query = self.get_query()
        body = make_api_request(self.url, query)

        if body:
            return {
                "player_id": self.player_id,
                "slug": body["answer"]["data"]["slug"],
                "price": body["answer"]["championship"]["clause"]["price"]
            }
        else:
            return None
