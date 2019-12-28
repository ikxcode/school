import random


def play_number_game(self):
    guess = -1
    guesses = 0
    answer = random.randint(1,100)

    while guess != answer:
        guesses += 1
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess == answer:
                print("You got the answer in " + str(guesses) + " guesses!")
            elif guess >= answer:
                print("Too high!")
                print("You have guessed " + str(guesses) + " times.")
            elif guess <= answer:
                print("Too low!")
                print("You have guessed " + str(guesses) + " times.")
        except Exception:
            print("That is not an integer.")
            print("You have guessed " + str(guesses) + " times.")


play_number_game()
