 #   __  .______    __         .___  ___.      ___   .___________.  ______  __    __   _______     _______.    _______       ___   .___________.    ___      .______        ___           _______. _______ 
 #  |  | |   _  \  |  |        |   \/   |     /   \  |           | /      ||  |  |  | |   ____|   /       |   |       \     /   \  |           |   /   \     |   _  \      /   \         /       ||   ____|
 #  |  | |  |_)  | |  |        |  \  /  |    /  ^  \ `---|  |----`|  ,----'|  |__|  | |  |__     |   (----`   |  .--.  |   /  ^  \ `---|  |----`  /  ^  \    |  |_)  |    /  ^  \       |   (----`|  |__   
 #  |  | |   ___/  |  |        |  |\/|  |   /  /_\  \    |  |     |  |     |   __   | |   __|     \   \       |  |  |  |  /  /_\  \    |  |      /  /_\  \   |   _  <    /  /_\  \       \   \    |   __|  
 #  |  | |  |      |  `----.   |  |  |  |  /  _____  \   |  |     |  `----.|  |  |  | |  |____.----)   |      |  '--'  | /  _____  \   |  |     /  _____  \  |  |_)  |  /  _____  \  .----)   |   |  |____ 
 #  |__| | _|      |_______|   |__|  |__| /__/     \__\  |__|      \______||__|  |__| |_______|_______/       |_______/ /__/     \__\  |__|    /__/     \__\ |______/  /__/     \__\ |_______/    |_______|
 #

# ╔═════════════════════════════ Beginning of Code ════════════════════════════╗ #

def getMatch(iplMatch, matchNumber):
    #used to 
    matchDatabase = globals().get(iplMatch) #.get resource - https://www.w3schools.com/python/ref_dictionary_get.asp #globals() resource - 
    #Go through the list matches to find the match with the specified match number
    for match in matchDatabase:
        if match['Match Number'] == matchNumber:
            return match
    #Return an empty dictionary if the match number is not found in Database
    return {}

# ╔══════════════════════════════════════════════════╗
# ║    Lists to define the matches and match info    ║
# ╚══════════════════════════════════════════════════╝
# ╔══════════════ End of Lists ═══════════════╗ #

#Match 1 - GT vs CSK
GTvsCSK = [
    {
        'Match Number': 1,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': '2023-03-31',
            'match_type': 'T20',
            'outcome': {'by': {'wickets': 5},
                        'winner': 'Gujarat Titans'},
            'overs': 20,
            'POTM': 'Rashid Khan',
            'Playing XIs': {
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
CSKvsGT = GTvsCSK

#Match 2 - PBKS vs KKR
PBKS_vs_KKR = [
    {
        'Match Number': 2,
        'info': {
            'city': 'Chandigarh',
            'competition': 'IPL',
            'dates': ['2023-04-01'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 7
                },
                'method': 'D/L',
                'winner': 'Punjab Kings'
            },
            'overs': 20,
            'POTM': ['Arshdeep Singh'],
            'Playing XIs': {
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
PBKSvsKKR = PBKS_vs_KKR
KKRvsPBKS = PBKS_vs_KKR

#Match 3 - LSG vs DC
LSG_vs_DC = [
    {
        'Match Number': 3,
        'info': {
            'city': 'Lucknow',
            'competition': 'IPL',
            'dates': ['2023-04-01'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 50
                },
                'winner': 'Lucknow Super Giants'
            },
            'overs': 20,
            'POTM': ['MA Wood'],
            'Playing XIs': {
                'Lucknow Super Giants': [
                    'KL Rahul',
                    'KR Mayers',
                    'DJ Hooda',
                    'KH Pandya',
                    'MP Stoinis',
                    'N Pooran',
                    'A Badoni',
                    'K Gowtham',
                    'Avesh Khan',
                    'Ravi Bishnoi',
                    'JD Unadkat',
                    'MA Wood'
                ],
                'Delhi Capitals': [
                    'KK Ahmed',
                    'PP Shaw',
                    'DA Warner',
                    'MR Marsh',
                    'SN Khan',
                    'RR Rossouw',
                    'R Powell',
                    'Aman Hakim Khan',
                    'AR Patel',
                    'Kuldeep Yadav',
                    'C Sakariya',
                    'Mukesh Kumar'
                ]
            }
        }
    },
]
LSGvsDC = LSG_vs_DC
DCvsLSG = LSG_vs_DC

#Match 4 - RR vs SRH
RR_vs_SRH = [
    {
        'Match Number': 4,
        'info': {
            'city': 'Hyderabad',
            'competition': 'IPL',
            'dates': ['2023-04-02'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 72
                },
                'winner': 'Rajasthan Royals'
            },
            'overs': 20,
            'POTM': ['JC Buttler'],
            'Playing XIs': {
                'Rajasthan Royals': [
                    'NA Saini',
                    'YBK Jaiswal',
                    'JC Buttler',
                    'SV Samson',
                    'D Padikkal',
                    'R Parag',
                    'SO Hetmyer',
                    'R Ashwin',
                    'JO Holder',
                    'TA Boult',
                    'KM Asif',
                    'YS Chahal'
                ],
                'Sunrisers Hyderabad': [
                    'Fazalhaq Farooqi',
                    'Abhishek Sharma',
                    'MA Agarwal',
                    'RA Tripathi',
                    'HC Brook',
                    'Washington Sundar',
                    'GD Phillips',
                    'Abdul Samad',
                    'AU Rashid',
                    'B Kumar',
                    'Umran Malik',
                    'T Natarajan'
                ]
            }
        }
    },
]
RRvsSRH = RR_vs_SRH
SRHvsRR = RR_vs_SRH

#Match 5 - MI vs RCB
MI_vs_RCB = [
    {
        'Match Number': 5,
        'info': {
            'city': 'Bengaluru',
            'competition': 'IPL',
            'dates': ['2023-04-02'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 8
                },
                'winner': 'Royal Challengers Bangalore'
            },
            'overs': 20,
            'POTM': ['F du Plessis'],
            'Playing XIs': {
                'Mumbai Indians': [
                    'JP Behrendorff',
                    'RG Sharma',
                    'Ishan Kishan',
                    'C Green',
                    'SA Yadav',
                    'Tilak Varma',
                    'N Wadhera',
                    'TH David',
                    'HR Shokeen',
                    'Arshad Khan',
                    'PP Chawla',
                    'JC Archer'
                ],
                'Royal Challengers Bangalore': [
                    'V Kohli',
                    'F du Plessis',
                    'KD Karthik',
                    'GJ Maxwell',
                    'MG Bracewell',
                    'Shahbaz Ahmed',
                    'HV Patel',
                    'Akash Deep',
                    'RJW Topley',
                    'Mohammed Siraj',
                    'KV Sharma'
                ]
            }
        }
    },
]
MIvsRCB = MI_vs_RCB
RCBvsMI = MI_vs_RCB

#Match 6 - CSK vs LSG
CSK_vs_LSG = [
    {
        'Match Number': 6,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-04-03'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 12
                },
                'winner': 'Chennai Super Kings'
            },
            'overs': 20,
            'POTM': ['MM Ali'],
            'Playing XIs': {
                'Chennai Super Kings': [
                    'TU Deshpande',
                    'RD Gaikwad',
                    'DP Conway',
                    'S Dube',
                    'MM Ali',
                    'BA Stokes',
                    'AT Rayudu',
                    'RA Jadeja',
                    'MS Dhoni',
                    'MJ Santner',
                    'DL Chahar',
                    'RS Hangargekar'
                ],
                'Lucknow Super Giants': [
                    'Avesh Khan',
                    'KL Rahul',
                    'KR Mayers',
                    'DJ Hooda',
                    'KH Pandya',
                    'MP Stoinis',
                    'N Pooran',
                    'A Badoni',
                    'K Gowtham',
                    'MA Wood',
                    'Yash Thakur',
                    'Ravi Bishnoi'
                ]
            }
        }
    },
]
CSKvsLSG = CSK_vs_LSG
LSGvsCSK = CSK_vs_LSG

#Match 7 - DC vs GT
DC_vs_GT = [
    {
        'Match Number': 7,
        'info': {
            'city': 'Delhi',
            'competition': 'IPL',
            'dates': ['2023-04-04'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 6
                },
                'winner': 'Gujarat Titans'
            },
            'overs': 20,
            'POTM': ['B Sai Sudharsan'],
            'Playing XIs': {
                'Delhi Capitals': [
                    'KK Ahmed',
                    'DA Warner',
                    'PP Shaw',
                    'MR Marsh',
                    'SN Khan',
                    'RR Rossouw',
                    'Abishek Porel',
                    'AR Patel',
                    'Aman Hakim Khan',
                    'Kuldeep Yadav',
                    'A Nortje',
                    'Mukesh Kumar'
                ],
                'Gujarat Titans': [
                    'J Little',
                    'WP Saha',
                    'Shubman Gill',
                    'B Sai Sudharsan',
                    'HH Pandya',
                    'V Shankar',
                    'DA Miller',
                    'R Tewatia',
                    'Rashid Khan',
                    'AS Joseph',
                    'Yash Dayal',
                    'Mohammed Shami'
                ]
            }
        }
    },
]
DCvsGT = DC_vs_GT
GTvsDC = DC_vs_GT

#Match 8 - PBKS vs RR
PBKS_vs_RR = [
    {
        'Match Number': 8,
        'info': {
            'city': 'Guwahati',
            'competition': 'IPL',
            'dates': ['2023-04-05'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 5
                },
                'winner': 'Punjab Kings'
            },
            'overs': 20,
            'POTM': ['NT Ellis'],
            'Playing XIs': {
                'Punjab Kings': [
                    'P Simran Singh',
                    'S Dhawan',
                    'PBB Rajapaksa',
                    'JM Sharma',
                    'Sikandar Raza',
                    'M Shahrukh Khan',
                    'SM Curran',
                    'Harpreet Brar',
                    'NT Ellis',
                    'RD Chahar',
                    'Arshdeep Singh',
                    'R Dhawan'
                ],
                'Rajasthan Royals': [
                    'YBK Jaiswal',
                    'R Ashwin',
                    'JC Buttler',
                    'SV Samson',
                    'D Padikkal',
                    'R Parag',
                    'SO Hetmyer',
                    'Dhruv Jurel',
                    'JO Holder',
                    'YS Chahal',
                    'TA Boult',
                    'KM Asif'
                ]
            }
        }
    },
]
PBKSvsRR = PBKS_vs_RR 
RRvsPBKS = PBKS_vs_RR 


KKR_vs_RCB = [
    {
        'Match Number': 9,
        'info': {
            'city': 'Kolkata',
            'competition': 'IPL',
            'dates': ['2023-04-06'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 81
                },
                'winner': 'Kolkata Knight Riders'
            },
            'overs': 20,
            'POTM': ['SN Thakur'],
            'Playing XIs': {
                'Kolkata Knight Riders': [
                    'Suyash Sharma',
                    'Rahmanullah Gurbaz',
                    'VR Iyer',
                    'Mandeep Singh',
                    'N Rana',
                    'RK Singh',
                    'AD Russell',
                    'SN Thakur',
                    'SP Narine',
                    'UT Yadav',
                    'TG Southee',
                    'CV Varun'
                ],
                'Royal Challengers Bangalore': [
                    'Mohammed Siraj',
                    'V Kohli',
                    'F du Plessis',
                    'MG Bracewell',
                    'GJ Maxwell',
                    'HV Patel',
                    'Shahbaz Ahmed',
                    'KD Karthik',
                    'Anuj Rawat',
                    'DJ Willey',
                    'KV Sharma',
                    'Akash Deep'
                ]
            }
        }
    },
]
KKRvsRCB = KKR_vs_RCB
RCBvsKKR = KKR_vs_RCB

SRH_vs_LSG = [
    {
        'Match Number': 10,
        'info': {
            'city': 'Lucknow',
            'competition': 'IPL',
            'dates': ['2023-04-07'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 5
                },
                'winner': 'Lucknow Super Giants'
            },
            'overs': 20,
            'POTM': ['KH Pandya'],
            'Playing XIs': {
                'Sunrisers Hyderabad': [
                    'Fazalhaq Farooqi',
                    'Anmolpreet Singh',
                    'MA Agarwal',
                    'RA Tripathi',
                    'AK Markram',
                    'HC Brook',
                    'Washington Sundar',
                    'Abdul Samad',
                    'AU Rashid',
                    'Umran Malik',
                    'B Kumar',
                    'T Natarajan'
                ],
                'Lucknow Super Giants': [
                    'A Mishra',
                    'KR Mayers',
                    'KL Rahul',
                    'DJ Hooda',
                    'KH Pandya',
                    'MP Stoinis',
                    'R Shepherd',
                    'N Pooran',
                    'Yash Thakur',
                    'JD Unadkat',
                    'Ravi Bishnoi',
                    'A Badoni'
                ]
            }
        }
    },
]
SRHvsLSG = SRH_vs_LSG
LSGvsSRH = SRH_vs_LSG

RR_vs_DC = [
    {
        'Match Number': 11,
        'info': {
            'city': 'Guwahati',
            'competition': 'IPL',
            'dates': ['2023-04-08'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 57
                },
                'winner': 'Rajasthan Royals'
            },
            'overs': 20,
            'POTM': ['YBK Jaiswal'],
            'Playing XIs': {
                'Rajasthan Royals': [
                    'M Ashwin',
                    'YBK Jaiswal',
                    'JC Buttler',
                    'SV Samson',
                    'R Parag',
                    'SO Hetmyer',
                    'Dhruv Jurel',
                    'JO Holder',
                    'R Ashwin',
                    'YS Chahal',
                    'TA Boult',
                    'Sandeep Sharma'
                ],
                'Delhi Capitals': [
                    'KK Ahmed',
                    'PP Shaw',
                    'DA Warner',
                    'MK Pandey',
                    'RR Rossouw',
                    'Lalit Yadav',
                    'AR Patel',
                    'R Powell',
                    'Abishek Porel',
                    'Kuldeep Yadav',
                    'A Nortje',
                    'Mukesh Kumar'
                ]
            }
        }
    },
]
RRvsDC = RR_vs_DC
DCvsRR = RR_vs_DC

MI_vs_CSK = [
    {
        'Match Number': 12,
        'info': {
            'city': 'Mumbai',
            'competition': 'IPL',
            'dates': ['2023-04-08'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 7
                },
                'winner': 'Chennai Super Kings'
            },
            'overs': 20,
            'POTM': ['RA Jadeja'],
            'Playing XIs': {
                'Mumbai Indians': [
                    'K Kartikeya',
                    'RG Sharma',
                    'Ishan Kishan',
                    'C Green',
                    'SA Yadav',
                    'Tilak Varma',
                    'Arshad Khan',
                    'TH David',
                    'T Stubbs',
                    'HR Shokeen',
                    'PP Chawla',
                    'JP Behrendorff'
                ],
                'Chennai Super Kings': [
                    'DL Chahar',
                    'DP Conway',
                    'RD Gaikwad',
                    'AM Rahane',
                    'S Dube',
                    'AT Rayudu',
                    'RA Jadeja',
                    'MS Dhoni',
                    'D Pretorius',
                    'MJ Santner',
                    'SSB Magala',
                    'TU Deshpande'
                ]
            }
        }
    },
]
MIvsCSK = MI_vs_CSK
CSKvsMI = MI_vs_CSK

GT_vs_KKR = [
    {
        'Match Number': 13,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-04-09'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 3
                },
                'winner': 'Kolkata Knight Riders'
            },
            'overs': 20,
            'POTM': ['RK Singh'],
            'Playing XIs': {
                'Gujarat Titans': [
                    'J Little',
                    'WP Saha',
                    'Shubman Gill',
                    'B Sai Sudharsan',
                    'A Manohar',
                    'V Shankar',
                    'DA Miller',
                    'R Tewatia',
                    'Rashid Khan',
                    'AS Joseph',
                    'Mohammed Shami',
                    'Yash Dayal'
                ],
                'Kolkata Knight Riders': [
                    'Suyash Sharma',
                    'Rahmanullah Gurbaz',
                    'N Jagadeesan',
                    'VR Iyer',
                    'N Rana',
                    'RK Singh',
                    'AD Russell',
                    'SP Narine',
                    'SN Thakur',
                    'UT Yadav',
                    'LH Ferguson',
                    'CV Varun'
                ]
            }
        }
    },
]
GTvsKKR = GT_vs_KKR
KKRvsGT = GT_vs_KKR

PBKS_vs_SRH = [
    {
        'Match Number': 14,
        'info': {
            'city': 'Hyderabad',
            'competition': 'IPL',
            'dates': ['2023-04-09'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 8
                },
                'winner': 'Sunrisers Hyderabad'
            },
            'overs': 20,
            'POTM': ['S Dhawan'],
            'Playing XIs': {
                'Punjab Kings': [
                    'P Simran Singh',
                    'S Dhawan',
                    'MW Short',
                    'JM Sharma',
                    'SM Curran',
                    'Sikandar Raza',
                    'M Shahrukh Khan',
                    'Harpreet Brar',
                    'RD Chahar',
                    'NT Ellis',
                    'Mohit Rathee',
                    'Arshdeep Singh'
                ],
                'Sunrisers Hyderabad': [
                    'HC Brook',
                    'MA Agarwal',
                    'RA Tripathi',
                    'AK Markram',
                    'H Klaasen',
                    'Washington Sundar',
                    'M Jansen',
                    'M Markande',
                    'B Kumar',
                    'Umran Malik',
                    'T Natarajan'
                ]
            }
        }
    },
]
PBKSvsSRH = PBKS_vs_SRH
SRHvsPBKS = PBKS_vs_SRH

RCB_vs_LSG = [
    {
        'Match Number': 15,
        'info': {
            'city': 'Bengaluru',
            'competition': 'IPL',
            'dates': ['2023-04-10'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 1
                },
                'winner': 'Lucknow Super Giants'
            },
            'overs': 20,
            'POTM': ['N Pooran'],
            'Playing XIs': {
                'Royal Challengers Bangalore': [
                    'Anuj Rawat',
                    'V Kohli',
                    'F du Plessis',
                    'GJ Maxwell',
                    'KD Karthik',
                    'MK Lomror',
                    'Shahbaz Ahmed',
                    'DJ Willey',
                    'WD Parnell',
                    'HV Patel',
                    'Mohammed Siraj',
                    'KV Sharma'
                ],
                'Lucknow Super Giants': [
                    'A Mishra',
                    'KR Mayers',
                    'KL Rahul',
                    'DJ Hooda',
                    'KH Pandya',
                    'MP Stoinis',
                    'N Pooran',
                    'A Badoni',
                    'JD Unadkat',
                    'MA Wood',
                    'Ravi Bishnoi',
                    'Avesh Khan'
                ]
            }
        }
    },
]
RCBvsLSG = RCB_vs_LSG
LSGvsRCB = RCB_vs_LSG

DC_vs_MI = [
    {
        'Match Number': 16,
        'info': {
            'city': 'Delhi',
            'competition': 'IPL',
            'dates': ['2023-04-11'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 6
                },
                'winner': 'Mumbai Indians'
            },
            'overs': 20,
            'POTM': ['RG Sharma'],
            'Playing XIs': {
                'Delhi Capitals': [
                    'Mukesh Kumar',
                    'DA Warner',
                    'PP Shaw',
                    'MK Pandey',
                    'YV Dhull',
                    'R Powell',
                    'Lalit Yadav',
                    'AR Patel',
                    'Abishek Porel',
                    'Kuldeep Yadav',
                    'A Nortje',
                    'Mustafizur Rahman'
                ],
                'Mumbai Indians': [
                    'RP Meredith',
                    'RG Sharma',
                    'Ishan Kishan',
                    'Tilak Varma',
                    'SA Yadav',
                    'TH David',
                    'C Green',
                    'N Wadhera',
                    'HR Shokeen',
                    'Arshad Khan',
                    'JP Behrendorff',
                    'PP Chawla'
                ]
            }
        }
    },
]
DCvsMI = DC_vs_MI
MIvsDC = DC_vs_MI

RR_vs_CSK = [
    {
        'Match Number': 17,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-04-12'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 3
                },
                'winner': 'Rajasthan Royals'
            },
            'overs': 20,
            'POTM': ['R Ashwin'],
            'Playing XIs': {
                'Rajasthan Royals': [
                    'YBK Jaiswal',
                    'JC Buttler',
                    'D Padikkal',
                    'SV Samson',
                    'R Ashwin',
                    'SO Hetmyer',
                    'Dhruv Jurel',
                    'JO Holder',
                    'A Zampa',
                    'KR Sen',
                    'Sandeep Sharma',
                    'YS Chahal'
                ],
                'Chennai Super Kings': [
                    'RD Gaikwad',
                    'DP Conway',
                    'AM Rahane',
                    'S Dube',
                    'MM Ali',
                    'AT Rayudu',
                    'RA Jadeja',
                    'MS Dhoni',
                    'SSB Magala',
                    'TU Deshpande',
                    'M Theekshana',
                    'Akash Singh'
                ]
            }
        }
    },
]
RRvsCSK = RR_vs_CSK
CSKvsRR = RR_vs_CSK

PBKS_vs_GT = [
    {
        'Match Number': 18,
        'info': {
            'city': 'Chandigarh',
            'competition': 'IPL',
            'dates': ['2023-04-13'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 6
                },
                'winner': 'Gujarat Titans'
            },
            'overs': 20,
            'POTM': ['MM Sharma'],
            'Playing XIs': {
                'Punjab Kings': [
                    'RD Chahar',
                    'P Simran Singh',
                    'S Dhawan',
                    'MW Short',
                    'PBB Rajapaksa',
                    'JM Sharma',
                    'SM Curran',
                    'M Shahrukh Khan',
                    'Harpreet Brar',
                    'R Dhawan',
                    'K Rabada',
                    'Arshdeep Singh'
                ],
                'Gujarat Titans': [
                    'WP Saha',
                    'Shubman Gill',
                    'B Sai Sudharsan',
                    'HH Pandya',
                    'DA Miller',
                    'R Tewatia',
                    'Rashid Khan',
                    'AS Joseph',
                    'Mohammed Shami',
                    'MM Sharma',
                    'J Little'
                ]
            }
        }
    },
]
PBKSvsGT = PBKS_vs_GT
GTvsPBKS = PBKS_vs_GT

KKR_vs_SRH = [
    {
        'Match Number': 19,
        'info': {
            'city': 'Kolkata',
            'competition': 'IPL',
            'dates': ['2023-04-14'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 23
                },
                'winner': 'Sunrisers Hyderabad'
            },
            'overs': 20,
            'POTM': ['HC Brook'],
            'Playing XIs': {
                'Sunrisers Hyderabad': [
                    'Washington Sundar',
                    'HC Brook',
                    'MA Agarwal',
                    'RA Tripathi',
                    'AK Markram',
                    'Abhishek Sharma',
                    'H Klaasen',
                    'M Jansen',
                    'M Markande',
                    'B Kumar',
                    'Umran Malik',
                    'T Natarajan'
                ],
                'Kolkata Knight Riders': [
                    'Suyash Sharma',
                    'Rahmanullah Gurbaz',
                    'N Jagadeesan',
                    'VR Iyer',
                    'SP Narine',
                    'N Rana',
                    'AD Russell',
                    'RK Singh',
                    'SN Thakur',
                    'UT Yadav',
                    'LH Ferguson',
                    'CV Varun'
                ]
            }
        }
    },
]
KKRvsSRH = KKR_vs_SRH
SRHvsKKR = KKR_vs_SRH

RCB_vs_DC = [
    {
        'Match Number': 20,
        'info': {
            'city': 'Bengaluru',
            'competition': 'IPL',
            'dates': ['2023-04-15'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 23
                },
                'winner': 'Royal Challengers Bangalore'
            },
            'overs': 20,
            'POTM': ['V Kohli'],
            'Playing XIs': {
                'Royal Challengers Bangalore': [
                    'V Kohli',
                    'F du Plessis',
                    'MK Lomror',
                    'GJ Maxwell',
                    'HV Patel',
                    'Shahbaz Ahmed',
                    'KD Karthik',
                    'Anuj Rawat',
                    'PWH de Silva',
                    'WD Parnell',
                    'Mohammed Siraj',
                    'Vijaykumar Vyshak'
                ],
                'Delhi Capitals': [
                    'DA Warner',
                    'PP Shaw',
                    'MR Marsh',
                    'YV Dhull',
                    'MK Pandey',
                    'Abishek Porel',
                    'AR Patel',
                    'Aman Hakim Khan',
                    'Lalit Yadav',
                    'A Nortje',
                    'Kuldeep Yadav',
                    'Mustafizur Rahman'
                ]
            }
        }
    },
]
RCBvsDC = RCB_vs_DC
DCvsRCB = RCB_vs_DC

LSG_vs_PBKS = [
    {
        'Match Number': 21,
        'info': {
            'city': 'Lucknow',
            'competition': 'IPL',
            'dates': ['2023-04-15'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 2
                },
                'winner': 'Punjab Kings'
            },
            'overs': 20,
            'POTM': ['Sikandar Raza'],
            'Playing XIs': {
                'Lucknow Super Giants': [
                    'KL Rahul',
                    'KR Mayers',
                    'DJ Hooda',
                    'KH Pandya',
                    'N Pooran',
                    'MP Stoinis',
                    'A Badoni',
                    'K Gowtham',
                    'Yudhvir Singh',
                    'Ravi Bishnoi',
                    'Avesh Khan',
                    'MA Wood'
                ],
                'Punjab Kings': [
                    'Atharva Taide',
                    'P Simran Singh',
                    'MW Short',
                    'Harpreet Singh',
                    'Sikandar Raza',
                    'SM Curran',
                    'JM Sharma',
                    'M Shahrukh Khan',
                    'Harpreet Brar',
                    'K Rabada',
                    'RD Chahar',
                    'Arshdeep Singh'
                ]
            }
        }
    },
]
LSGvsPBKS = LSG_vs_PBKS
PBKSvsLSG = LSG_vs_PBKS

KKR_vs_MI = [
    {
        'Match Number': 22,
        'info': {
            'city': 'Mumbai',
            'competition': 'IPL',
            'dates': ['2023-04-16'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 5
                },
                'winner': 'Mumbai Indians'
            },
            'overs': 20,
            'POTM': ['VR Iyer'],
            'Playing XIs': {
                'Kolkata Knight Riders': [
                    'Suyash Sharma',
                    'Rahmanullah Gurbaz',
                    'N Jagadeesan',
                    'VR Iyer',
                    'N Rana',
                    'SN Thakur',
                    'RK Singh',
                    'AD Russell',
                    'SP Narine',
                    'UT Yadav',
                    'LH Ferguson',
                    'CV Varun'
                ],
                'Mumbai Indians': [
                    'RP Meredith',
                    'RG Sharma',
                    'Ishan Kishan',
                    'SA Yadav',
                    'Tilak Varma',
                    'TH David',
                    'N Wadhera',
                    'C Green',
                    'Arjun Tendulkar',
                    'HR Shokeen',
                    'PP Chawla',
                    'D Jansen'
                ]
            }
        }
    },
]
KKRvsMI = KKR_vs_MI
MIvsKKR = KKR_vs_MI

GT_vs_RR = [
    {
        'Match Number': 23,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-04-16'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 3
                },
                'winner': 'Rajasthan Royals'
            },
            'overs': 20,
            'POTM': ['SO Hetmyer'],
            'Playing XIs': {
                'Gujarat Titans': [
                    'Noor Ahmad',
                    'WP Saha',
                    'Shubman Gill',
                    'B Sai Sudharsan',
                    'HH Pandya',
                    'DA Miller',
                    'A Manohar',
                    'R Tewatia',
                    'Rashid Khan',
                    'AS Joseph',
                    'Mohammed Shami',
                    'MM Sharma'
                ],
                'Rajasthan Royals': [
                    'YS Chahal',
                    'YBK Jaiswal',
                    'JC Buttler',
                    'D Padikkal',
                    'SV Samson',
                    'R Parag',
                    'SO Hetmyer',
                    'Dhruv Jurel',
                    'R Ashwin',
                    'TA Boult',
                    'Sandeep Sharma',
                    'A Zampa'
                ]
            }
        }
    },
]
GTvsRR = GT_vs_RR
RRvsGT = GT_vs_RR

CSK_vs_RCB = [
    {
        'Match Number': 24,
        'info': {
            'city': 'Bengaluru',
            'competition': 'IPL',
            'dates': ['2023-04-17'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 8
                },
                'winner': 'Chennai Super Kings'
            },
            'overs': 20,
            'POTM': ['DP Conway'],
            'Playing XIs': {
                'Chennai Super Kings': [
                    'RD Gaikwad',
                    'DP Conway',
                    'AM Rahane',
                    'S Dube',
                    'AT Rayudu',
                    'MM Ali',
                    'RA Jadeja',
                    'MS Dhoni',
                    'TU Deshpande',
                    'M Theekshana',
                    'M Pathirana',
                    'Akash Singh'
                ],
                'Royal Challengers Bangalore': [
                    'V Kohli',
                    'F du Plessis',
                    'MK Lomror',
                    'GJ Maxwell',
                    'Shahbaz Ahmed',
                    'KD Karthik',
                    'SS Prabhudessai',
                    'WD Parnell',
                    'PWH de Silva',
                    'HV Patel',
                    'Mohammed Siraj',
                    'Vijaykumar Vyshak'
                ]
            }
        }
    },
]
CSKvsRCB = CSK_vs_RCB
RCBvsCSK = CSK_vs_RCB

MI_vs_SRH = [
    {
        'Match Number': 25,
        'info': {
            'city': 'Hyderabad',
            'competition': 'IPL',
            'dates': ['2023-04-18'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 14
                },
                'winner': 'Mumbai Indians'
            },
            'overs': 20,
            'POTM': ['C Green'],
            'Playing XIs': {
                'Mumbai Indians': [
                    'RP Meredith',
                    'RG Sharma',
                    'Ishan Kishan',
                    'C Green',
                    'SA Yadav',
                    'Tilak Varma',
                    'TH David',
                    'N Wadhera',
                    'Arjun Tendulkar',
                    'HR Shokeen',
                    'PP Chawla',
                    'JP Behrendorff'
                ],
                'Sunrisers Hyderabad': [
                    'T Natarajan',
                    'HC Brook',
                    'MA Agarwal',
                    'RA Tripathi',
                    'AK Markram',
                    'Abhishek Sharma',
                    'H Klaasen',
                    'Abdul Samad',
                    'M Jansen',
                    'Washington Sundar',
                    'B Kumar',
                    'M Markande'
                ]
            }
        }
    },
]
MIvsSRH = MI_vs_SRH
SRHvsMI = MI_vs_SRH

LSG_vs_RR = [
    {
        'Match Number': 26,
        'info': {
            'city': 'Jaipur',
            'competition': 'IPL',
            'dates': ['2023-04-19'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 10
                },
                'winner': 'Lucknow Super Giants'
            },
            'overs': 20,
            'POTM': ['MP Stoinis'],
            'Playing XIs': {
                'Lucknow Super Giants': [
                    'A Mishra',
                    'KL Rahul',
                    'KR Mayers',
                    'A Badoni',
                    'DJ Hooda',
                    'MP Stoinis',
                    'N Pooran',
                    'KH Pandya',
                    'Yudhvir Singh',
                    'Naveen-ul-Haq',
                    'Ravi Bishnoi',
                    'Avesh Khan'
                ],
                'Rajasthan Royals': [
                    'YS Chahal',
                    'YBK Jaiswal',
                    'JC Buttler',
                    'SV Samson',
                    'D Padikkal',
                    'SO Hetmyer',
                    'R Parag',
                    'Dhruv Jurel',
                    'R Ashwin',
                    'JO Holder',
                    'TA Boult',
                    'Sandeep Sharma'
                ]
            }
        }
    },
]
LSGvsRR = LSG_vs_RR
RRvsLSG = LSG_vs_RR

RCB_vs_PBKS = [
    {
        'Match Number': 27,
        'info': {
            'city': 'Chandigarh',
            'competition': 'IPL',
            'dates': ['2023-04-20'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 24
                },
                'winner': 'Royal Challengers Bangalore'
            },
            'overs': 20,
            'POTM': ['Mohammed Siraj'],
            'Playing XIs': {
                'Royal Challengers Bangalore': [
                    'Vijaykumar Vyshak',
                    'V Kohli',
                    'F du Plessis',
                    'GJ Maxwell',
                    'KD Karthik',
                    'MK Lomror',
                    'Shahbaz Ahmed',
                    'SS Prabhudessai',
                    'PWH de Silva',
                    'HV Patel',
                    'WD Parnell',
                    'Mohammed Siraj'
                ],
                'Punjab Kings': [
                    'RD Chahar',
                    'Atharva Taide',
                    'P Simran Singh',
                    'MW Short',
                    'LS Livingstone',
                    'Harpreet Singh',
                    'SM Curran',
                    'JM Sharma',
                    'M Shahrukh Khan',
                    'Harpreet Brar',
                    'NT Ellis',
                    'Arshdeep Singh'
                ]
            }
        }
    },
]
RCBvsPBKS = RCB_vs_PBKS
PBKSvsRCB = RCB_vs_PBKS

KKR_vs_DC = [
    {
        'Match Number': 28,
        'info': {
            'city': 'Delhi',
            'competition': 'IPL',
            'dates': ['2023-04-20'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 4
                },
                'winner': 'Delhi Capitals'
            },
            'overs': 20,
            'POTM': ['I Sharma'],
            'Playing XIs': {
                'Kolkata Knight Riders': [
                    'JJ Roy',
                    'Liton Das',
                    'VR Iyer',
                    'N Rana',
                    'Mandeep Singh',
                    'RK Singh',
                    'SP Narine',
                    'AD Russell',
                    'AS Roy',
                    'UT Yadav',
                    'CV Varun',
                    'K Khejroliya'
                ],
                'Delhi Capitals': [
                    'I Sharma',
                    'DA Warner',
                    'PP Shaw',
                    'MR Marsh',
                    'PD Salt',
                    'MK Pandey',
                    'AR Patel',
                    'Aman Hakim Khan',
                    'Lalit Yadav',
                    'Mukesh Kumar',
                    'Kuldeep Yadav',
                    'A Nortje'
                ]
            }
        }
    },
]
KKRvsDC = KKR_vs_DC
DCvsKKR = KKR_vs_DC

SRH_vs_CSK = [
    {
        'Match Number': 29,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-04-21'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 7
                },
                'winner': 'Chennai Super Kings'
            },
            'overs': 20,
            'POTM': ['RA Jadeja'],
            'Playing XIs': {
                'Sunrisers Hyderabad': [
                    'Mayank Dagar',
                    'HC Brook',
                    'Abhishek Sharma',
                    'RA Tripathi',
                    'AK Markram',
                    'H Klaasen',
                    'MA Agarwal',
                    'M Jansen',
                    'Washington Sundar',
                    'B Kumar',
                    'M Markande',
                    'Umran Malik'
                ],
                'Chennai Super Kings': [
                    'Akash Singh',
                    'RD Gaikwad',
                    'DP Conway',
                    'AM Rahane',
                    'AT Rayudu',
                    'MM Ali',
                    'S Dube',
                    'RA Jadeja',
                    'MS Dhoni',
                    'TU Deshpande',
                    'M Theekshana',
                    'M Pathirana'
                ]
            }
        }
    },
]
SRHvsCSK = SRH_vs_CSK
CSKvsSRH = SRH_vs_CSK

GT_vs_LSG = [
    {
        'Match Number': 30,
        'info': {
            'city': 'Lucknow',
            'competition': 'IPL',
            'dates': ['2023-04-22'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 7
                },
                'winner': 'Gujarat Titans'
            },
            'overs': 20,
            'POTM': ['MM Sharma'],
            'Playing XIs': {
                'Gujarat Titans': [
                    'J Yadav',
                    'WP Saha',
                    'Shubman Gill',
                    'HH Pandya',
                    'A Manohar',
                    'V Shankar',
                    'DA Miller',
                    'R Tewatia',
                    'Rashid Khan',
                    'Mohammed Shami',
                    'Noor Ahmad',
                    'MM Sharma'
                ],
                'Lucknow Super Giants': [
                    'A Mishra',
                    'KL Rahul',
                    'KR Mayers',
                    'KH Pandya',
                    'N Pooran',
                    'A Badoni',
                    'MP Stoinis',
                    'DJ Hooda',
                    'PN Mankad',
                    'Ravi Bishnoi',
                    'Avesh Khan',
                    'Naveen-ul-Haq'
                ]
            }
        }
    },
]
GTvsLSG = GT_vs_LSG
LSGvsGT = GT_vs_LSG

PBKS_vs_MI = [
    {
        'Match Number': 31,
        'info': {
            'city': 'Mumbai',
            'competition': 'IPL',
            'dates': ['2023-04-22'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 13
                },
                'winner': 'Punjab Kings'
            },
            'overs': 20,
            'POTM': ['SM Curran'],
            'Playing XIs': {
                'Punjab Kings': [
                    'NT Ellis',
                    'MW Short',
                    'P Simran Singh',
                    'Atharva Taide',
                    'LS Livingstone',
                    'Harpreet Singh',
                    'SM Curran',
                    'JM Sharma',
                    'M Shahrukh Khan',
                    'Harpreet Brar',
                    'Arshdeep Singh',
                    'RD Chahar'
                ],
                'Mumbai Indians': [
                    'JP Behrendorff',
                    'RG Sharma',
                    'Ishan Kishan',
                    'C Green',
                    'SA Yadav',
                    'TH David',
                    'Tilak Varma',
                    'N Wadhera',
                    'JC Archer',
                    'Arjun Tendulkar',
                    'HR Shokeen',
                    'PP Chawla'
                ]
            }
        }
    },
]
PBKSvsMI = PBKS_vs_MI
MIvsPBKS = PBKS_vs_MI

RCB_vs_RR = [
    {
        'Match Number': 32,
        'info': {
            'city': 'Bengaluru',
            'competition': 'IPL',
            'dates': ['2023-04-23'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 7
                },
                'winner': 'Royal Challengers Bangalore'
            },
            'overs': 20,
            'POTM': ['GJ Maxwell'],
            'Playing XIs': {
                'Royal Challengers Bangalore': [
                    'HV Patel',
                    'V Kohli',
                    'F du Plessis',
                    'Shahbaz Ahmed',
                    'GJ Maxwell',
                    'MK Lomror',
                    'KD Karthik',
                    'SS Prabhudessai',
                    'PWH de Silva',
                    'DJ Willey',
                    'Vijaykumar Vyshak',
                    'Mohammed Siraj'
                ],
                'Rajasthan Royals': [
                    'YBK Jaiswal',
                    'JC Buttler',
                    'D Padikkal',
                    'SV Samson',
                    'SO Hetmyer',
                    'Dhruv Jurel',
                    'R Ashwin',
                    'Abdul Basith',
                    'JO Holder',
                    'TA Boult',
                    'Sandeep Sharma',
                    'YS Chahal'
                ]
            }
        }
    },
]
RCBvsRR = RCB_vs_RR
RRvsRCB = RCB_vs_RR

CSK_vs_KKR = [
    {
        'Match Number': 33,
        'info': {
            'city': 'Kolkata',
            'competition': 'IPL',
            'dates': ['2023-04-23'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 49
                },
                'winner': 'Chennai Super Kings'
            },
            'overs': 20,
            'POTM': ['AM Rahane'],
            'Playing XIs': {
                'Chennai Super Kings': [
                    'Akash Singh',
                    'RD Gaikwad',
                    'DP Conway',
                    'AM Rahane',
                    'S Dube',
                    'RA Jadeja',
                    'MS Dhoni',
                    'MM Ali',
                    'AT Rayudu',
                    'M Pathirana',
                    'TU Deshpande',
                    'M Theekshana'
                ],
                'Kolkata Knight Riders': [
                    'Suyash Sharma',
                    'N Jagadeesan',
                    'SP Narine',
                    'VR Iyer',
                    'N Rana',
                    'JJ Roy',
                    'RK Singh',
                    'AD Russell',
                    'D Wiese',
                    'UT Yadav',
                    'CV Varun',
                    'K Khejroliya'
                ]
            }
        }
    },
]
CSKvsKKR = CSK_vs_KKR
KKRvsCSK = CSK_vs_KKR

DC_vs_SRH = [
    {
        'Match Number': 34,
        'info': {
            'city': 'Hyderabad',
            'competition': 'IPL',
            'dates': ['2023-04-24'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 7
                },
                'winner': 'Delhi Capitals'
            },
            'overs': 20,
            'POTM': ['AR Patel'],
            'Playing XIs': {
                'Delhi Capitals': [
                    'Mukesh Kumar',
                    'DA Warner',
                    'PD Salt',
                    'MR Marsh',
                    'SN Khan',
                    'MK Pandey',
                    'Aman Hakim Khan',
                    'AR Patel',
                    'RV Patel',
                    'A Nortje',
                    'Kuldeep Yadav',
                    'I Sharma'
                ],
                'Sunrisers Hyderabad': [
                    'T Natarajan',
                    'HC Brook',
                    'MA Agarwal',
                    'RA Tripathi',
                    'Abhishek Sharma',
                    'AK Markram',
                    'H Klaasen',
                    'Washington Sundar',
                    'M Jansen',
                    'M Markande',
                    'B Kumar',
                    'Umran Malik'
                ]
            }
        }
    },
]
DCvsSRH = DC_vs_SRH
SRHvsDC = DC_vs_SRH

GT_vs_MI = [
    {
        'Match Number': 35,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-04-25'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 55
                },
                'winner': 'Gujarat Titans'
            },
            'overs': 20,
            'POTM': ['A Manohar'],
            'Playing XIs': {
                'Gujarat Titans': [
                    'J Little',
                    'WP Saha',
                    'Shubman Gill',
                    'HH Pandya',
                    'V Shankar',
                    'DA Miller',
                    'A Manohar',
                    'R Tewatia',
                    'Rashid Khan',
                    'MM Sharma',
                    'Mohammed Shami',
                    'Noor Ahmad'
                ],
                'Mumbai Indians': [
                    'K Kartikeya',
                    'RG Sharma',
                    'Ishan Kishan',
                    'C Green',
                    'Tilak Varma',
                    'SA Yadav',
                    'TH David',
                    'N Wadhera',
                    'PP Chawla',
                    'Arjun Tendulkar',
                    'JP Behrendorff',
                    'RP Meredith'
                ]
            }
        }
    },
]
GTvsMI = GT_vs_MI
MIvsGT = GT_vs_MI

KKR_vs_RCB = [
    {
        'Match Number': 36,
        'info': {
            'city': 'Bengaluru',
            'competition': 'IPL',
            'dates': ['2023-04-26'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 21
                },
                'winner': 'Kolkata Knight Riders'
            },
            'overs': 20,
            'POTM': ['CV Varun'],
            'Playing XIs': {
                'Kolkata Knight Riders': [
                    'Suyash Sharma',
                    'JJ Roy',
                    'N Jagadeesan',
                    'VR Iyer',
                    'N Rana',
                    'AD Russell',
                    'RK Singh',
                    'D Wiese',
                    'SP Narine',
                    'VG Arora',
                    'UT Yadav',
                    'CV Varun'
                ],
                'Royal Challengers Bangalore': [
                    'HV Patel',
                    'V Kohli',
                    'F du Plessis',
                    'Shahbaz Ahmed',
                    'GJ Maxwell',
                    'MK Lomror',
                    'KD Karthik',
                    'SS Prabhudessai',
                    'PWH de Silva',
                    'DJ Willey',
                    'Vijaykumar Vyshak',
                    'Mohammed Siraj'
                ]
            }
        }
    },
]
KKRvsRCB2 = KKR_vs_RCB
RCBvsKKR2 = KKR_vs_RCB

RR_vs_CSK = [
    {
        'Match Number': 37,
        'info': {
            'city': 'Jaipur',
            'competition': 'IPL',
            'dates': ['2023-04-27'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 32
                },
                'winner': 'Rajasthan Royals'
            },
            'overs': 20,
            'POTM': ['YBK Jaiswal'],
            'Playing XIs': {
                'Rajasthan Royals': [
                    'K Yadav',
                    'YBK Jaiswal',
                    'JC Buttler',
                    'SV Samson',
                    'SO Hetmyer',
                    'Dhruv Jurel',
                    'D Padikkal',
                    'R Ashwin',
                    'JO Holder',
                    'Sandeep Sharma',
                    'YS Chahal',
                    'A Zampa'
                ],
                'Chennai Super Kings': [
                    'Akash Singh',
                    'RD Gaikwad',
                    'DP Conway',
                    'AM Rahane',
                    'S Dube',
                    'AT Rayudu',
                    'MM Ali',
                    'RA Jadeja',
                    'MS Dhoni',
                    'M Pathirana',
                    'TU Deshpande',
                    'M Theekshana'
                ]
            }
        }
    },
]
RRvsCSK2 = RR_vs_CSK
CSKvsRR2 = RR_vs_CSK

LSG_vs_PBKS = [
    {
        'Match Number': 38,
        'info': {
            'city': 'Chandigarh',
            'competition': 'IPL',
            'dates': ['2023-04-28'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 56
                },
                'winner': 'Lucknow Super Giants'
            },
            'overs': 20,
            'POTM': ['MP Stoinis'],
            'Playing XIs': {
                'Lucknow Super Giants': [
                    'A Mishra',
                    'KL Rahul',
                    'KR Mayers',
                    'A Badoni',
                    'MP Stoinis',
                    'N Pooran',
                    'DJ Hooda',
                    'KH Pandya',
                    'Naveen-ul-Haq',
                    'Ravi Bishnoi',
                    'Avesh Khan',
                    'Yash Thakur'
                ],
                'Punjab Kings': [
                    'Gurnoor Brar',
                    'P Simran Singh',
                    'S Dhawan',
                    'Atharva Taide',
                    'Sikandar Raza',
                    'LS Livingstone',
                    'SM Curran',
                    'JM Sharma',
                    'M Shahrukh Khan',
                    'RD Chahar',
                    'K Rabada',
                    'Arshdeep Singh'
                ]
            }
        }
    },
]
LSGvsPBKS2 = LSG_vs_PBKS
PBKSvsLSG2 = LSG_vs_PBKS

KKR_vs_GT = [
    {
        'Match Number': 39,
        'info': {
            'city': 'Kolkata',
            'competition': 'IPL',
            'dates': ['2023-04-29'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 7
                },
                'winner': 'Gujarat Titans'
            },
            'overs': 20,
            'POTM': ['J Little'],
            'Playing XIs': {
                'Kolkata Knight Riders': [
                    'Suyash Sharma',
                    'N Jagadeesan',
                    'Rahmanullah Gurbaz',
                    'SN Thakur',
                    'VR Iyer',
                    'N Rana',
                    'RK Singh',
                    'AD Russell',
                    'D Wiese',
                    'SP Narine',
                    'Harshit Rana',
                    'CV Varun'
                ],
                'Gujarat Titans': [
                    'MM Sharma',
                    'WP Saha',
                    'Shubman Gill',
                    'HH Pandya',
                    'V Shankar',
                    'DA Miller',
                    'A Manohar',
                    'R Tewatia',
                    'Rashid Khan',
                    'Noor Ahmad',
                    'Mohammed Shami',
                    'J Little'
                ]
            }
        }
    },
]
KKRvsGT = KKR_vs_GT
GTvsKKR = KKR_vs_GT

DC_vs_SRH = [
    {
        'Match Number': 40,
        'info': {
            'city': 'Delhi',
            'competition': 'IPL',
            'dates': ['2023-04-29'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 9
                },
                'winner': 'Sunrisers Hyderabad'
            },
            'overs': 20,
            'POTM': ['MR Marsh'],
            'Playing XIs': {
                'Sunrisers Hyderabad': [
                    'T Natarajan',
                    'Abhishek Sharma',
                    'MA Agarwal',
                    'RA Tripathi',
                    'AK Markram',
                    'HC Brook',
                    'H Klaasen',
                    'Abdul Samad',
                    'AJ Hosein',
                    'M Markande',
                    'B Kumar',
                    'Umran Malik'
                ],
                'Delhi Capitals': [
                    'I Sharma',
                    'DA Warner',
                    'PD Salt',
                    'MR Marsh',
                    'MK Pandey',
                    'PK Garg',
                    'SN Khan',
                    'AR Patel',
                    'RV Patel',
                    'Kuldeep Yadav',
                    'A Nortje',
                    'Mukesh Kumar'
                ]
            }
        }
    },
]
DCvsSRH2 = DC_vs_SRH
SRHvsDC2 = DC_vs_SRH

CSK_vs_PBKS = [
    {
        'Match Number': 41,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-04-30'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 4
                },
                'winner': 'Punjab Kings'
            },
            'overs': 20,
            'POTM': ['DP Conway'],
            'Playing XIs': {
                'Chennai Super Kings': [
                    'Akash Singh',
                    'RD Gaikwad',
                    'DP Conway',
                    'S Dube',
                    'MM Ali',
                    'RA Jadeja',
                    'MS Dhoni',
                    'AM Rahane',
                    'M Pathirana',
                    'TU Deshpande',
                    'M Theekshana',
                    'AT Rayudu'
                ],
                'Punjab Kings': [
                    'K Rabada',
                    'P Simran Singh',
                    'S Dhawan',
                    'Atharva Taide',
                    'LS Livingstone',
                    'SM Curran',
                    'JM Sharma',
                    'M Shahrukh Khan',
                    'Sikandar Raza',
                    'Harpreet Brar',
                    'RD Chahar',
                    'Arshdeep Singh'
                ]
            }
        }
    },
]
CSKvsPBKS = CSK_vs_PBKS
PBKSvsCSK = CSK_vs_PBKS

RR_vs_MI = [
    {
        'Match Number': 42,
        'info': {
            'city': 'Mumbai',
            'competition': 'IPL',
            'dates': ['2023-04-30'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 6
                },
                'winner': 'Mumbai Indians'
            },
            'overs': 20,
            'POTM': ['YBK Jaiswal'],
            'Playing XIs': {
                'Rajasthan Royals': [
                    'KR Sen',
                    'YBK Jaiswal',
                    'JC Buttler',
                    'SV Samson',
                    'D Padikkal',
                    'JO Holder',
                    'SO Hetmyer',
                    'Dhruv Jurel',
                    'R Ashwin',
                    'TA Boult',
                    'Sandeep Sharma',
                    'YS Chahal'
                ],
                'Mumbai Indians': [
                    'RG Sharma',
                    'Ishan Kishan',
                    'C Green',
                    'SA Yadav',
                    'Tilak Varma',
                    'TH David',
                    'PP Chawla',
                    'JC Archer',
                    'K Kartikeya',
                    'RP Meredith',
                    'Arshad Khan'
                ]
            }
        }
    },
]
RRvsMI = RR_vs_MI
MIvsRR = RR_vs_MI

RCB_vs_LSG = [
    {
        'Match Number': 43,
        'info': {
            'city': 'Lucknow',
            'competition': 'IPL',
            'dates': ['2023-05-01'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 18
                },
                'winner': 'Royal Challengers Bangalore'
            },
            'overs': 20,
            'POTM': ['F du Plessis'],
            'Playing XIs': {
                'Royal Challengers Bangalore': [
                    'V Kohli',
                    'F du Plessis',
                    'Anuj Rawat',
                    'GJ Maxwell',
                    'SS Prabhudessai',
                    'KD Karthik',
                    'MK Lomror',
                    'PWH de Silva',
                    'KV Sharma',
                    'Mohammed Siraj',
                    'JR Hazlewood',
                    'HV Patel'
                ],
                'Lucknow Super Giants': [
                    'KR Mayers',
                    'A Badoni',
                    'KH Pandya',
                    'DJ Hooda',
                    'MP Stoinis',
                    'N Pooran',
                    'K Gowtham',
                    'Ravi Bishnoi',
                    'A Mishra',
                    'Naveen-ul-Haq',
                    'KL Rahul',
                    'Yash Thakur'
                ]
            }
        }
    },
]
RCBvsLSG2 = RCB_vs_LSG
LSGvsRCB2 = RCB_vs_LSG

DC_vs_GT = [
    {
        'Match Number': 44,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-05-02'],

            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 5
                },
                'winner': 'Delhi Capitals'
            },
            'overs': 20,
            'POTM': ['Mohammed Shami'],
            'Playing XIs': {
                'Delhi Capitals': [
                    'KK Ahmed',
                    'PD Salt',
                    'DA Warner',
                    'PK Garg',
                    'RR Rossouw',
                    'MK Pandey',
                    'AR Patel',
                    'Aman Hakim Khan',
                    'RV Patel',
                    'A Nortje',
                    'Kuldeep Yadav',
                    'I Sharma'
                ],
                'Gujarat Titans': [
                    'MM Sharma',
                    'WP Saha',
                    'Shubman Gill',
                    'HH Pandya',
                    'V Shankar',
                    'DA Miller',
                    'A Manohar',
                    'R Tewatia',
                    'Rashid Khan',
                    'Noor Ahmad',
                    'Mohammed Shami',
                    'J Little'
                ]
            }
        }
    },
]
DCvsGT2 = DC_vs_GT
GTvsDC2 = DC_vs_GT

LSG_vs_CSK = [
    {
        'Match Number': 45,
        'info': {
            'city': 'Lucknow',
            'competition': 'IPL',
            'dates': ['2023-05-03'],

            'match_type': 'T20',
            'outcome': {
                'result': 'no result'
            },
            'overs': 20,
            'Playing XIs': {
                'Lucknow Super Giants': [
                    'M Vohra',
                    'KR Mayers',
                    'KS Sharma',
                    'KH Pandya',
                    'MP Stoinis',
                    'N Pooran',
                    'A Badoni',
                    'K Gowtham',
                    'Naveen-ul-Haq',
                    'Ravi Bishnoi',
                    'Mohsin Khan'
                ],
                'Chennai Super Kings': [
                    'AT Rayudu',
                    'RD Gaikwad',
                    'DP Conway',
                    'AM Rahane',
                    'MM Ali',
                    'S Dube',
                    'RA Jadeja',
                    'MS Dhoni',
                    'M Pathirana',
                    'TU Deshpande',
                    'M Theekshana',
                    'DL Chahar'
                ]
            }
        }
    },
]
LSGvsCSK = LSG_vs_CSK
CSKvsLSG = LSG_vs_CSK

PBKS_vs_MI = [
    {
        'Match Number': 46,
        'info': {
            'city': 'Chandigarh',
            'competition': 'IPL',
            'dates': ['2023-05-03'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Mumbai Indians',
                'by': {
                    'wickets': 6
                }
            },
            'overs': 20,
            'POTM': ['Ishan Kishan'],
            'Playing XIs': {
                'Punjab Kings': [
                    'NT Ellis',
                    'P Simran Singh',
                    'S Dhawan',
                    'MW Short',
                    'LS Livingstone',
                    'JM Sharma',
                    'SM Curran',
                    'M Shahrukh Khan',
                    'Harpreet Brar',
                    'R Dhawan',
                    'RD Chahar',
                    'Arshdeep Singh'
                ],
                'Mumbai Indians': [
                    'Akash Madhwal',
                    'RG Sharma',
                    'Ishan Kishan',
                    'C Green',
                    'SA Yadav',
                    'TH David',
                    'Tilak Varma',
                    'N Wadhera',
                    'PP Chawla',
                    'JC Archer',
                    'K Kartikeya',
                    'Arshad Khan'
                ]
            }
        }
    },
]
PBKSvsMI2 = PBKS_vs_MI
MIvsPBKS2 = PBKS_vs_MI

SRH_vs_KKR = [
    {
        'Match Number': 47,
        'info': {
            'city': 'Hyderabad',
            'competition': 'IPL',
            'dates': ['2023-05-04'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Kolkata Knight Riders',
                'by': {
                    'runs': 5
                }
            },
            'overs': 20,
            'POTM': ['CV Varun'],
            'Playing XIs': {
                'Kolkata Knight Riders': [
                    'JJ Roy',
                    'Rahmanullah Gurbaz',
                    'VR Iyer',
                    'N Rana',
                    'RK Singh',
                    'AD Russell',
                    'SP Narine',
                    'SN Thakur',
                    'AS Roy',
                    'Harshit Rana',
                    'VG Arora',
                    'CV Varun'
                ],
                'Sunrisers Hyderabad': [
                    'T Natarajan',
                    'Abhishek Sharma',
                    'MA Agarwal',
                    'RA Tripathi',
                    'AK Markram',
                    'HC Brook',
                    'H Klaasen',
                    'Abdul Samad',
                    'M Jansen',
                    'B Kumar',
                    'M Markande',
                    'Kartik Tyagi'
                ]
            }
        }
    },
]
SRHvsKKR = SRH_vs_KKR
KKRvsSRH = SRH_vs_KKR

RR_vs_GT = [
    {
        'Match Number': 48,
        'info': {
            'city': 'Jaipur',
            'competition': 'IPL',
            'dates': ['2023-05-05'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Gujarat Titans',
                'by': {
                    'wickets': 9
                }
            },
            'overs': 20,
            'POTM': ['Rashid Khan'],
            'Playing XIs': {
                'Rajasthan Royals': [
                    'YBK Jaiswal',
                    'JC Buttler',
                    'SV Samson',
                    'D Padikkal',
                    'R Ashwin',
                    'R Parag',
                    'SO Hetmyer',
                    'Dhruv Jurel',
                    'TA Boult',
                    'A Zampa',
                    'Sandeep Sharma',
                    'YS Chahal'
                ],
                'Gujarat Titans': [
                    'MM Sharma',
                    'WP Saha',
                    'Shubman Gill',
                    'HH Pandya',
                    'Rashid Khan',
                    'DA Miller',
                    'V Shankar',
                    'R Tewatia',
                    'A Manohar',
                    'Noor Ahmad',
                    'Mohammed Shami',
                    'J Little'
                ]
            }
        }
    },
]
RRvsGT = RR_vs_GT
GTvsRR = RR_vs_GT

MI_vs_CSK = [
    {
        'Match Number': 49,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-05-06'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Chennai Super Kings',
                'by': {
                    'wickets': 6
                }
            },
            'overs': 20,
            'POTM': ['M Pathirana'],
            'Playing XIs': {
                'Mumbai Indians': [
                    'R Goyal',
                    'C Green',
                    'Ishan Kishan',
                    'RG Sharma',
                    'N Wadhera',
                    'SA Yadav',
                    'T Stubbs',
                    'TH David',
                    'Arshad Khan',
                    'JC Archer',
                    'PP Chawla',
                    'Akash Madhwal'
                ],
                'Chennai Super Kings': [
                    'M Theekshana',
                    'RD Gaikwad',
                    'DP Conway',
                    'AM Rahane',
                    'AT Rayudu',
                    'S Dube',
                    'MS Dhoni',
                    'MM Ali',
                    'RA Jadeja',
                    'DL Chahar',
                    'M Pathirana',
                    'TU Deshpande'
                ]
            }
        }
    },
]
MIvsCSK2 = MI_vs_CSK
CSKvsMI2 = MI_vs_CSK

RCB_vs_DC = [
    {
        'Match Number': 50,
        'info': {
            'city': 'Delhi',
            'competition': 'IPL',
            'dates': ['2023-05-06'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Delhi Capitals',
                'by': {
                    'wickets': 7
                }
            },
            'overs': 20,
            'POTM': ['PD Salt'],
            'Playing XIs': {
                'Royal Challengers Bangalore': [
                    'HV Patel',
                    'V Kohli',
                    'F du Plessis',
                    'GJ Maxwell',
                    'MK Lomror',
                    'KD Karthik',
                    'Anuj Rawat',
                    'KM Jadhav',
                    'PWH de Silva',
                    'KV Sharma',
                    'Mohammed Siraj',
                    'JR Hazlewood'
                ],
                'Delhi Capitals': [
                    'I Sharma',
                    'DA Warner',
                    'PD Salt',
                    'MR Marsh',
                    'RR Rossouw',
                    'AR Patel',
                    'Aman Hakim Khan',
                    'MK Pandey',
                    'Kuldeep Yadav',
                    'Mukesh Kumar',
                    'KK Ahmed',
                    'RV Patel'
                ]
            }
        }
    },
]
RCBvsDC2 = RCB_vs_DC
DCvsRCB2 = RCB_vs_DC

GT_vs_LSG = [
    {
        'Match Number': 51,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-05-07'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Gujarat Titans',
                'by': {
                    'runs': 56
                }
            },
            'overs': 20,
            'POTM': ['Shubman Gill'],
            'Playing XIs': {
                'Gujarat Titans': [
                    'AS Joseph',
                    'WP Saha',
                    'Shubman Gill',
                    'HH Pandya',
                    'DA Miller',
                    'V Shankar',
                    'Rashid Khan',
                    'R Tewatia',
                    'A Manohar',
                    'MM Sharma',
                    'Mohammed Shami',
                    'Noor Ahmad'
                ],
                'Lucknow Super Giants': [
                    'Yash Thakur',
                    'KR Mayers',
                    'Q de Kock',
                    'DJ Hooda',
                    'MP Stoinis',
                    'N Pooran',
                    'A Badoni',
                    'Swapnil Singh',
                    'KH Pandya',
                    'Ravi Bishnoi',
                    'Mohsin Khan',
                    'Avesh Khan'
                ]
            }
        }
    },
]
GTvsLSG2 = GT_vs_LSG
LSGvsGT2 = GT_vs_LSG

RR_vs_SRH = [
    {
        'Match Number': 52,
        'info': {
            'city': 'Jaipur',
            'competition': 'IPL',
            'dates': ['2023-05-07'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Sunrisers Hyderabad',
                'by': {
                    'wickets': 4
                }
            },
            'overs': 20,
            'POTM': ['GD Phillips'],
            'Playing XIs': {
                'Rajasthan Royals': [
                    'OC McCoy',
                    'YBK Jaiswal',
                    'JC Buttler',
                    'SV Samson',
                    'SO Hetmyer',
                    'JE Root',
                    'Dhruv Jurel',
                    'R Ashwin',
                    'Sandeep Sharma',
                    'M Ashwin',
                    'K Yadav',
                    'YS Chahal'
                ],
                'Sunrisers Hyderabad': [
                    'T Natarajan',
                    'Anmolpreet Singh',
                    'Abhishek Sharma',
                    'RA Tripathi',
                    'H Klaasen',
                    'AK Markram',
                    'GD Phillips',
                    'Abdul Samad',
                    'M Jansen',
                    'Vivrant Sharma',
                    'M Markande',
                    'B Kumar'
                ]
            }
        }
    },
]
RRvsSRH2 = RR_vs_SRH
SRHvsRR2 = RR_vs_SRH

PBKS_vs_KKR = [
    {
        'Match Number': 53,
        'info': {
            'city': 'Kolkata',
            'competition': 'IPL',
            'dates': ['2023-05-08'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Kolkata Knight Riders',
                'by': {
                    'wickets': 5
                }
            },
            'overs': 20,
            'POTM': ['AD Russell'],
            'Playing XIs': {
                'Punjab Kings': [
                    'NT Ellis',
                    'P Simran Singh',
                    'S Dhawan',
                    'PBB Rajapaksa',
                    'LS Livingstone',
                    'JM Sharma',
                    'SM Curran',
                    'R Dhawan',
                    'M Shahrukh Khan',
                    'Harpreet Brar',
                    'RD Chahar',
                    'Arshdeep Singh'
                ],
                'Kolkata Knight Riders': [
                    'Suyash Sharma',
                    'JJ Roy',
                    'Rahmanullah Gurbaz',
                    'N Rana',
                    'VR Iyer',
                    'AD Russell',
                    'RK Singh',
                    'SN Thakur',
                    'SP Narine',
                    'Harshit Rana',
                    'VG Arora',
                    'CV Varun'
                ]
            }
        }
    },
]
PBKSvsKKR2 = PBKS_vs_KKR
KKRvsPBKS2 = PBKS_vs_KKR

RCB_vs_MI = [
    {
        'Match Number': 54,
        'info': {
            'city': 'Mumbai',
            'competition': 'IPL',
            'dates': ['2023-05-09'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Mumbai Indians',
                'by': {
                    'wickets': 6
                }
            },
            'overs': 20,
            'POTM': ['SA Yadav'],
            'Playing XIs': {
                'Royal Challengers Bangalore': [
                    'V Kohli',
                    'F du Plessis',
                    'Anuj Rawat',
                    'GJ Maxwell',
                    'MK Lomror',
                    'KD Karthik',
                    'KM Jadhav',
                    'PWH de Silva',
                    'JR Hazlewood',
                    'Mohammed Siraj',
                    'Vijaykumar Vyshak',
                    'HV Patel'
                ],
                'Mumbai Indians': [
                    'Ishan Kishan',
                    'RG Sharma',
                    'SA Yadav',
                    'N Wadhera',
                    'TH David',
                    'C Green',
                    'CJ Jordan',
                    'PP Chawla',
                    'JP Behrendorff',
                    'K Kartikeya',
                    'Akash Madhwal'
                ]
            }
        }
    },
]
RCBvsMI = RCB_vs_MI
MIvsRCB = RCB_vs_MI

CSK_vs_DC = [
    {
        'Match Number': 55,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-05-10'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Chennai Super Kings',
                'by': {
                    'runs': 27
                }
            },
            'overs': 20,
            'POTM': ['RA Jadeja'],
            'Playing XIs': {
                'Chennai Super Kings': [
                    'M Pathirana',
                    'RD Gaikwad',
                    'DP Conway',
                    'AM Rahane',
                    'MM Ali',
                    'S Dube',
                    'AT Rayudu',
                    'RA Jadeja',
                    'MS Dhoni',
                    'DL Chahar',
                    'TU Deshpande',
                    'M Theekshana'
                ],
                'Delhi Capitals': [
                    'KK Ahmed',
                    'DA Warner',
                    'PD Salt',
                    'MR Marsh',
                    'MK Pandey',
                    'RR Rossouw',
                    'RV Patel',
                    'AR Patel',
                    'Aman Hakim Khan',
                    'Lalit Yadav',
                    'Kuldeep Yadav',
                    'I Sharma'
                ]
            }
        }
    },
]
CSKvsDC = CSK_vs_DC
DCvsCSK = CSK_vs_DC

KKR_vs_RR = [
    {
        'Match Number': 56,
        'info': {
            'city': 'Kolkata',
            'competition': 'IPL',
            'dates': ['2023-05-11'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Rajasthan Royals',
                'by': {
                    'wickets': 9
                }
            },
            'overs': 20,
            'POTM': ['YBK Jaiswal'],
            'Playing XIs': {
                'Kolkata Knight Riders': [
                    'Suyash Sharma',
                    'JJ Roy',
                    'Rahmanullah Gurbaz',
                    'VR Iyer',
                    'N Rana',
                    'AD Russell',
                    'RK Singh',
                    'SN Thakur',
                    'AS Roy',
                    'SP Narine',
                    'Harshit Rana',
                    'CV Varun'
                ],
                'Rajasthan Royals': [
                    'YBK Jaiswal',
                    'JC Buttler',
                    'SV Samson',
                    'JE Root',
                    'Dhruv Jurel',
                    'SO Hetmyer',
                    'R Ashwin',
                    'Sandeep Sharma',
                    'KM Asif',
                    'TA Boult',
                    'YS Chahal'
                ]
            }
        }
    },
]
KKRvsRR = KKR_vs_RR
RRvsKKR = KKR_vs_RR

MI_vs_GT = [
    {
        'Match Number': 57,
        'info': {
            'city': 'Mumbai',
            'competition': 'IPL',
            'dates': ['2023-05-12'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Mumbai Indians',
                'by': {
                    'runs': 27
                }
            },
            'overs': 20,
            'POTM': ['SA Yadav'],
            'Playing XIs': {
                'Mumbai Indians': [
                    'Akash Madhwal',
                    'Ishan Kishan',
                    'RG Sharma',
                    'SA Yadav',
                    'N Wadhera',
                    'Vishnu Vinod',
                    'TH David',
                    'C Green',
                    'CJ Jordan',
                    'PP Chawla',
                    'JP Behrendorff',
                    'K Kartikeya'
                ],
                'Gujarat Titans': [
                    'MM Sharma',
                    'WP Saha',
                    'Shubman Gill',
                    'HH Pandya',
                    'V Shankar',
                    'DA Miller',
                    'A Manohar',
                    'R Tewatia',
                    'Rashid Khan',
                    'Noor Ahmad',
                    'AS Joseph',
                    'Mohammed Shami'
                ]
            }
        }
    },
]
MIvsGT = MI_vs_GT
GTvsMI = MI_vs_GT

SRH_vs_LSG = [
    {
        'Match Number': 58,
        'info': {
            'city': 'Hyderabad',
            'competition': 'IPL',
            'dates': ['2023-05-13'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Lucknow Super Giants',
                'by': {
                    'wickets': 7
                }
            },
            'overs': 20,
            'POTM': ['PN Mankad'],
            'Playing XIs': {
                'Sunrisers Hyderabad': [
                    'Vivrant Sharma',
                    'Anmolpreet Singh',
                    'Abhishek Sharma',
                    'RA Tripathi',
                    'AK Markram',
                    'H Klaasen',
                    'GD Phillips',
                    'Abdul Samad',
                    'B Kumar',
                    'T Natarajan',
                    'M Markande',
                    'Fazalhaq Farooqi'
                ],
                'Lucknow Super Giants': [
                    'A Mishra',
                    'KR Mayers',
                    'Q de Kock',
                    'PN Mankad',
                    'MP Stoinis',
                    'N Pooran',
                    'KH Pandya',
                    'Yash Thakur',
                    'Ravi Bishnoi',
                    'Yudhvir Singh',
                    'Avesh Khan',
                    'A Badoni'
                ]
            }
        }
    },
]
SRHvsLSG2 = SRH_vs_LSG
LSGvsSRH2 = SRH_vs_LSG

DC_vs_PBKS = [
    {
        'Match Number': 59,
        'info': {
            'city': 'Delhi',
            'competition': 'IPL',
            'dates': ['2023-05-13'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Punjab Kings',
                'by': {
                    'runs': 31
                }
            },
            'overs': 20,
            'POTM': ['P Simran Singh'],
            'Playing XIs': {
                'Punjab Kings': [
                    'NT Ellis',
                    'P Simran Singh',
                    'S Dhawan',
                    'LS Livingstone',
                    'JM Sharma',
                    'SM Curran',
                    'Harpreet Brar',
                    'M Shahrukh Khan',
                    'Sikandar Raza',
                    'R Dhawan',
                    'RD Chahar',
                    'Arshdeep Singh'
                ],
                'Delhi Capitals': [
                    'KK Ahmed',
                    'DA Warner',
                    'PD Salt',
                    'MR Marsh',
                    'RR Rossouw',
                    'AR Patel',
                    'MK Pandey',
                    'Aman Hakim Khan',
                    'P Dubey',
                    'Kuldeep Yadav',
                    'Mukesh Kumar',
                    'I Sharma'
                ]
            }
        }
    },
]
DCvsPBKS = DC_vs_PBKS
PBKSvsDC = DC_vs_PBKS

RCB_vs_RR = [
    {
        'Match Number': 60,
        'info': {
            'city': 'Jaipur',
            'competition': 'IPL',
            'dates': ['2023-05-14'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Royal Challengers Bangalore',
                'by': {
                    'runs': 112
                }
            },
            'overs': 20,
            'POTM': ['WD Parnell'],
            'Playing XIs': {
                'Royal Challengers Bangalore': [
                    'Shahbaz Ahmed',
                    'V Kohli',
                    'F du Plessis',
                    'GJ Maxwell',
                    'MK Lomror',
                    'KD Karthik',
                    'MG Bracewell',
                    'Anuj Rawat',
                    'WD Parnell',
                    'KV Sharma',
                    'HV Patel',
                    'Mohammed Siraj'
                ],
                'Rajasthan Royals': [
                    'YS Chahal',
                    'YBK Jaiswal',
                    'JC Buttler',
                    'SV Samson',
                    'JE Root',
                    'D Padikkal',
                    'SO Hetmyer',
                    'Dhruv Jurel',
                    'R Ashwin',
                    'A Zampa',
                    'Sandeep Sharma',
                    'KM Asif'
                ]
            }
        }
    },
]
RCBvsRR2 = RCB_vs_RR
RRvsRCB2 = RCB_vs_RR

CSK_vs_KKR = [
    {
        'Match Number': 61,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-05-14'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Kolkata Knight Riders',
                'by': {
                    'wickets': 6
                }
            },
            'overs': 20,
            'POTM': ['RK Singh'],
            'Playing XIs': {
                'Chennai Super Kings': [
                    'M Pathirana',
                    'RD Gaikwad',
                    'DP Conway',
                    'AM Rahane',
                    'AT Rayudu',
                    'S Dube',
                    'MM Ali',
                    'RA Jadeja',
                    'MS Dhoni',
                    'DL Chahar',
                    'TU Deshpande',
                    'M Theekshana'
                ],
                'Kolkata Knight Riders': [
                    'Suyash Sharma',
                    'JJ Roy',
                    'Rahmanullah Gurbaz',
                    'VR Iyer',
                    'N Rana',
                    'RK Singh',
                    'AD Russell',
                    'SN Thakur',
                    'SP Narine',
                    'VG Arora',
                    'Harshit Rana',
                    'CV Varun'
                ]
            }
        }
    },
]
CSKvsKKR2 = CSK_vs_KKR
KKRvsCSK2 = CSK_vs_KKR

GT_vs_SRH = [
    {
        'Match Number': 62,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-05-15'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Gujarat Titans',
                'by': {
                    'runs': 34
                }
            },
            'overs': 20,
            'POTM': ['Shubman Gill'],
            'Playing XIs': {
                'Gujarat Titans': [
                    'Yash Dayal',
                    'WP Saha',
                    'Shubman Gill',
                    'B Sai Sudharsan',
                    'HH Pandya',
                    'DA Miller',
                    'R Tewatia',
                    'MD Shanaka',
                    'Rashid Khan',
                    'Noor Ahmad',
                    'Mohammed Shami',
                    'MM Sharma'
                ],
                'Sunrisers Hyderabad': [
                    'T Natarajan',
                    'Anmolpreet Singh',
                    'Abhishek Sharma',
                    'AK Markram',
                    'RA Tripathi',
                    'H Klaasen',
                    'Sanvir Singh',
                    'Abdul Samad',
                    'M Jansen',
                    'B Kumar',
                    'M Markande',
                    'Fazalhaq Farooqi'
                ]
            }
        }
    },
]
GTvsSRH = GT_vs_SRH
SRHvsGT = GT_vs_SRH

LSG_vs_MI = [
    {
        'Match Number': 63,
        'info': {
            'city': 'Lucknow',
            'competition': 'IPL',
            'dates': ['2023-05-16'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Lucknow Super Giants',
                'by': {
                    'runs': 5
                }
            },
            'overs': 20,
            'POTM': ['MP Stoinis'],
            'Playing XIs': {
                'Lucknow Super Giants': [
                    'Yash Thakur',
                    'DJ Hooda',
                    'Q de Kock',
                    'PN Mankad',
                    'KH Pandya',
                    'MP Stoinis',
                    'N Pooran',
                    'A Badoni',
                    'Naveen-ul-Haq',
                    'Ravi Bishnoi',
                    'Swapnil Singh',
                    'Mohsin Khan'
                ],
                'Mumbai Indians': [
                    'Akash Madhwal',
                    'Ishan Kishan',
                    'RG Sharma',
                    'SA Yadav',
                    'N Wadhera',
                    'TH David',
                    'Vishnu Vinod',
                    'C Green',
                    'CJ Jordan',
                    'HR Shokeen',
                    'PP Chawla',
                    'JP Behrendorff'
                ]
            }
        }
    },
]
LSGvsMI = LSG_vs_MI
MIvsLSG = LSG_vs_MI

DC_vs_PBKS = [
    {
        'Match Number': 64,
        'info': {
            'city': 'Dharamsala',
            'competition': 'IPL',
            'dates': ['2023-05-17'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Delhi Capitals',
                'by': {
                    'runs': 15
                }
            },
            'overs': 20,
            'POTM': ['RR Rossouw'],
            'Playing XIs': {
                'Delhi Capitals': [
                    'Mukesh Kumar',
                    'DA Warner',
                    'PP Shaw',
                    'RR Rossouw',
                    'PD Salt',
                    'AR Patel',
                    'Aman Hakim Khan',
                    'YV Dhull',
                    'Kuldeep Yadav',
                    'A Nortje',
                    'I Sharma',
                    'KK Ahmed'
                ],
                'Punjab Kings': [
                    'NT Ellis',
                    'P Simran Singh',
                    'S Dhawan',
                    'Atharva Taide',
                    'LS Livingstone',
                    'JM Sharma',
                    'M Shahrukh Khan',
                    'SM Curran',
                    'Harpreet Brar',
                    'RD Chahar',
                    'K Rabada',
                    'Arshdeep Singh'
                ]
            }
        }
    },
]
DCvsPBKS2 = DC_vs_PBKS
PBKSvsDC2 = DC_vs_PBKS

SRH_vs_RCB = [
    {
        'Match Number': 65,
        'info': {
            'city': 'Hyderabad',
            'competition': 'IPL',
            'dates': ['2023-05-18'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Royal Challengers Bangalore',
                'by': {
                    'wickets': 8
                }
            },
            'overs': 20,
            'POTM': ['V Kohli'],
            'Playing XIs': {
                'Sunrisers Hyderabad': [
                    'T Natarajan',
                    'Abhishek Sharma',
                    'RA Tripathi',
                    'AK Markram',
                    'H Klaasen',
                    'HC Brook',
                    'GD Phillips',
                    'Abdul Samad',
                    'B Kumar',
                    'Kartik Tyagi',
                    'Mayank Dagar',
                    'Nithish Kumar Reddy'
                ],
                'Royal Challengers Bangalore': [
                    'V Kohli',
                    'F du Plessis',
                    'GJ Maxwell',
                    'MG Bracewell',
                    'MK Lomror',
                    'Anuj Rawat',
                    'Shahbaz Ahmed',
                    'HV Patel',
                    'WD Parnell',
                    'KV Sharma',
                    'Mohammed Siraj'
                ]
            }
        }
    },
]
SRHvsRCB = SRH_vs_RCB
RCBvsSRH = SRH_vs_RCB

PBKS_vs_RR = [
    {
        'Match Number': 66,
        'info': {
            'city': 'Dharamsala',
            'competition': 'IPL',
            'dates': ['2023-05-19'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Rajasthan Royals',
                'by': {
                    'wickets': 4
                }
            },
            'overs': 20,
            'POTM': ['D Padikkal'],
            'Playing XIs': {
                'Punjab Kings': [
                    'NT Ellis',
                    'P Simran Singh',
                    'S Dhawan',
                    'Atharva Taide',
                    'LS Livingstone',
                    'SM Curran',
                    'JM Sharma',
                    'M Shahrukh Khan',
                    'Harpreet Brar',
                    'RD Chahar',
                    'K Rabada',
                    'Arshdeep Singh'
                ],
                'Rajasthan Royals': [
                    'YS Chahal',
                    'YBK Jaiswal',
                    'JC Buttler',
                    'D Padikkal',
                    'SV Samson',
                    'SO Hetmyer',
                    'R Parag',
                    'Dhruv Jurel',
                    'TA Boult',
                    'A Zampa',
                    'Navdeep Saini',
                    'Sandeep Sharma'
                ]
            }
        }
    },
]
PBKSvsRR2 = PBKS_vs_RR
RRvsPBKS2 = PBKS_vs_RR

CSK_vs_DC = [
    {
        'Match Number': 67,
        'info': {
            'city': 'Delhi',
            'competition': 'IPL',
            'dates': ['2023-05-20'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Chennai Super Kings',
                'by': {
                    'runs': 77
                }
            },
            'overs': 20,
            'POTM': ['RD Gaikwad'],
            'Playing XIs': {
                'Chennai Super Kings': [
                    'M Pathirana',
                    'RD Gaikwad',
                    'DP Conway',
                    'S Dube',
                    'MS Dhoni',
                    'RA Jadeja',
                    'AM Rahane',
                    'MM Ali',
                    'AT Rayudu',
                    'DL Chahar',
                    'TU Deshpande',
                    'M Theekshana'
                ],
                'Delhi Capitals': [
                    'KK Ahmed',
                    'PP Shaw',
                    'DA Warner',
                    'PD Salt',
                    'RR Rossouw',
                    'YV Dhull',
                    'AR Patel',
                    'Aman Hakim Khan',
                    'Lalit Yadav',
                    'A Nortje',
                    'Kuldeep Yadav',
                    'C Sakariya'
                ]
            }
        }
    },
]
CSKvsDC2 = CSK_vs_DC
DCvsCSK2 = CSK_vs_DC

LSG_vs_KKR = [
    {
        'Match Number': 68,
        'info': {
            'city': 'Kolkata',
            'competition': 'IPL',
            'dates': ['2023-05-20'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Lucknow Super Giants',
                'by': {
                    'runs': 1
                }
            },
            'overs': 20,
            'POTM': ['N Pooran'],
            'Playing XIs': {
                'Lucknow Super Giants': [
                    'Yash Thakur',
                    'KS Sharma',
                    'Q de Kock',
                    'PN Mankad',
                    'MP Stoinis',
                    'KH Pandya',
                    'A Badoni',
                    'N Pooran',
                    'K Gowtham',
                    'Ravi Bishnoi',
                    'Naveen-ul-Haq',
                    'Mohsin Khan'
                ],
                'Kolkata Knight Riders': [
                    'Harshit Rana',
                    'JJ Roy',
                    'VR Iyer',
                    'N Rana',
                    'Rahmanullah Gurbaz',
                    'RK Singh',
                    'AD Russell',
                    'SN Thakur',
                    'SP Narine',
                    'VG Arora',
                    'CV Varun',
                    'Suyash Sharma'
                ]
            }
        }
    },
]
LSGvsKKR = LSG_vs_KKR
KKRvsLSG = LSG_vs_KKR

SRH_vs_MI = [
    {
        'Match Number': 69,
        'info': {
            'city': 'Mumbai',
            'competition': 'IPL',
            'dates': ['2023-05-21'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Mumbai Indians',
                'by': {
                    'wickets': 8
                }
            },
            'overs': 20,
            'POTM': ['C Green'],
            'Playing XIs': {
                'Sunrisers Hyderabad': [
                    'Kartik Tyagi',
                    'Vivrant Sharma',
                    'MA Agarwal',
                    'H Klaasen',
                    'GD Phillips',
                    'AK Markram',
                    'HC Brook',
                    'Sanvir Singh',
                    'Nithish Kumar Reddy',
                    'Mayank Dagar',
                    'B Kumar',
                    'Umran Malik'
                ],
                'Mumbai Indians': [
                    'Ishan Kishan',
                    'RG Sharma',
                    'C Green',
                    'SA Yadav',
                    'TH David',
                    'N Wadhera',
                    'CJ Jordan',
                    'PP Chawla',
                    'JP Behrendorff',
                    'K Kartikeya',
                    'Akash Madhwal'
                ]
            }
        }
    },
]
SRHvsMI = SRH_vs_MI
MIvsSRH = SRH_vs_MI

RCB_vs_GT = [
    {
        'Match Number': 70,
        'info': {
            'city': 'Bengaluru',
            'competition': 'IPL',
            'dates': ['2023-05-21'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Gujarat Titans',
                'by': {
                    'wickets': 6
                }
            },
            'overs': 20,
            'POTM': ['Shubman Gill'],
            'Playing XIs': {
                'Royal Challengers Bangalore': [
                    'H Sharma',
                    'V Kohli',
                    'F du Plessis',
                    'GJ Maxwell',
                    'MK Lomror',
                    'MG Bracewell',
                    'KD Karthik',
                    'Anuj Rawat',
                    'HV Patel',
                    'WD Parnell',
                    'Vijaykumar Vyshak',
                    'Mohammed Siraj'
                ],
                'Gujarat Titans': [
                    'Yash Dayal',
                    'WP Saha',
                    'Shubman Gill',
                    'V Shankar',
                    'MD Shanaka',
                    'DA Miller',
                    'R Tewatia',
                    'HH Pandya',
                    'Rashid Khan',
                    'Noor Ahmad',
                    'Mohammed Shami',
                    'MM Sharma'
                ]
            }
        }
    },
]
RCBvsGT = RCB_vs_GT
GTvsRCB = RCB_vs_GT

CSK_vs_GT = [
    {
        'Match Number': 71,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-05-23'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Chennai Super Kings',
                'by': {
                    'runs': 15
                }
            },
            'overs': 20,
            'POTM': ['RD Gaikwad'],
            'Playing XIs': {
                'Chennai Super Kings': [
                    'M Pathirana',
                    'RD Gaikwad',
                    'DP Conway',
                    'S Dube',
                    'AM Rahane',
                    'AT Rayudu',
                    'RA Jadeja',
                    'MS Dhoni',
                    'MM Ali',
                    'DL Chahar',
                    'TU Deshpande',
                    'M Theekshana'
                ],
                'Gujarat Titans': [
                    'MM Sharma',
                    'WP Saha',
                    'Shubman Gill',
                    'HH Pandya',
                    'MD Shanaka',
                    'DA Miller',
                    'V Shankar',
                    'R Tewatia',
                    'Rashid Khan',
                    'DG Nalkande',
                    'Noor Ahmad',
                    'Mohammed Shami'
                ]
            }
        }
    },
]
CSKvsGT2 = CSK_vs_GT
GTvsCSK2 = CSK_vs_GT

MI_vs_LSG = [
    {
        'Match Number': 72,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-05-24'],

            'match_type': 'T20',
            'outcome': {
                'winner': 'Mumbai Indians',
                'by': {
                    'runs': 81
                }
            },
            'overs': 20,
            'POTM': ['Akash Madhwal'],
            'Playing XIs': {
                'Mumbai Indians': [
                    'Ishan Kishan',
                    'RG Sharma',
                    'C Green',
                    'SA Yadav',
                    'Tilak Varma',
                    'TH David',
                    'N Wadhera',
                    'CJ Jordan',
                    'HR Shokeen',
                    'PP Chawla',
                    'JP Behrendorff',
                    'Akash Madhwal'
                ],
                'Lucknow Super Giants': [
                    'Yash Thakur',
                    'KR Mayers',
                    'PN Mankad',
                    'KH Pandya',
                    'MP Stoinis',
                    'A Badoni',
                    'N Pooran',
                    'DJ Hooda',
                    'K Gowtham',
                    'Ravi Bishnoi',
                    'Naveen-ul-Haq',
                    'Mohsin Khan'
                ]
            }
        }
    },
]
MIvsLSG2 = MI_vs_LSG
LSGvsMI2 = MI_vs_LSG

GT_vs_MI = [
    {
        'Match Number': 73,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-05-26'],
            'match_type': 'T20',
            'outcome': {
                'winner': 'Gujarat Titans',
                'by': {
                    'runs': 62
                }
            },
            'overs': 20,
            'POTM': ['Shubman Gill'],
            'Playing XIs': {
                'Gujarat Titans': [
                    'J Little',
                    'WP Saha',
                    'Shubman Gill',
                    'B Sai Sudharsan',
                    'HH Pandya',
                    'Rashid Khan',
                    'DA Miller',
                    'R Tewatia',
                    'V Shankar',
                    'Noor Ahmad',
                    'Mohammed Shami',
                    'MM Sharma'
                ],
                'Mumbai Indians': [
                    'Ishan Kishan',
                    'Akash Madhwal',
                    'RG Sharma',
                    'N Wadhera',
                    'C Green',
                    'SA Yadav',
                    'Tilak Varma',
                    'Vishnu Vinod',
                    'TH David',
                    'CJ Jordan',
                    'PP Chawla',
                    'K Kartikeya',
                    'JP Behrendorff'
                ]
            }
        }
    },
]
GTvsMI2 = GT_vs_MI
MIvsGT2 = GT_vs_MI

CSK_vs_GT = [
    {
        'Match Number': 74,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': '2023-05-29',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Chennai Super Kings',
                'by': {
                    'wickets': 5
                },
                'method': 'D/L'
            },
            'overs': 20,
            'POTM': ['DP Conway'],
            'Playing XIs': {
                'Gujarat Titans': [
                    'WP Saha',
                    'Shubman Gill',
                    'B Sai Sudharsan',
                    'HH Pandya',
                    'Rashid Khan',
                    'V Shankar',
                    'DA Miller',
                    'R Tewatia',
                    'MM Sharma',
                    'Noor Ahmad',
                    'Mohammed Shami',
                    'J Little'
                ],
                'Chennai Super Kings': [
                    'RD Gaikwad',
                    'DP Conway',
                    'S Dube',
                    'AM Rahane',
                    'AT Rayudu',
                    'MS Dhoni',
                    'RA Jadeja',
                    'MM Ali',
                    'DL Chahar',
                    'M Pathirana',
                    'TU Deshpande',
                    'M Theekshana'
                ]
            }
        }
    },
]
CSKvsGT3 = CSK_vs_GT
GTvsCSK3 = CSK_vs_GT
# ╚══════════════ End of Lists ═══════════════╝ #

# ╚═══════════════════════════════ End of Code ═════════════════════════════════╝ #


