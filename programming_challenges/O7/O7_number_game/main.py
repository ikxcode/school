import random


class NumberGame:
    def __init__(self):
        self.guess = -1
        self.guesses = 0
        self.answer = random.randint(1, 100)

    def play_number_game(self):
        while self.guess != self.answer:
            self.guesses += 1
            try:
                self.guess = int(input("Guess a number between 1 and 100: "))
                if self.guess == self.answer:
                    print("You got the answer in " + str(self.guesses) + " guesses!")
                elif self.guess >= self.answer:
                    print("Too high!")
                    print("You have guessed " + str(self.guesses) + " times.")
                elif self.guess <= self.answer:
                    print("Too low!")
                    print("You have guessed " + str(self.guesses) + " times.")
            except Exception:
                print("That is not an integer.")
                print("You have guessed " + str(self.guesses) + " times.")


number_game = NumberGame()
number_game.play_number_game()
