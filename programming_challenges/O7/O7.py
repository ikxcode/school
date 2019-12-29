import time
import sys
import random


# menu selection problem
chosen = False
while not chosen:
    try:
        choice = int(input("PLAY GAME(1), instructions(2), quit(3) "))
        if choice == 1:
            print("YOU WIN")
            chosen = True
        elif choice == 2:
            print("Step 1: press 1 to play")
            print("Step 2: win")
            print("PRO TIP: don't press quit")
            print()
        elif choice == 3:
            print("YOU LOSE")
            chosen = True
        else:
            sys.exit()
    except Exception:
        print("You had one job")
        time.sleep(2)
        print("to press a number")
        time.sleep(2)
        print("from 1 to 3")
        time.sleep(2)
        print("and you failed")
        time.sleep(2)
        print("shutting down")
        time.sleep(2)
        sys.exit()


# compound interest problem
def ask_user_for_bank_amounts(question):
    while True:
        try:
            number = int(input(question))
            if number > 0:
                return number
            else:
                print("just give me a positive integer")
        except Exception:
            print("just give me a positive integer")


current_balance = ask_user_for_bank_amounts("How much money have you put in your savings account? ")
interest_rate = ask_user_for_bank_amounts("What is the interest rate (AER) ? ")
desired_balance = ask_user_for_bank_amounts("How much money do you want in your savings account? ")

years = 0
interest_rate = interest_rate / 100
while current_balance < desired_balance:
    years += 1
    current_balance = current_balance + (current_balance * interest_rate)
    print("year " + str(years) + ": " + str(current_balance))

print(str(years) + " years needed to reach desired balance")


# number game
def play_number_game():
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


# gamertag problem
# this program checks the length of gamertags entered

valid_gamertag = True

while valid_gamertag:
    print("Gamertags must be less than 15 characters")
    gamertag = input("Enter your gamertag ")
    gamertag_length = len(gamertag)
    if gamertag_length > 15:
        print("Your gamertag is too long")
    else:
        print("Gamertag accepted")
        valid_gamertag = False


# rock, paper, scissors problem
def convert_choice_to_string(choice):
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"


def print_choice_and_score(cpu_score, player_score, player_choice, cpu_choice):
    print("You picked " + convert_choice_to_string(player_choice))
    print("And the cpu picked " + convert_choice_to_string(cpu_choice))
    print("You have " + str(player_score) + " points and the CPU has " + str(cpu_score) + " points.")
    print()


def is_valid_choice(player_choice):
    return player_choice == 1 or player_choice == 2 or player_choice == 3


def is_not_valid_choice(player_choice):
    return not is_valid_choice(player_choice)


def play_rock_paper_scissors():
    cpu_score = 0
    player_score = 0
    while cpu_score != 10 and player_score != 10:
        cpu_choice = random.randint(1, 3)
        try:
            player_choice = int(input("Rock(1), paper(2) or scissors(3)? "))
        except Exception:
            print("Please select a valid option")
            continue
        if is_not_valid_choice(player_choice):
            print("please select a valid option")
        elif player_choice == cpu_choice:
            print("You both picked " + convert_choice_to_string(player_choice))
            print_choice_and_score(cpu_score, player_score, player_choice, cpu_choice)
        elif player_choice == 3 and cpu_choice == 1:
            print("You lose!")
            cpu_score += 1
            print_choice_and_score(cpu_score, player_score, player_choice, cpu_choice)
        elif cpu_choice == 3 and player_choice == 1:
            print("You win!")
            player_score += 1
            print_choice_and_score(cpu_score, player_score, player_choice, cpu_choice)
        elif player_choice > cpu_choice:
            print("You win!")
            player_score += 1
            print_choice_and_score(cpu_score, player_score, player_choice, cpu_choice)
        elif cpu_choice > player_choice:
            print("You lose!")
            cpu_score += 1
            print_choice_and_score(cpu_score, player_score, player_choice, cpu_choice)

    if cpu_score == 10:
        print("CPU wins!")
    else:
        print("You win!")


play_rock_paper_scissors()


# happy numbers problem
digit_list = []
squared_list = []


number = input("Give me a number and I will check if it is a happy number or not: ")


def split_number_into_digits(number):
    check_for_sad_number(number)
    check_for_happy_number(number)
    number = str(number)
    for digit in number:
        digit = int(digit)
        digit_list.append(digit)
    square_digits()


def square_digits():
    for digit in digit_list:
        squared_digit = digit * digit
        squared_list.append(squared_digit)
    add_digits()


def add_digits():
    added_digit = 0
    for digit in squared_list:
        added_digit = added_digit + digit
    clear_lists()
    split_number_into_digits(str(added_digit))


def clear_lists():
    digit_list.clear()
    squared_list.clear()


def check_for_sad_number(added_digit):
    if added_digit == "4":
        print("The number " + str(number) + " is sad")
        sys.exit()


def check_for_happy_number(added_digit):
    if added_digit == "1":
        print("The number " + str(number) + " is happy")
        sys.exit()


split_number_into_digits(number)
