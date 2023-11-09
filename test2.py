import os
import json

def get_match_records(database_folder):
    """
    Function to get the match records from the cricsheet database.

    Parameters:
    - database_folder: str
        The path to the cricsheet database folder.

    Returns:
    - dict:
        A dictionary containing the match records with match IDs as keys and match details as values.
    """

    match_records = {}

    # Checking if the database folder exists
    if not os.path.exists(database_folder):
        raise FileNotFoundError("Database folder not found.")

    # Looping through the files in the database folder
    for filename in os.listdir(database_folder):
        file_path = os.path.join(database_folder, filename)

        # Checking if the file is a JSON file
        if os.path.isfile(file_path) and filename.endswith(".json"):
            with open(file_path, "r") as file:
                try:
                    # Loading the JSON data
                    match_data = json.load(file)

                    # Extracting the match ID from the file name
                    match_id = filename.split(".")[0]

                    # Adding the match details to the match records dictionary
                    match_records[match_id] = match_data

                except json.JSONDecodeError:
                    print(f"Error decoding JSON data in file: {filename}")

    return match_records


def print_match_info(match_records, match_id):
    """
    Function to print the match information for a given match ID.

    Parameters:
    - match_records: dict
        A dictionary containing the match records with match IDs as keys and match details as values.
    - match_id: str
        The match ID for which the information is to be printed.
    """

    # Checking if the match ID exists in the match records
    if match_id not in match_records:
        print(f"No match records found for match ID: {match_id}")
        return

    # Getting the match details for the given match ID
    match_details = match_records[match_id]

    # Extracting the required information from the match details
    team1 = match_details["info"]["teams"][0]
    team2 = match_details["info"]["teams"][1]
    playing11 = match_details["innings"][0]["1st innings"]["deliveries"][0]["batsman"]
    squad = match_details["info"]["teams"]
    result = match_details["info"]["outcome"]["winner"]

    # Checking if the match was tied
    if result == "tie":
        super_result = match_details["info"]["outcome"]["result"]
        print(f"Match ID: {match_id}")
        print(f"Team 1: {team1}")
        print(f"Team 2: {team2}")
        print(f"Playing 11: {playing11}")
        print(f"Squad: {squad}")
        print("Result: Tied")
        print(f"Super Result: {super_result}")
    else:
        print(f"Match ID: {match_id}")
        print(f"Team 1: {team1}")
        print(f"Team 2: {team2}")
        print(f"Playing 11: {playing11}")
        print(f"Squad: {squad}")
        print(f"Result: {result}")


# Example usage:

# Get the match records from the cricsheet database folder
database_folder = "cricsheet_folder"
match_records = get_match_records(database_folder)

# Ask the user for the match ID
match_id = input("Enter the match ID: ")

# Print the match information for the given match ID
print_match_info(match_records, match_id)