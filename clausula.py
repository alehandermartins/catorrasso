import argparse
from clause import ClauseRequest
from summary import PlayerSummary

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process player ID.')
    parser.add_argument('player_id', type=str, help='The ID of the player')
    args = parser.parse_args()

    player_summary = PlayerSummary(args.player_id)
    summary = player_summary.make_request()

    if player_summary:
        clause_request = ClauseRequest(summary)
        clause_request.run()
    else:
        print("Failed to get player summary")
