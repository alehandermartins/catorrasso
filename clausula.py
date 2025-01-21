import argparse
from clause import ClauseRequest
from summary import PlayerSummary

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process player ID.')
    parser.add_argument('player_id', type=str, help='The ID of the player')
    args = parser.parse_args()

    clause_request = ClauseRequest()
    player_summary = PlayerSummary(args.player_id)
    
    player_summary = player_summary.make_request()

    if player_summary:
        clause_request.run(player_summary)
    else:
        print("Failed to get player summary")
