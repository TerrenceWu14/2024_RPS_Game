# Asks the user how many rounds they want to play or infinite mode
def num_rounds():
    while True:
        num_round = input("How many rounds do you want to play (press <enter> for infinite): ")
        # Returns infinite if the user pressed <enter>
        if num_round == "":
            return "infinite"
        # Returns the number of rounds the user chose
        try:
            num_round = int(num_round)
            # Returns the number of rounds the user chose if it's greater than 0
            if num_round > 0:
                return num_round
            else:
                print("Please enter a number greater than 0 or press <enter> for infinite mode")
        # Handles errors if the input is not a number
        except ValueError:
            print("Please enter a valid number or press <enter> for infinite mode")


# Check that users have entered a valid option based on a list
def string_checker(question, valid_ans=('yes', 'no')):
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

# Gets the total rounds that the user wants to play
total_rounds = num_rounds()
# Initialises Round Number
round_number = 0

if total_rounds == "infinite":
    # Loops infinitely
    while True:
        # Updates the round number at the start of each round
        round_number = round_number + 1
        print(f"--- Round {round_number} | Infinite Mode ---")

        user_choice = string_checker("Rock, Paper or Scissors (xxx to exit)? ", rps_list)
        print(user_choice)
        print()
        # If user types xxx it ends the program
        if user_choice == "xxx":
            exit()

else:
    # Loops until the selected it reaches amount of rounds
    for item in range(1, total_rounds + 1):
        print(f"--- Round {item} out of {total_rounds} ---")
        user_choice = string_checker("Rock, Paper or Scissors (xxx to exit)? ", rps_list)
        print(user_choice)
        print()
        # If user types xxx it ends the program
        if user_choice == "xxx":
            exit()
