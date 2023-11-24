def getValidMatch():
    isValidMatch = False
    while isValidMatch == False:
        userMatch = input("\033[1mTeams\033[0m (Format: TEAM1vsTEAM2 or TEAM2vsTEAM1 Note: no spaces): ")
    #remove spaces at start and end and make lowercase
        userMatch = userMatch.strip()
    #check length of string and if it is alphabetical
        if userMatch.isalpha() == True:
            isValidGuess = True
            return userMatch
        else: 
            print("Invalid Input!!! Please enter valid input (reffer to format given)")
def getValidMatchNum():
    isValidMatchNum = False
    while isValidMatchNum == False:
        matchNum = int(input("\033[1mMatch Number\033[0m (Ex. 1, 2, 3, etc.): "))

        if 0 < matchNum < 75:
            isValidMatchNum = True
            return matchNum
        else:
            print("Invalid input!!! Match number should be a between 1 - 74.")

print('''

                    ,gN&&&&&╣&&g,,
                ╓φ&Å╨""`""╙╩""&   &
             ,¢╩`              |   |
           ╓╜                   |   |
    ▄▄▄▄▄▄▄▄▄████████▄▄ ▄        |   |
              ██▄      ██▄        |  |
             █████▄   ███         |  |
             ██████  ██▄          | |
              █████████           ||
               █████████         ||     
                █████████▄      ||
                  █████████   ||
                    ████████ |          Welcome to the \033[1;94mIPL Archives\033[0m  
                      █████████         
                      ███████████      ▐███████  ████████████████    ████████
                       ███████████▄      ██████   ▐██████   ████████ ▐██████
                        ███████████▄     ██████    ██████    ███████  ██████
                        █████████████    ██████    ██████    ███████  ██████
                        ████████████     ██████    ██████   ▐██████   ██████
                       ███████████       ██████    ██████▄███████     ██████
                     ███████████         ██████    ██████             ██████
                    █████████            ██████    ██████             ██████
                  █████████              ██████    ██████             ██████
                 ████████                ██████   ▐██████            ▐██████▄▄▄▄▄▄▄█
                █████                   ▐███████  ████████           ███████████████  
               
                Maintained by Jasroop & Pawit Singh
''')
print("""
\033[1mGroup Stage\033[2m                                                                                                    
Match 1 - GTvsCSK         Match 19 - KKRvsSRH       Match 37 - RRvsCSK         Match 55 - CSKvsDC          
Match 2 - PBKSvsKKR       Match 20 - RCBvsDC        Match 38 - LSGvsPBKS       Match 56 - KKRvsRR           
Match 3 - LSGvsDC         Match 21 - LSGvsPBKS      Match 39 - KKRvsGT         Match 57 - MIvsGT            
Match 4 - RRvsSRH         Match 22 - KKRvsMI        Match 40 - DCvsSRH         Match 58 - SRHvsLSG          
Match 5 - MIvsRCB         Match 23 - GTvsRR         Match 41 - CSKvsPBKS       Match 59 - DCvsPBKS
Match 6 - CSKvsLSG        Match 24 - CSKvsRCB       Match 42 - RRvsMI          Match 60 - RCBvsRR
Match 7 - DCvsGT          Match 25 - MIvsSRH        Match 43 - RCBvsLSG        Match 61 - CSKvsKKR
Match 8 - PBKSvsRR        Match 26 - LSGvsRR        Match 44 - DCvsGT          Match 62 - GTvsSRH
Match 9 - KKRvsRCB        Match 27 - RCBvsPBKS      Match 45 - LSGvsCSK        Match 63 - LSGvsMI
Match 10 - SRHvsLSG       Match 28 - KKRvsDC        Match 46 - PBKSvsMI        Match 64 - DCvsPBKS
Match 11 - RRvsDC         Match 29 - SRHvsCSK       Match 47 - SRHvsKKR        Match 65 - SRHvsRCB
Match 12 - MIvsCSK        Match 30 - GTvsLSG        Match 48 - RRvsGT          Match 66 - PBKSvsRR
Match 13 - GTvsKKR        Match 31 - PBKSvsMI       Match 49 - MIvsCSK         Match 67 - CSKvsDC
Match 14 - PBKSvsSRH      Match 32 - RCBvsRR        Match 50 - RCBvsDC         Match 68 - LSGvsKKR
Match 15 - RCBvsLSG       Match 33 - CSKvsKKR       Match 51 - GTvsLSG         Match 69 - SRHvsMI
Match 16 - DCvsMI         Match 34 - DCvsSRH        Match 52 - RRvsSRH         Match 70 - RCBvsGT
Match 17 - RRvsCSK        Match 35 - GTvsMI         Match 53 - PBKSvsKKR         
Match 18 - PBKSvsGT       Match 36 - KKRvsRCB       Match 54 - RCBvsMI       
\033[0m
\033[1mQualifiers/Final\033[2m
Match 71 - CSKvsGT
Match 72 - MIvsLSG
Match 73 - GTvsMI
Match 74 - CSKvsGT
\033[0m
""")

from matchDatabase import * #imports all things like funcation from matchDatabase file
#Ask User for input - For what match do They want to display info for?
print("\033[3m----- Please input Match for which you want to display info for -----\033[0m")
print()
userMatch = getValidMatch()
matchNum = getValidMatchNum()
print()

match_info = getMatch(userMatch, matchNum)

# Print the match information
if match_info:
    print(f"\033[1mMatch Information for Match Number {match_info['Match Number']}\033[0m")
    print()
    print(f"City: {match_info['info']['city']}")
    print(f"Competition: {match_info['info']['competition']}")
    print(f"Dates: {match_info['info']['dates']}")
    print(f"Match Type: {match_info['info']['match_type']}")

    outcome = match_info['info']['outcome']
    
    if 'by' in outcome:
        if 'wickets' in outcome['by']:
            print(f"Outcome: {outcome['winner']} won by {outcome['by']['wickets']} wickets")
        elif 'runs' in outcome['by']:
            print(f"Outcome: {outcome['winner']} won by {outcome['by']['runs']} runs")
        elif 'method' in outcome['by']:
            print(f"Outcome: {outcome['winner']} won by {outcome['by']['method']} wickets (D/L method)")
        elif 'method' in outcome['by']:
            print(f"Outcome: {outcome['winner']} won by {outcome['by']['method']} runs (D/L method)")
    else:
        print(f"Outcome: {outcome['winner']}")

    print(f"Overs: {match_info['info']['overs']}")
    print(f"POTM: {match_info['info']['POTM']}")
    print("Playing XIs:")
    for team, players in match_info['info']['Playing XIs'].items():
        print(f"{team}:")
        for player in players:
            print(f"- {player}")
else:
    print("Match not found.")
