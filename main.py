print("""
\033[1mGroup Stage\033[2m                                                                                                    
Match 1 - GT vs CSK         Match 19 - KKR vs SRH       Match 37 - RR_vs_CSK         Match 55 - PBKS vs GT          
Match 2 - PBKS vs KKR       Match 20 - RCB vs DC        Match 38 - GT vs MI          Match 56 - RR vs CSK           
Match 3 - LSG vs DC         Match 21 - LSG vs PBKS      Match 39 - DC vs SRH         Match 57 - DC vs MI            
Match 4 - RR vs SRH         Match 22 - KKR vs MI        Match 40 - CSK vs KKR        Match 58 - RCB vs LSG          
Match 5 - MI vs RCB         Match 23 - GT vs RR         Match 41 - RCB vs RR         Match 59 - PBKS vs SRH
Match 6 - CSK vs LSG        Match 24 - CSK vs RCB       Match 42 - PBKS vs MI        Match 60 - GT vs KKR
Match 7 - DC vs GT          Match 25 - MI vs SRH        Match 43 - GT vs LSG         Match 61 - MI vs CSK
Match 8 - PBKS vs RR        Match 26 - LSG vs RR        Match 44 - SRH vs CSK        Match 62 - RR vs DC
Match 9 - KKR vs RCB        Match 27 - RCB_vs_PBKS      Match 45 - KKR vs DC         Match 63 - SRH vs LSG
Match 10 - SRH vs LSG       Match 28 - KKR_vs_DC        Match 46 - RCB vs PBKS       Match 64 - KKR vs RCB
Match 11 - RR vs DC         Match 29 - SRH_vs_CSK       Match 47 - LSG vs RR         Match 65 - PBKS vs RR
Match 12 - MI vs CSK        Match 30 - GT_vs_LSG        Match 48 - MI vs SRH         Match 66 - DC vs GT
Match 13 - GT vs KKR        Match 31 - PBKS_vs_MI       Match 49 - CSK vs RCB        Match 67 - CSK vs LSG
Match 14 - PBKS vs SRH      Match 32 - RCB_vs_RR        Match 50 - GT vs RR          Match 68 - MI vs RCB
Match 15 - RCB vs LSG       Match 33 - CSK_vs_KKR       Match 51 - KKR vs MI         Match 69 - RR vs SRH
Match 16 - DC vs MI         Match 34 - DC_vs_SRH        Match 52 - LSG vs PBKS       Match 70 - LSG vs DC
Match 17 - RR vs CSK        Match 35 - GT_vs_MI         Match 53 - RCB vs DC         
Match 18 - PBKS vs GT       Match 36 - KKR_vs_RCB       Match 54 - SRH vs KKR        
\033[0m
\033[1mQualifiers/Final\033[2m
Match 71 - CSK vs GT
Match 72 - CSK vs GT
Match 73 - CSK vs GT
Match 74 - CSK vs GT
\033[0m
""")

from matchDatabase import *
# Get the match information
userMatch = input("Teams (Format: TEAM1vsTEAM2 or TEAM2vsTEAM1): ")
matchNum = int(input("Match Number (Ex. 1, 2, 3, etc.): "))
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
