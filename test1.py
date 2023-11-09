class CricketMatchRecord:
    """
    Class to represent a cricket match record.

    Attributes:
    - match_id: int
        The unique identifier for the match.
    - team1: str
        The name of the first team.
    - team2: str
        The name of the second team.
    - winner: str
        The name of the winning team.
    - date: str
        The date of the match.
    """

    def __init__(self, match_id: int, team1: str, team2: str, winner: str, date: str):
        """
        Constructor to instantiate the CricketMatchRecord class.

        Parameters:
        - match_id: int
            The unique identifier for the match.
        - team1: str
            The name of the first team.
        - team2: str
            The name of the second team.
        - winner: str
            The name of the winning team.
        - date: str
            The date of the match.
        """

        self.match_id = match_id
        self.team1 = team1
        self.team2 = team2
        self.winner = winner
        self.date = date

    def __str__(self):
        """
        Returns a string representation of the CricketMatchRecord object.

        Returns:
        - str:
            A string representation of the match record.
        """

        return f"Match ID: {self.match_id}\n" \
               f"Team 1: {self.team1}\n" \
               f"Team 2: {self.team2}\n" \
               f"Winner: {self.winner}\n" \
               f"Date: {self.date}"


def print_cricket_match_records(records):
    """
    Function to print the information of cricket match records.

    Parameters:
    - records: list
        A list of CricketMatchRecord objects.
    """

    for record in records:
        print(record)
        print()
