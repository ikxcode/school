import random


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
