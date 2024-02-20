import random


# The entire game loop
def play_game(total_rounds):
    rps_list = ["rock", "paper", "scissors", "xxx"]

    # Initializes the game variables
    game_history = []
    round_number = 0
    round_tied = 0
    round_lost = 0
    round_won = 0

    while total_rounds == "infinite" or round_number < total_rounds:
        print()
        # Depending on the mode, it chooses what headings to display
        if total_rounds == "infinite":
            print(f"--- Round {round_number + 1} | Infinite Mode ---")
        else:
            print(f"--- Round {round_number + 1} out of {total_rounds} Rounds ---")

        # User's turn to choose
        user_choice = string_checker("Rock, Paper or Scissors (xxx to exit game)? ", rps_list)

        # Exits the game if user types "xxx"
        if round_number == 0 and user_choice == "xxx":
            print()
            print("Game has ended. However, you have not even played one round thus we have not stats or history to "
                  "show you.")
            exit()

        elif user_choice == "xxx":
            break

        # Prints what user chose
        print()
        print(f"You chose: {user_choice}")

        # Computer's turn
        comp_choice = random.choice(rps_list[:-1])

        # Prints what computer chose
        print(f"Computer chose: {comp_choice}")
        print()

        # Decides the winner between the user and the computer
        result = rps_compare(user_choice, comp_choice)

        # Gets feedback depending on results
        if result == "tie":
            round_tied += 1
            feedback = "😐 Its a tie 😐"

        elif result == "lose":
            round_lost += 1
            feedback = "😢 You have lost 😢"

        elif result == "win":
            round_won += 1
            feedback = "😀 You have won 😀"

        # Gets the round feedback and outputs it for the user
        round_feedback = f"{user_choice} vs {comp_choice}, {feedback} has won this round!"
        print(round_feedback)

        # Stores the results into a list
        history_item = f"Round: {round_number + 1} - {round_feedback}"
        game_history.append(history_item)

        round_number += 1

    # Asks the user if they want to view the game stats
    print()
    view_stats = string_checker("Do you want to view the stats? ")
    print()

    # If yes, displays the game stats
    if view_stats == "yes":
        # Calculates the win percentage
        rounds_won = round_won / (round_number - round_tied) * 100

        # Calculates loss percentage
        rounds_lost = round_lost / (round_number - round_tied) * 100

        # Calculates tie percentage
        rounds_tied = round_tied / round_number * 100

        print(f"Out of {total_rounds} rounds:")
        print()
        print(f"- {rounds_won:.2f}% of games won")
        print()
        print(f"- {rounds_lost:.2f}% of games lost")
        print()
        print(f"- {rounds_tied:.2f}% of rounds tied")
        print()

    # Asks the user if they want to view the game history
    view_history = string_checker("Do you want to view the game's round history?")

    # If yes, displays the game history
    if view_history == "yes":
        print("\n⌛⌛⌛ Game History ⌛⌛⌛ ")
        print()
        # Outputs the game history
        for item in game_history:
            print(item)


# Asks the user how many rounds they want to play
def num_rounds():
    while True:
        print()
        num_round = input("How many rounds do you want to play (press <enter> for infinite): ")
        if num_round == "":
            return "infinite"
        try:
            num_round = int(num_round)
            if num_round > 0:
                return num_round
            else:
                print("Please enter a number greater than 0 or press <enter> for infinite mode")
        except ValueError:
            print("Please enter a valid number or press <enter> for infinite mode")


# yes/no checker
def string_checker(question, valid_ans=('yes', 'no')):
    error = f"Please enter a valid answer from the following list: {valid_ans}"
    while True:
        user_response = input(question).lower()
        for item in valid_ans:
            if item.startswith(user_response):
                return item
        print(error)


# Compares between what the user chose and what the computer chose
def rps_compare(user, computer):
    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    # returns the result
    if user == computer:
        return "tie"
    elif win_conditions[user] == computer:
        return "win"
    else:
        return "lose"


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


# Asks the user if they want to see the instructions
want_instructions = string_checker("Do you want to see the instructions? ")

# If yes, outputs it
if want_instructions == "yes":
    instructions()

# Starts the game
total_rounds = num_rounds()
play_game(total_rounds)

print()
print("--- Thanks for Playing --- ")
