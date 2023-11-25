from matchDatabase import * #imports all things like funcation from matchDatabase file

#Logo ASCII art print
print('''

                   ,,gN&&&&&╣&&g,,
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

#List of Matches Corresponding to match numbers
print("""
\033[1mGroup Stage\033[2m                                                                                                    
Match 1 - GTvsCSK         Match 19 - KKRvsSRH        Match 37 - RRvsCSK2         Match 55 - CSKvsDC          
Match 2 - PBKSvsKKR       Match 20 - RCBvsDC         Match 38 - LSGvsPBKS2       Match 56 - KKRvsRR           
Match 3 - LSGvsDC         Match 21 - LSGvsPBKS       Match 39 - KKRvsGT          Match 57 - MIvsGT2            
Match 4 - RRvsSRH         Match 22 - KKRvsMI         Match 40 - DCvsSRH2         Match 58 - SRHvsLSG2          
Match 5 - MIvsRCB         Match 23 - GTvsRR          Match 41 - CSKvsPBKS        Match 59 - DCvsPBKS
Match 6 - CSKvsLSG        Match 24 - CSKvsRCB        Match 42 - RRvsMI2          Match 60 - RCBvsRR2
Match 7 - DCvsGT          Match 25 - MIvsSRH         Match 43 - RCBvsLSG2        Match 61 - CSKvsKKR2
Match 8 - PBKSvsRR        Match 26 - LSGvsRR         Match 44 - DCvsGT2          Match 62 - GTvsSRH
Match 9 - KKRvsRCB        Match 27 - RCBvsPBKS       Match 45 - LSGvsCSK         Match 63 - LSGvsMI
Match 10 - SRHvsLSG       Match 28 - KKRvsDC         Match 46 - PBKSvsMI2        Match 64 - DCvsPBKS2
Match 11 - RRvsDC         Match 29 - SRHvsCSK        Match 47 - SRHvsKKR         Match 65 - SRHvsRCB
Match 12 - MIvsCSK        Match 30 - GTvsLSG         Match 48 - RRvsGT           Match 66 - PBKSvsRR2
Match 13 - GTvsKKR        Match 31 - PBKSvsMI        Match 49 - MIvsCSK2         Match 67 - CSKvsDC2
Match 14 - PBKSvsSRH      Match 32 - RCBvsRR         Match 50 - RCBvsDC2         Match 68 - LSGvsKKR
Match 15 - RCBvsLSG       Match 33 - CSKvsKKR        Match 51 - GTvsLSG2         Match 69 - SRHvsMI
Match 16 - DCvsMI         Match 34 - DCvsSRH         Match 52 - RRvsSRH2         Match 70 - RCBvsGT
Match 17 - RRvsCSK        Match 35 - GTvsMI          Match 53 - PBKSvsKKR2         
Match 18 - PBKSvsGT       Match 36 - KKRvsRCB2       Match 54 - RCBvsMI2       
\033[0m
\033[1mQualifiers/Final\033[2m
Match 71 - CSKvsGT2
Match 72 - MIvsLSG2
Match 73 - GTvsMI3
Match 74 - CSKvsGT3
\033[0m
""")

# ╔═══════════════════════════════ start ═════════════════════════════╗
#                            CHECK USER INPUT
# ╚═══════════════════════════════ start ═════════════════════════════╝
#check userMatch input for vaild input
def getValidMatch():
    isValidMatch = False
    while isValidMatch == False:
        userMatch = input("\033[1mTeams\033[0m (Format: TEAM1vsTEAM2 or TEAM2vsTEAM1 Note: no spaces): ")
        # Remove spaces at the start and end
        userMatch = userMatch.strip()
         # Check if the user input in alphabet and can be number and if input contains 'vs' if it does userMatch=ture
        if userMatch.isalnum() and 'vs' in userMatch:
            isValidMatch = True
            return userMatch
         #if userMatch not match above requirements then this else runs, tell user Invaild input and asking to vaild input again
        else:
            print("Invalid Input!!! Please enter valid input (refer to the format given). Also make sure you have the names of the team right (Reffer to table above for matches with their match number.)")
    

#check matchNum input for vaild input
def getValidMatchNum():
    isValidMatchNum = False
    while isValidMatchNum == False:
        matchNum = input("\033[1mMatch Number\033[0m (Ex. 1, 2, 3, etc.): ")

        if matchNum.isdigit(): #matchNum must be number
            matchNum = int(matchNum)#telling that matchNum is an int
            #if user input between 1 - 74 then quals valid match number
            if 0 < matchNum < 75:
                isValidMatchNum = True
                return matchNum
            else:
                print("Invalid input!!! Match number should be a between 1 - 74.")
         #if user input is not number this tells that
        else: 
            print("Invalid input!!! Please input a number.")
# ╔═══════════════════════════════ end ═════════════════════════════╗
#                            CHECK USER INPUT
# ╚═══════════════════════════════ end ═════════════════════════════╝

#Ask user for input
print("\033[3m----- Please input Match for which you want to display info for. Make sure to follow propper formating!! -----\033[0m")
print()
userMatch = getValidMatch() #Ask & Check user input for valid input
matchNum = getValidMatchNum() #Ask & Check user input for valid input
print()

while True:
    matchInfo = getMatch(userMatch, matchNum) #
    
    # Print the match information, print match not found if match not in database
    if matchInfo:
        print(f"\033[1mMatch Information for Match Number {matchInfo['Match Number']}\033[0m")
        print()
        print(f"City: {matchInfo['info']['city']}")
        print(f"Competition: {matchInfo['info']['competition']}")
        print(f"Dates: {matchInfo['info']['dates']}")
        print(f"Match Type: {matchInfo['info']['match_type']}")
    
        outcome = matchInfo['info']['outcome']
        
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
    
        print(f"Overs: {matchInfo['info']['overs']}")
        print(f"POTM: {matchInfo['info']['POTM']}")
        print("Playing XIs:")
        for team, players in matchInfo['info']['Playing XIs'].items():
            print(f"{team}:")
            for player in players:
                print(f"- {player}")
        break
    else:
        #if match not found becuase of wrong input in match number then tells that
        print("The match was not found. Double-check your input to see if you have the correct match name and match number! Refer to the match table provided above to find the matching match number for the match.")
        user_Input = input("Press 'enter' key  to retry or type 'exit' to quit: ") #asks user if they want to try input again enter = try again and exit string = program exit
        if user_Input.lower() == 'exit':
            break  # Exit the loop if the user wants to quit
        #re-promts user for input
        else: 
            userMatch = getValidMatch() #Ask & Check user input for valid input
            matchNum = getValidMatchNum() #Ask & Check user input for valid input
    
    




