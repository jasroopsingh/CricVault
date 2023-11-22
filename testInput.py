from matchDatabase import get_match_info
 
def display_match_info(match_name: str, match_number: int):
    """
    Function to display the match information for a given match name and match number.
 
    Parameters:
    - match_name: str
        The name of the match for which the information is to be displayed.
    - match_number: int
        The number of the match for which the information is to be displayed.
 
    Returns:
    - None
 
    Prints the match information if available, otherwise prints an error message.
    """
 
    # Get the match information using the provided match name and match number
    match_info = get_match_info(match_name, match_number)
 
    # Check if match information is available
    if match_info:
        print(f"Match Information for Match Number {match_info['match_number']}:")
        print(f"City: {match_info['info']['city']}")
        print(f"Competition: {match_info['info']['competition']}")
        print(f"Dates: {', '.join(match_info['info']['dates'])}")
        print(f"Match Type: {match_info['info']['match_type']}")
    else:
        print("Match information not found.")
 
# Example usage of the display_match_info function
match_name = "GT_vs_CSK"
match_number = 1
display_match_info(match_name, match_number)
