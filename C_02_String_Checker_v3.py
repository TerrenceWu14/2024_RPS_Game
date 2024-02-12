# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans):
    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            # Checks if the user response is a word in the list
            if item == user_response:
                return item
            # Checks if the user response
            # is the as the first letter of an item in the list

            elif user_response == item[0]:
                return item


# Main routine

yes_no = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("Do you want ot see the instructions? ",
                                   yes_no)
