import score_writer
from dice_roller import DiceRoller


def play_round(player1_score, player2_score):
    print()
    input("Player 1: Press enter to roll")
    player1_score += DiceRoller.roll()
    print()
    print("Player 1 now has " + str(player1_score) + " points! \n")

    print()
    input("Player 2: Press enter to roll")
    player2_score += DiceRoller.roll()
    print()
    print("Player 2 now has " + str(player2_score) + " points! \n")

    return player1_score, player2_score


def play_game():
    player1_score = 0
    player2_score = 0

    for rounds in range(5):
        scores = play_round(player1_score, player2_score)
        player1_score = scores[0]
        player2_score = scores[1]

    if player1_score == player2_score:
        print("\n TIEBREAKER")
        while player1_score == player2_score:
            player1_score += DiceRoller.roll_single()
            print("Player 1 now has " + str(player1_score) + " points! \n")
            player2_score += DiceRoller.roll_single()
            print("Player 2 now has " + str(player2_score) + " points! \n")

    score_writer.write_score(show_scores(player1_score, player2_score))


def validate(player_number):
    valid = False
    while not valid:
        player_name = input("Player " + str(player_number)
                            + ": Please enter your name (between 3 and 12 characters): ")

        if 3 <= len(player_name) <= 12:
            print("\n Here are the top 5 scores:")
            return player_name
        elif len(player_name) < 3:
            print("That name is too short! Please enter a different name")
        else:
            print("That name is too long! Please enter a different name")


def show_scores(player1_score, player2_score):
    print("\n FINAL SCORES:")
    print("Player 1 has " + str(player1_score) + " points!")
    print("Player 2 has " + str(player2_score) + " points!")

    if player1_score > player2_score:
        score_difference = player1_score - player2_score
        print("Player 1 beat player 2 by " + str(score_difference) + " points")
        player_name = validate(1)
        winner_score = player1_score
    else:
        score_difference = player2_score - player1_score
        print("Player 2 beat player 1 by " + str(score_difference) + " points")
        player_name = validate(2)
        winner_score = player2_score

    return player_name, winner_score
