import random


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


# Compares the user's choice and the comp choice to decide round result
# returning either win, lose or tie
def rps_compare(user, computer):
    # if the user and the computer choice were the same it's a tie
    if user == computer:
        round_results = "tie"

    # The three ways to win
    elif user == "paper" and computer == "rock":
        round_results = "win"

    elif user == "rock" and computer == "scissors":
        round_results = "win"

    elif user == "scissors" and computer == "paper":
        round_results = "win"

    # else it's a loss
    else:
        round_results = "lose"

    return round_results


# Displays instructions
def instructions():
    print('''
*** Instructions ***

To begin you must first set a number of rounds to play with the computer (or play infinite mode)

Then play against the computer. You can either choose R (Rock), P (Paper) or S (Scissors). 

These are the rules to determine the winner of a round:
- Paper beats rock
- Rock beats scissors
- Scissors beats paper
    ''')


# Main routine

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

# Asks the user if they want to see the instructions
want_instructions = string_checker("Do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()

# Gets the total rounds that the user wants to play
total_rounds = num_rounds()

# Initialises game variables
round_number = 0
round_tied = 0
round_lost = 0

if total_rounds == "infinite":
    # Loops infinitely
    while True:
        # Updates the round number at the start of each round
        round_number = round_number + 1
        print()
        print(f"--- Round {round_number} | Infinite Mode ---")

        user_choice = string_checker("Rock, Paper or Scissors (xxx to exit game)? ", rps_list)
        print()
        print(f"You chose: {user_choice}")
        # If user types xxx it ends the program
        if user_choice == "xxx":
            exit()

        # Computer's Choice
        print()
        comp_choice = random.choice(rps_list[:-1])
        print(f"Computer chose: {comp_choice}")
        print()

        # Decides and outputs the winner
        result = rps_compare(user_choice, comp_choice)

        # Adjusts the rounds lost/win/tie and updates game history
        if result == "tie":
            round_tied += 1
            feedback = "😐Its a tie😐"

        elif result == "lose":
            round_lost += 1
            feedback = "😢You have lost😢"
        elif result == "win":
            feedback = "😀You have won😀"

        # stores the result of the round into this variable
        round_feedback = f"{user_choice} vs {comp_choice}, {feedback} has won this round!"

        # Adds to the game history list for the result of the round
        history_item = f"Round: {round_number} - {round_feedback}"

        # outputs the round's result
        print(round_feedback)

        # Adds the round's result into the list
        game_history.append(history_item)

        print(game_history)

else:
    # Loops until the selected it reaches amount of rounds
    for item in range(1, total_rounds + 1):
        print()
        print(f"--- Round {item} out of {total_rounds} ---")
        user_choice = string_checker("Rock, Paper or Scissors (xxx to exit game)? ", rps_list)
        print(f"You chose: {user_choice}")
        print()

        if user_choice == "xxx":
            exit()

        # Computer's Choice
        comp_choice = random.choice(rps_list[:-1])
        print(f"Computer chose: {user_choice}")

        # Decides and outputs the winner
        result = rps_compare(user_choice, comp_choice)

        if result == "win":
            result = "User"
        else:
            result = "The Computer"

        print(f"{result} has won this round!")
