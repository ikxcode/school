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


# XP problem
total_XP = 0
rank = 1

while total_XP < 2000:
    XP = int(input("Enter the XP you earned last game: "))
    total_XP = total_XP + XP
    if total_XP >= 1500 and rank < 5:
        print("You have been promoted to Warrant Officer ")
        rank = 5
    elif total_XP >= 700 and rank < 4:
        print("You have been promoted to Staff Sergeant ")
        rank = 4
    elif total_XP >= 300 and rank < 3:
        print("You have been promoted to Sergeant ")
        rank = 3
    elif total_XP >= 100 and rank < 2:
        print("You have been promoted to Corporal ")
        rank = 2

    print("Total XP: " + str(total_XP))


# happy numbers problem
def run_happy_numbers_problem():
    is_recurring = False
    is_happy = False
    number = get_user_input()
    number_str = number
    while not is_recurring and not is_happy:
        digit_list = split_number_into_digits(number_str)
        squared_list = square_digits(digit_list)
        sum_of_digits = sum_digits(squared_list)
        number_str = str(sum_of_digits)
        is_recurring = is_number_recurring(sum_of_digits)
        is_happy = is_number_happy(sum_of_digits)

    if is_recurring:
        print("the number " + number + " is sad")
    elif is_happy:
        print("the number " + number + " is happy")


def get_user_input():
    while True:
        try:
            number = input("Give me a positive integer and I will check if it is happy or sad: ").strip()
            if int(number) <= 0:
                print("That is not a positive integer")
            else:
                return number
        except Exception:
            print("That is not a positive integer")


def split_number_into_digits(number):
    digit_list = []
    for digit in number:
        digit_int = int(digit)
        digit_list.append(digit_int)
    return digit_list


def square_digits(digit_list):
    squared_list = []
    for digit in digit_list:
        squared_digit = digit * digit
        squared_list.append(squared_digit)
    return squared_list


def sum_digits(squared_list):
    sum = 0
    for digit in squared_list:
        sum += digit
    return sum


def is_number_recurring(number):
    return number == 4


def is_number_happy(number):
    return number == 1


run_happy_numbers_problem()
