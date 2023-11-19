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
