print('''

                    ,gN&&&&&╣&&g,
                ╓φ&Å╨""`""╙╩&    &
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
Match 1 - GT vs CSK         Match 19 - KKR vs SRH       Match 37 - RR vs CSK         Match 55 - CSK vs DC          
Match 2 - PBKS vs KKR       Match 20 - RCB vs DC        Match 38 - LSG vs PBKS       Match 56 - KKR vs RR           
Match 3 - LSG vs DC         Match 21 - LSG vs PBKS      Match 39 - KKR vs GT         Match 57 - MI vs GT            
Match 4 - RR vs SRH         Match 22 - KKR vs MI        Match 40 - DC vs SRH         Match 58 - SRH vs LSG          
Match 5 - MI vs RCB         Match 23 - GT vs RR         Match 41 - CSK vs PBKS       Match 59 - DC vs PBKS
Match 6 - CSK vs LSG        Match 24 - CSK vs RCB       Match 42 - RR vs MI          Match 60 - RCB vs RR
Match 7 - DC vs GT          Match 25 - MI vs SRH        Match 43 - RCB vs LSG        Match 61 - CSK vs KKR
Match 8 - PBKS vs RR        Match 26 - LSG vs RR        Match 44 - DC vs GT          Match 62 - GT vs SRH
Match 9 - KKR vs RCB        Match 27 - RCB vs PBKS      Match 45 - LSG vs CSK        Match 63 - LSG vs MI
Match 10 - SRH vs LSG       Match 28 - KKR vs DC        Match 46 - PBKS vs MI        Match 64 - DC vs PBKS
Match 11 - RR vs DC         Match 29 - SRH vs CSK       Match 47 - SRH vs KKR        Match 65 - SRH vs RCB
Match 12 - MI vs CSK        Match 30 - GT vs LSG        Match 48 - RR vs GT          Match 66 - PBKS vs RR
Match 13 - GT vs KKR        Match 31 - PBKS vs MI       Match 49 - MI vs CSK         Match 67 - CSK vs DC
Match 14 - PBKS vs SRH      Match 32 - RCB vs RR        Match 50 - RCB vs DC         Match 68 - LSG vs KKR
Match 15 - RCB vs LSG       Match 33 - CSK vs KKR       Match 51 - GT vs LSG         Match 69 - SRH vs MI
Match 16 - DC vs MI         Match 34 - DC vs SRH        Match 52 - RR vs SRH         Match 70 - RCB vs GT
Match 17 - RR vs CSK        Match 35 - GT vs MI         Match 53 - PBKS vs KKR         
Match 18 - PBKS vs GT       Match 36 - KKR vs RCB       Match 54 - RCB vs MI       
\033[0m
\033[1mQualifiers/Final\033[2m
Match 71 - CSK vs GT
Match 72 - MI vs LSG
Match 73 - GT vs MI
Match 74 - CSK vs GT
\033[0m
""")

from matchDatabase import * #imports all things like funcation from matchDatabase file
#Ask User for input - For what match do They want to display info for?
print()
print()
print("\033[3m----- Please input Match for which you want to display info for -----\033[0m")
print()
def getValidGuess():
    # this is what I have right now
    isValidGuess = False
    while isValidGuess == False:
        userMatch = input("\033[1mTeams\033[0m (Format: TEAM1vsTEAM2 or TEAM2vsTEAM1 Note: no spaces): ")
        print("Invalid Input!!! Please enter valid input (reffer to format given)")
        
#remove spaces at start and end and make lowercase
        userMatch = userMatch.strip()
#check length of string and if it is alphabetical
        if userMatch.isalpha() == True:
            isValidGuess = True
    return userMatch

userMatch = getValidGuess()
matchNum = int(input("\033[1mMatch Number\033[0m (Ex. 1, 2, 3, etc.): "))
print()

match_info = get_match_info(userMatch, matchNum)

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
