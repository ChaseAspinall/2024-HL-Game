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


secret = 7

low_num = 0
high_num = 10
guesses_allowed = 5

guesses_used = 0
already_guessed = []

guess = ""
while guess != secret and guesses_used < guesses_allowed:

    guess = int_check("Guess: ", low_num, high_num)

    if guess == "xxx":
        end_game = "yes"
        break

    if guess in already_guessed:
        print(f"You've already guessed {guess}. You've *still* used "
              f"{guesses_used} / {guesses_allowed} guesses ")
        continue

    else:
        already_guessed.append(guess)

    guesses_used += 1

    if guess < secret and guesses_used < guesses_allowed:
        feedback = (f"Too low, please try a higher number. "
                    f"You've used {guesses_used} / {guesses_allowed} guesses")
    elif guess > secret and guesses_used < guesses_allowed:
        feedback = (f"Too high, please try a lower number. "
                    f"You've used {guesses_used} / {guesses_allowed} guesses")

    elif guess == secret:

        if guesses_used == 1:
            feedback = "Lucky! You got it on the first guess."
        elif guesses_used == guesses_allowed:
            feedback = f"Phew! You got it in {guesses_used} guesses>"
        else:
            feedback = f"Well done! You guesses the secret number in {guesses_used} guesses."

    else:
        feedback = "Sorry - you have no more guesses. You lose this round!"

    print(feedback)

    if guesses_used == guesses_allowed - 1:
        print("\nCareful - you have one guess left!\n")

print()
print("End of round")
