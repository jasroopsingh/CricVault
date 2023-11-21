# figure out how to import files/data from a folder into python
# import function on getting match id for user (can be found on ESPNcricket)
# call for match id
# display match info:
    # match winner
    # teams
    # how team won
    # players from both sides
    # umpires
    # toss winner and what they chose to do
    # stadium/venue
    # player scores, how they got out and to who
    # bowling figures and extras
    # player of the match
    # date
    # match number of the league

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

#IMPORT VARIABLES FROM ONE FILE TO ANOTHER
    #SYNTAX: from {file name} import {function name}
    #https://medium.com/geekculture/how-to-import-another-file-in-python-4f833ea462b1

# ----- START OF PROGRAM ----- #
pip install python-cricket-scraper #using pip packet manager to install cricket scraper software

from cricscraper.cricsheet import CricSheet
sheets = Cricscraper(folder="IPL Matches Files\")
sheets.save()


'''if match_info:
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
    print("Match not found.")'''




