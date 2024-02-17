# Check that users have entered a valid
# option based on a list
def rps_compare(user, computer):

    # if the user and the computer choice were the same it's a tie
    if user == computer:
        result = "tie"

    # The three ways to win
    elif user == "paper" and computer == "rock":
        result = "win"

    elif user == "rock" and computer == "scissors":
        result = "win"

    elif user == "scissors" and computer == "paper":
        result = "win"

    # else it's a loss
    else:
        result = "lose"

    return result


# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ('rock', 'rock', 'tie'),
    ('rock', 'paper', 'lose'),
    ('rock', 'scissors', 'win'),
    ('paper', 'paper', 'tie'),
    ('paper', 'rock', 'win'),
    ('paper', 'scissors', 'lose'),
    ('scissors', 'scissors', 'tie'),
    ('scissors', 'rock', 'lose'),
    ('scissors', 'paper', 'win'),
]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    user = item[0]
    computer = item[1]
    expected = item[2]

    # get actual value (ie: test ticket function)
    actual = rps_compare(user, computer)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {user} vs {computer}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {user} vs {computer}, expected: {expected}, received: {actual} ❌❌❌")
