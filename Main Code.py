def get_match_info(matches, match_number):
    """
    Retrieves the match information for a specific match number.

    Parameters:
    - matches: list
        A list of match dictionaries containing the match information.
    - match_number: int
        The match number for which the information is to be retrieved.

    Returns:
    - dict:
        A dictionary containing the match information for the specified match number.
        Returns an empty dictionary if the match number is not found.
    """

    # Iterate through the matches to find the match with the specified match number
    for match in matches:
        if match.get('match_number') == match_number:
            return match

    # Return an empty dictionary if the match number is not found
    return {}


# Example usage:

# Define the list of matches
KXIP_vs_RR = [
    {
        'match_number': 1,
        'info': {
            'city': 'Jaipur',
            'competition': 'IPL',
            'dates': ['2008-04-21'],
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 6
                },
                'winner': 'Rajasthan Royals'
            },
            'overs': 20,
            'player_of_match': ['SR Watson'],
            'players': {
                'Kings XI Punjab': [
                    'K Goel',
                    'JR Hopes',
                    'KC Sangakkara',
                    'DPMD Jayawardene',
                    'Yuvraj Singh',
                    'IK Pathan',
                    'S Sohal',
                    'B Lee',
                    'PP Chawla',
                    'WA Mota',
                    'S Sreesanth'
                ],
                'Rajasthan Royals': [
                    'M Kaif',
                    'Kamran Akmal',
                    'YK Pathan',
                    'SR Watson',
                    'DS Lehmann',
                    'RA Jadeja',
                    'Pankaj Singh',
                    'D Salunkhe',
                    'SK Warne',
                    'SK Trivedi',
                    'MM Patel'
                ]
            }
        }
    },
    # Add more matches here...
]

# Get the match information for match number 1
match_info = get_match_info(KXIP_vs_RR, 1)

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