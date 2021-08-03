def get_valid_answer(valid_answers, prompt):
    """Takes answer choices and prompt, asks user for answer until it is valid, returns valid answer"""
    while True:
        play = input(prompt)
        if play in valid_answers:
            return play
        else:
            print("Invalid answer, try again!")

def format_list_to_string(in_list):
    """Takes a list of items and formats them to add commas and 'and' in the right spots. Returns a string"""
    len_list = len(in_list)
    out_string = ""
    for i in range(len_list-1):
        out_string += f"{in_list[i]}, "
    out_string += f"and {in_list[len_list-1]}"
    return out_string
