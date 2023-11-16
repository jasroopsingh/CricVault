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
