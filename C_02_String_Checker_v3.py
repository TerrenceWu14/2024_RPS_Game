# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=['yes', 'no']):
    error = f"Please enter a valid answer from the following list: {valid_ans}"

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

        # Print error if the user does not enter something that is valid
        print(error)
        print()


# Main routine

rps_list = ["rock", "paper", "scissors", "xxx"]

# Asks the user if they want to see the instructions
want_instructions = string_checker("Do you want to see the instructions? ")
print(f"You chose {want_instructions}")

user_choice = string_checker("Rock, Paper or Scissors? ", rps_list)
print(user_choice)
