
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
    
    To begin, chose the number of rounds and either customise the game parameters or go with the default game (between 1 and 100).
    
    Then chose how many rounds or <enter> for infinite mode>
    
    Your goal is to guess the number without running out of guesses.
    
    Good luck>
    
        ''')


print()
print("Welcome to the Higher Lower Game")
print()


want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()
print("Program continues")
