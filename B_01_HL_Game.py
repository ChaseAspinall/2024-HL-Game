def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instructions():
    print('''

    To begin, chose the number of rounds and either customise the game 
    parameters or go with the default game (between 1 and 100).

    Then chose how many rounds or <enter> for infinite mode>

    Your goal is to guess the number without running out of guesses.

    Good luck>

        ''')


def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


mode = "regular"
rounds_played = 0


print("Welcome to the Higher Lower Game")
print()

want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode:")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

while rounds_played < num_rounds:

    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (Infinite Mode) "
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds} "

    print(rounds_heading)
    print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    if mode == "infinite":
        num_rounds += 1
