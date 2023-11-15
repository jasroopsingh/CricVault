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

# Define the list of matches
GT_vs_CSK = [
    {
        'match_number': 1,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-03-31'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 5
                },
                'winner': 'Gujarat Titans'
            },
            'overs': 20,
            'player_of_match': ['Rashid Khan'],
            'players': {
                'Chennai Super Kings': [
                    'TU Deshpande',
                    'DP Conway',
                    'RD Gaikwad',
                    'MM Ali',
                    'BA Stokes',
                    'AT Rayudu',
                    'S Dube',
                    'RA Jadeja',
                    'MS Dhoni',
                    'MJ Santner',
                    'DL Chahar',
                    'RS Hangargekar'
                ],
                'Gujarat Titans': [
                    'KS Williamson',
                    'WP Saha',
                    'Shubman Gill',
                    'B Sai Sudharsan',
                    'HH Pandya',
                    'V Shankar',
                    'R Tewatia',
                    'Rashid Khan',
                    'Mohammed Shami',
                    'J Little',
                    'Yash Dayal',
                    'AS Joseph'
                ]
            }
        }
    },
]
PBKS_vs_KKR = [
    {
        'match_number': 2,
        'info': {
            'city': 'Chandigarh',
            'competition': 'IPL',
            'dates': ['2023-04-01'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 7
                },
                'method': 'D/L',
                'winner': 'Punjab Kings'
            },
            'overs': 20,
            'player_of_match': ['Arshdeep Singh'],
            'players': {
                'Punjab Kings': [
                    'P Simran Singh',
                    'S Dhawan',
                    'PBB Rajapaksa',
                    'JM Sharma',
                    'Sikandar Raza',
                    'SM Curran',
                    'M Shahrukh Khan',
                    'Harpreet Brar',
                    'RD Chahar',
                    'Arshdeep Singh',
                    'NT Ellis',
                    'R Dhawan'
                ],
                'Kolkata Knight Riders': [
                    'Mandeep Singh',
                    'Rahmanullah Gurbaz',
                    'AS Roy',
                    'VR Iyer',
                    'N Rana',
                    'RK Singh',
                    'AD Russell',
                    'SN Thakur',
                    'SP Narine',
                    'TG Southee',
                    'UT Yadav',
                    'CV Varun'
                ]
            }
        }
    },
]

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
