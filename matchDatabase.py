 #   __  .______    __         .___  ___.      ___   .___________.  ______  __    __   _______     _______.    _______       ___   .___________.    ___      .______        ___           _______. _______ 
 #  |  | |   _  \  |  |        |   \/   |     /   \  |           | /      ||  |  |  | |   ____|   /       |   |       \     /   \  |           |   /   \     |   _  \      /   \         /       ||   ____|
 #  |  | |  |_)  | |  |        |  \  /  |    /  ^  \ `---|  |----`|  ,----'|  |__|  | |  |__     |   (----`   |  .--.  |   /  ^  \ `---|  |----`  /  ^  \    |  |_)  |    /  ^  \       |   (----`|  |__   
 #  |  | |   ___/  |  |        |  |\/|  |   /  /_\  \    |  |     |  |     |   __   | |   __|     \   \       |  |  |  |  /  /_\  \    |  |      /  /_\  \   |   _  <    /  /_\  \       \   \    |   __|  
 #  |  | |  |      |  `----.   |  |  |  |  /  _____  \   |  |     |  `----.|  |  |  | |  |____.----)   |      |  '--'  | /  _____  \   |  |     /  _____  \  |  |_)  |  /  _____  \  .----)   |   |  |____ 
 #  |__| | _|      |_______|   |__|  |__| /__/     \__\  |__|      \______||__|  |__| |_______|_______/       |_______/ /__/     \__\  |__|    /__/     \__\ |______/  /__/     \__\ |_______/    |_______|
 #

# ╔═════════════════════════════ Beigining of Code ════════════════════════════╗ #

#
def get_match_info(matches, match_number):
    #Go through the list matches to find the match with the specified match number
    for match in matches:
        if match.get('match_number') == match_number:
            return match
    #Return an empty dictionary if the match number is not found
    return {}

# ╔══════════════════════════════════════════════════╗
# ║    Lists to define the matches and match info    ║
# ╚══════════════════════════════════════════════════╝

#Match 1 - GT vs CSK
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
GTvsCSK = GT_vs_CSK
CSKvsGT = GT_vs_CSK

#Match 2 - PBKS vs KKR
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

LSG_vs_DC = [
    {
        'match_number': 3,
        'info': {
            'city': 'Lucknow',
            'competition': 'IPL',
            'dates': ['2023-04-01'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 50
                },
                'winner': 'Lucknow Super Giants'
            },
            'overs': 20,
            'player_of_match': ['MA Wood'],
            'players': {
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


RR_vs_SRH = [
    {
        'match_number': 4,
        'info': {
            'city': 'Hyderabad',
            'competition': 'IPL',
            'dates': ['2023-04-02'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 72
                },
                'winner': 'Rajasthan Royals'
            },
            'overs': 20,
            'player_of_match': ['JC Buttler'],
            'players': {
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

MI_vs_RCB = [
    {
        'match_number': 5,
        'info': {
            'city': 'Bengaluru',
            'competition': 'IPL',
            'dates': ['2023-04-02'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 8
                },
                'winner': 'Royal Challengers Bangalore'
            },
            'overs': 20,
            'player_of_match': ['F du Plessis'],
            'players': {
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


CSK_vs_LSG = [
    {
        'match_number': 6,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-04-03'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 12
                },
                'winner': 'Chennai Super Kings'
            },
            'overs': 20,
            'player_of_match': ['MM Ali'],
            'players': {
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


DC_vs_GT = [
    {
        'match_number': 7,
        'info': {
            'city': 'Delhi',
            'competition': 'IPL',
            'dates': ['2023-04-04'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 6
                },
                'winner': 'Gujarat Titans'
            },
            'overs': 20,
            'player_of_match': ['B Sai Sudharsan'],
            'players': {
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

PBKS_vs_RR = [
    {
        'match_number': 8,
        'info': {
            'city': 'Guwahati',
            'competition': 'IPL',
            'dates': ['2023-04-05'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 5
                },
                'winner': 'Punjab Kings'
            },
            'overs': 20,
            'player_of_match': ['NT Ellis'],
            'players': {
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


KKR_vs_RCB = [
    {
        'match_number': 9,
        'info': {
            'city': 'Kolkata',
            'competition': 'IPL',
            'dates': ['2023-04-06'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 81
                },
                'winner': 'Kolkata Knight Riders'
            },
            'overs': 20,
            'player_of_match': ['SN Thakur'],
            'players': {
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

SRH_vs_LSG = [
    {
        'match_number': 10,
        'info': {
            'city': 'Lucknow',
            'competition': 'IPL',
            'dates': ['2023-04-07'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 5
                },
                'winner': 'Lucknow Super Giants'
            },
            'overs': 20,
            'player_of_match': ['KH Pandya'],
            'players': {
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

RR_vs_DC = [
    {
        'match_number': 11,
        'info': {
            'city': 'Guwahati',
            'competition': 'IPL',
            'dates': ['2023-04-08'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 57
                },
                'winner': 'Rajasthan Royals'
            },
            'overs': 20,
            'player_of_match': ['YBK Jaiswal'],
            'players': {
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

MI_vs_CSK = [
    {
        'match_number': 12,
        'info': {
            'city': 'Mumbai',
            'competition': 'IPL',
            'dates': ['2023-04-08'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 7
                },
                'winner': 'Chennai Super Kings'
            },
            'overs': 20,
            'player_of_match': ['RA Jadeja'],
            'players': {
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

GT_vs_KKR = [
    {
        'match_number': 13,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-04-09'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 3
                },
                'winner': 'Kolkata Knight Riders'
            },
            'overs': 20,
            'player_of_match': ['RK Singh'],
            'players': {
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

PBKS_vs_SRH = [
    {
        'match_number': 14,
        'info': {
            'city': 'Hyderabad',
            'competition': 'IPL',
            'dates': ['2023-04-09'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 8
                },
                'winner': 'Sunrisers Hyderabad'
            },
            'overs': 20,
            'player_of_match': ['S Dhawan'],
            'players': {
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

RCB_vs_LSG = [
    {
        'match_number': 15,
        'info': {
            'city': 'Bengaluru',
            'competition': 'IPL',
            'dates': ['2023-04-10'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 1
                },
                'winner': 'Lucknow Super Giants'
            },
            'overs': 20,
            'player_of_match': ['N Pooran'],
            'players': {
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

DC_vs_MI = [
    {
        'match_number': 16,
        'info': {
            'city': 'Delhi',
            'competition': 'IPL',
            'dates': ['2023-04-11'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 6
                },
                'winner': 'Mumbai Indians'
            },
            'overs': 20,
            'player_of_match': ['RG Sharma'],
            'players': {
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

RR_vs_CSK = [
    {
        'match_number': 17,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-04-12'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 3
                },
                'winner': 'Rajasthan Royals'
            },
            'overs': 20,
            'player_of_match': ['R Ashwin'],
            'players': {
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

PBKS_vs_GT = [
    {
        'match_number': 18,
        'info': {
            'city': 'Chandigarh',
            'competition': 'IPL',
            'dates': ['2023-04-13'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 6
                },
                'winner': 'Gujarat Titans'
            },
            'overs': 20,
            'player_of_match': ['MM Sharma'],
            'players': {
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

KKR_vs_SRH = [
    {
        'match_number': 19,
        'info': {
            'city': 'Kolkata',
            'competition': 'IPL',
            'dates': ['2023-04-14'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 23
                },
                'winner': 'Sunrisers Hyderabad'
            },
            'overs': 20,
            'player_of_match': ['HC Brook'],
            'players': {
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

RCB_vs_DC = [
    {
        'match_number': 20,
        'info': {
            'city': 'Bengaluru',
            'competition': 'IPL',
            'dates': ['2023-04-15'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 23
                },
                'winner': 'Royal Challengers Bangalore'
            },
            'overs': 20,
            'player_of_match': ['V Kohli'],
            'players': {
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

LSG_vs_PBKS = [
    {
        'match_number': 21,
        'info': {
            'city': 'Lucknow',
            'competition': 'IPL',
            'dates': ['2023-04-15'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 2
                },
                'winner': 'Punjab Kings'
            },
            'overs': 20,
            'player_of_match': ['Sikandar Raza'],
            'players': {
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

KKR_vs_MI = [
    {
        'match_number': 22,
        'info': {
            'city': 'Mumbai',
            'competition': 'IPL',
            'dates': ['2023-04-16'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 5
                },
                'winner': 'Mumbai Indians'
            },
            'overs': 20,
            'player_of_match': ['VR Iyer'],
            'players': {
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

GT_vs_RR = [
    {
        'match_number': 22,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-04-16'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 3
                },
                'winner': 'Rajasthan Royals'
            },
            'overs': 20,
            'player_of_match': ['SO Hetmyer'],
            'players': {
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

CSK_vs_RCB = [
    {
        'match_number': 23,
        'info': {
            'city': 'Bengaluru',
            'competition': 'IPL',
            'dates': ['2023-04-17'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 8
                },
                'winner': 'Chennai Super Kings'
            },
            'overs': 20,
            'player_of_match': ['DP Conway'],
            'players': {
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

MI_vs_SRH = [
    {
        'match_number': 24,
        'info': {
            'city': 'Hyderabad',
            'competition': 'IPL',
            'dates': ['2023-04-18'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 14
                },
                'winner': 'Mumbai Indians'
            },
            'overs': 20,
            'player_of_match': ['C Green'],
            'players': {
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

LSG_vs_RR = [
    {
        'match_number': 25,
        'info': {
            'city': 'Jaipur',
            'competition': 'IPL',
            'dates': ['2023-04-19'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 10
                },
                'winner': 'Lucknow Super Giants'
            },
            'overs': 20,
            'player_of_match': ['MP Stoinis'],
            'players': {
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

RCB_vs_PBKS = [
    {
        'match_number': 26,
        'info': {
            'city': 'Chandigarh',
            'competition': 'IPL',
            'dates': ['2023-04-20'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 24
                },
                'winner': 'Royal Challengers Bangalore'
            },
            'overs': 20,
            'player_of_match': ['Mohammed Siraj'],
            'players': {
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

KKR_vs_DC = [
    {
        'match_number': 27,
        'info': {
            'city': 'Delhi',
            'competition': 'IPL',
            'dates': ['2023-04-20'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 4
                },
                'winner': 'Delhi Capitals'
            },
            'overs': 20,
            'player_of_match': ['I Sharma'],
            'players': {
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

SRH_vs_CSK = [
    {
        'match_number': 28,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-04-21'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 7
                },
                'winner': 'Chennai Super Kings'
            },
            'overs': 20,
            'player_of_match': ['RA Jadeja'],
            'players': {
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

GT_vs_LSG = [
    {
        'match_number': 29,
        'info': {
            'city': 'Lucknow',
            'competition': 'IPL',
            'dates': ['2023-04-22'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 7
                },
                'winner': 'Gujarat Titans'
            },
            'overs': 20,
            'player_of_match': ['MM Sharma'],
            'players': {
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

PK_vs_MI = [
    {
        'match_number': 30,
        'info': {
            'city': 'Mumbai',
            'competition': 'IPL',
            'dates': ['2023-04-22'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 13
                },
                'winner': 'Punjab Kings'
            },
            'overs': 20,
            'player_of_match': ['SM Curran'],
            'players': {
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

RCB_vs_MI = [
    {
        'match_number': 31,
        'info': {
            'city': 'Bengaluru',
            'competition': 'IPL',
            'dates': ['2023-04-23'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 7
                },
                'winner': 'Royal Challengers Bangalore'
            },
            'overs': 20,
            'player_of_match': ['GJ Maxwell'],
            'players': {
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

CSK_vs_KKR = [
    {
        'match_number': 32,
        'info': {
            'city': 'Kolkata',
            'competition': 'IPL',
            'dates': ['2023-04-23'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 49
                },
                'winner': 'Chennai Super Kings'
            },
            'overs': 20,
            'player_of_match': ['AM Rahane'],
            'players': {
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

DC_vs_SRH = [
    {
        'match_number': 33,
        'info': {
            'city': 'Hyderabad',
            'competition': 'IPL',
            'dates': ['2023-04-24'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 7
                },
                'winner': 'Delhi Capitals'
            },
            'overs': 20,
            'player_of_match': ['AR Patel'],
            'players': {
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

GT_vs_MI = [
    {
        'match_number': 34,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-04-25'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 55
                },
                'winner': 'Gujarat Titans'
            },
            'overs': 20,
            'player_of_match': ['A Manohar'],
            'players': {
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

KKR_vs_RCB = [
    {
        'match_number': 35,
        'info': {
            'city': 'Bengaluru',
            'competition': 'IPL',
            'dates': ['2023-04-26'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 21
                },
                'winner': 'Kolkata Knight Riders'
            },
            'overs': 20,
            'player_of_match': ['CV Varun'],
            'players': {
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

RR_vs_CSK = [
    {
        'match_number': 36,
        'info': {
            'city': 'Jaipur',
            'competition': 'IPL',
            'dates': ['2023-04-27'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 32
                },
                'winner': 'Rajasthan Royals'
            },
            'overs': 20,
            'player_of_match': ['YBK Jaiswal'],
            'players': {
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

LSG_vs_PBKS = [
    {
        'match_number': 37,
        'info': {
            'city': 'Chandigarh',
            'competition': 'IPL',
            'dates': ['2023-04-28'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 56
                },
                'winner': 'Lucknow Super Giants'
            },
            'overs': 20,
            'player_of_match': ['MP Stoinis'],
            'players': {
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

KKR_vs_GT = [
    {
        'match_number': 38,
        'info': {
            'city': 'Kolkata',
            'competition': 'IPL',
            'dates': ['2023-04-29'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 7
                },
                'winner': 'Gujarat Titans'
            },
            'overs': 20,
            'player_of_match': ['J Little'],
            'players': {
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

DC_vs_SRH = [
    {
        'match_number': 39,
        'info': {
            'city': 'Delhi',
            'competition': 'IPL',
            'dates': ['2023-04-29'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 9
                },
                'winner': 'Sunrisers Hyderabad'
            },
            'overs': 20,
            'player_of_match': ['MR Marsh'],
            'players': {
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

CSK_vs_PBKS = [
    {
        'match_number': 40,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-04-30'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 4
                },
                'winner': 'Punjab Kings'
            },
            'overs': 20,
            'player_of_match': ['DP Conway'],
            'players': {
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

RR_vs_MI = [
    {
        'match_number': 41,
        'info': {
            'city': 'Mumbai',
            'competition': 'IPL',
            'dates': ['2023-04-30'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'wickets': 6
                },
                'winner': 'Mumbai Indians'
            },
            'overs': 20,
            'player_of_match': ['YBK Jaiswal'],
            'players': {
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

RCB_vs_LSG = [
    {
        'match_number': 42,
        'info': {
            'city': 'Lucknow',
            'competition': 'IPL',
            'dates': ['2023-05-01'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 18
                },
                'winner': 'Royal Challengers Bangalore'
            },
            'overs': 20,
            'player_of_match': ['F du Plessis'],
            'players': {
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

DC_vs_GT = [
    {
        'match_number': 43,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-05-02'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'by': {
                    'runs': 5
                },
                'winner': 'Delhi Capitals'
            },
            'overs': 20,
            'player_of_match': ['Mohammed Shami'],
            'players': {
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

LSG_vs_CSK = [
    {
        'match_number': 44,
        'info': {
            'city': 'Lucknow',
            'competition': 'IPL',
            'dates': ['2023-05-03'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'result': 'no result'
            },
            'overs': 20,
            'players': {
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

PBKS_vs_MI = [
    {
        'match_number': 45,
        'info': {
            'city': 'Chandigarh',
            'competition': 'IPL',
            'dates': ['2023-05-03'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Mumbai Indians',
                'by': {
                    'wickets': 6
                }
            },
            'overs': 20,
            'player_of_match': ['Ishan Kishan'],
            'players': {
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

SRH_vs_KKR = [
    {
        'match_number': 46,
        'info': {
            'city': 'Hyderabad',
            'competition': 'IPL',
            'dates': ['2023-05-04'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Kolkata Knight Riders',
                'by': {
                    'runs': 5
                }
            },
            'overs': 20,
            'player_of_match': ['CV Varun'],
            'players': {
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

RR_vs_GT = [
    {
        'match_number': 47,
        'info': {
            'city': 'Jaipur',
            'competition': 'IPL',
            'dates': ['2023-05-05'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Gujarat Titans',
                'by': {
                    'wickets': 9
                }
            },
            'overs': 20,
            'player_of_match': ['Rashid Khan'],
            'players': {
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

MI_vs_CSK = [
    {
        'match_number': 48,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-05-06'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Chennai Super Kings',
                'by': {
                    'wickets': 6
                }
            },
            'overs': 20,
            'player_of_match': ['M Pathirana'],
            'players': {
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

RCB_vs_DC = [
    {
        'match_number': 49,
        'info': {
            'city': 'Delhi',
            'competition': 'IPL',
            'dates': ['2023-05-06'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Delhi Capitals',
                'by': {
                    'wickets': 7
                }
            },
            'overs': 20,
            'player_of_match': ['PD Salt'],
            'players': {
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

GT_vs_LSG = [
    {
        'match_number': 50,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-05-07'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Gujarat Titans',
                'by': {
                    'runs': 56
                }
            },
            'overs': 20,
            'player_of_match': ['Shubman Gill'],
            'players': {
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

RR_vs_SRH = [
    {
        'match_number': 51,
        'info': {
            'city': 'Jaipur',
            'competition': 'IPL',
            'dates': ['2023-05-07'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Sunrisers Hyderabad',
                'by': {
                    'wickets': 4
                }
            },
            'overs': 20,
            'player_of_match': ['GD Phillips'],
            'players': {
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


PBKS_vs_KKR = [
    {
        'match_number': 52,
        'info': {
            'city': 'Kolkata',
            'competition': 'IPL',
            'dates': ['2023-05-08'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Kolkata Knight Riders',
                'by': {
                    'wickets': 5
                }
            },
            'overs': 20,
            'player_of_match': ['AD Russell'],
            'players': {
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

RCB_vs_MI = [
    {
        'match_number': 53,
        'info': {
            'city': 'Mumbai',
            'competition': 'IPL',
            'dates': ['2023-05-09'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Mumbai Indians',
                'by': {
                    'wickets': 6
                }
            },
            'overs': 20,
            'player_of_match': ['SA Yadav'],
            'players': {
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


CSK_vs_DC = [
    {
        'match_number': 54,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-05-10'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Chennai Super Kings',
                'by': {
                    'runs': 27
                }
            },
            'overs': 20,
            'player_of_match': ['RA Jadeja'],
            'players': {
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

KKR_vs_RR = [
    {
        'match_number': 55,
        'info': {
            'city': 'Kolkata',
            'competition': 'IPL',
            'dates': ['2023-05-11'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Rajasthan Royals',
                'by': {
                    'wickets': 9
                }
            },
            'overs': 20,
            'player_of_match': ['YBK Jaiswal'],
            'players': {
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

MI_vs_GT = [
    {
        'match_number': 56,
        'info': {
            'city': 'Mumbai',
            'competition': 'IPL',
            'dates': ['2023-05-12'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Mumbai Indians',
                'by': {
                    'runs': 27
                }
            },
            'overs': 20,
            'player_of_match': ['SA Yadav'],
            'players': {
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

SRH_vs_LSG = [
    {
        'match_number': 57,
        'info': {
            'city': 'Hyderabad',
            'competition': 'IPL',
            'dates': ['2023-05-13'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Lucknow Super Giants',
                'by': {
                    'wickets': 7
                }
            },
            'overs': 20,
            'player_of_match': ['PN Mankad'],
            'players': {
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

DC_vs_PBKS = [
    {
        'match_number': 58,
        'info': {
            'city': 'Delhi',
            'competition': 'IPL',
            'dates': ['2023-05-13'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Punjab Kings',
                'by': {
                    'runs': 31
                }
            },
            'overs': 20,
            'player_of_match': ['P Simran Singh'],
            'players': {
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

RCB_vs_RR = [
    {
        'match_number': 59,
        'info': {
            'city': 'Jaipur',
            'competition': 'IPL',
            'dates': ['2023-05-14'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Royal Challengers Bangalore',
                'by': {
                    'runs': 112
                }
            },
            'overs': 20,
            'player_of_match': ['WD Parnell'],
            'players': {
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

CSK_vs_KKR = [
    {
        'match_number': 60,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-05-14'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Kolkata Knight Riders',
                'by': {
                    'wickets': 6
                }
            },
            'overs': 20,
            'player_of_match': ['RK Singh'],
            'players': {
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

GT_vs_SRH = [
    {
        'match_number': 61,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-05-15'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Gujarat Titans',
                'by': {
                    'runs': 34
                }
            },
            'overs': 20,
            'player_of_match': ['Shubman Gill'],
            'players': {
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

LSG_vs_MI = [
    {
        'match_number': 62,
        'info': {
            'city': 'Lucknow',
            'competition': 'IPL',
            'dates': ['2023-05-16'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Lucknow Super Giants',
                'by': {
                    'runs': 5
                }
            },
            'overs': 20,
            'player_of_match': ['MP Stoinis'],
            'players': {
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

DC_vs_PBKS = [
    {
        'match_number': 63,
        'info': {
            'city': 'Dharamsala',
            'competition': 'IPL',
            'dates': ['2023-05-17'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Delhi Capitals',
                'by': {
                    'runs': 15
                }
            },
            'overs': 20,
            'player_of_match': ['RR Rossouw'],
            'players': {
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

SRH_vs_RCB = [
    {
        'match_number': 64,
        'info': {
            'city': 'Hyderabad',
            'competition': 'IPL',
            'dates': ['2023-05-18'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Royal Challengers Bangalore',
                'by': {
                    'wickets': 8
                }
            },
            'overs': 20,
            'player_of_match': ['V Kohli'],
            'players': {
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

PBKS_vs_RR = [
    {
        'match_number': 65,
        'info': {
            'city': 'Dharamsala',
            'competition': 'IPL',
            'dates': ['2023-05-19'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Rajasthan Royals',
                'by': {
                    'wickets': 4
                }
            },
            'overs': 20,
            'player_of_match': ['D Padikkal'],
            'players': {
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

CSK_vs_DC = [
    {
        'match_number': 66,
        'info': {
            'city': 'Delhi',
            'competition': 'IPL',
            'dates': ['2023-05-20'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Chennai Super Kings',
                'by': {
                    'runs': 77
                }
            },
            'overs': 20,
            'player_of_match': ['RD Gaikwad'],
            'players': {
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

LSG_vs_KKR = [
    {
        'match_number': 67,
        'info': {
            'city': 'Kolkata',
            'competition': 'IPL',
            'dates': ['2023-05-20'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Lucknow Super Giants',
                'by': {
                    'runs': 1
                }
            },
            'overs': 20,
            'player_of_match': ['N Pooran'],
            'players': {
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

SRH_vs_MI = [
    {
        'match_number': 68,
        'info': {
            'city': 'Mumbai',
            'competition': 'IPL',
            'dates': ['2023-05-21'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Mumbai Indians',
                'by': {
                    'wickets': 8
                }
            },
            'overs': 20,
            'player_of_match': ['C Green'],
            'players': {
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

RCB_vs_GT = [
    {
        'match_number': 68,
        'info': {
            'city': 'Bengaluru',
            'competition': 'IPL',
            'dates': ['2023-05-21'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Gujarat Titans',
                'by': {
                    'wickets': 6
                }
            },
            'overs': 20,
            'player_of_match': ['Shubman Gill'],
            'players': {
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

CSK_vs_GT = [
    {
        'match_number': 69,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-05-23'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Chennai Super Kings',
                'by': {
                    'runs': 15
                }
            },
            'overs': 20,
            'player_of_match': ['RD Gaikwad'],
            'players': {
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

MI_vs_LSG = [
    {
        'match_number': 70,
        'info': {
            'city': 'Chennai',
            'competition': 'IPL',
            'dates': ['2023-05-24'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Mumbai Indians',
                'by': {
                    'runs': 81
                }
            },
            'overs': 20,
            'player_of_match': ['Akash Madhwal'],
            'players': {
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

GT_vs_MI = [
    {
        'match_number': 71,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-05-26'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Gujarat Titans',
                'by': {
                    'runs': 62
                }
            },
            'overs': 20,
            'player_of_match': ['Shubman Gill'],
            'players': {
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

CSK_vs_GT = [
    {
        'match_number': 72,
        'info': {
            'city': 'Ahmedabad',
            'competition': 'IPL',
            'dates': ['2023-05-29'],
            'gender': 'male',
            'match_type': 'T20',
            'outcome': {
                'winner': 'Chennai Super Kings',
                'by': {
                    'wickets': 5
                },
                'method': 'D/L'
            },
            'overs': 20,
            'player_of_match': ['DP Conway'],
            'players': {
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

# ╚═══════════════════════════════ End of Code ═════════════════════════════════╝ #


