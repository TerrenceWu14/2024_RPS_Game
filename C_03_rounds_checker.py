# Asks the user how many rounds they want to play or infinite mode
def num_rounds():
    while True:
        num_round = input("How many rounds do you want to play (press <enter> for infinite): ")
        # Returns infinite if the user pressed <enter>
        if num_round == "":
            return "infinite"
        # Returns the number of rounds the user chose
        num_round > 0:
            return num_round
        # Anything else gets sent back to the start of the loop
        else:
            print("Please either press <enter> for infinite mode "
                  "or type the number (greater than 0) of rounds you want to play")
            print()


for item in range(0, 5):
    rounds = num_rounds()
    print(rounds)
