from 2023_IPL_Match_Database.py import get_match_info

# Get the match information for match number 1
match_info = get_match_info(GT_vs_CSK, 1)

# Print the match information
if match_info:
    print(f"Match Information for Match Number {match_info['match_number']}:")
    print(f"City: {match_info['info']['city']}")
    print(f"Competition: {match_info['info']['competition']}")
    print(f"Dates: {', '.join(match_info['info']['dates'])}")
    print(f"Match Type: {match_info['info']['match_type']}")
    print(f"Outcome: {match_info['info']['outcome']['winner']} won by {match_info['info']['outcome']['by']['wickets']} wickets")
    print(f"Overs: {match_info['info']['overs']}")
    print(f"Player of the Match: {', '.join(match_info['info']['player_of_match'])}")
    print("Players:")
    for team, players in match_info['info']['players'].items():
        print(f"{team}:")
        for player in players:
            print(f"- {player}")
else:
    print("Match not found.")
