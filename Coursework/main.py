import hashlib
import unicodedata
import random
import sys

from dice_roller import DiceRoller
from score_keeper import TopPlayers, PlayerScore



def authenticate(password, password_checksum):
    normalised_password = unicodedata.normalize("NFKD", password).encode("ascii", "ignore")
    checksummifier = hashlib.md5()
    checksummifier.update(normalised_password)

    if password_checksum == checksummifier.hexdigest():
        print("Correct password \n")
    else:
        print("Invalid password")
        print("Exiting game...")
        sys.exit()



def play_round(player1_score, player2_score):
    print()
    input("Player 1: Press enter to roll")
    player1_score += DiceRoller.roll()
    print("Player 1 now has " + str(player1_score) + " points! \n")

    input("Player 2: Press enter to roll")
    player2_score += DiceRoller.roll()
    print("Player 2 now has " + str(player2_score) + " points! \n")

    scores = [player1_score, player2_score]
    return scores


player1_password_checksum = "2ca3b093eacd099fc8b7f9cfdefebec5"
player2_password_checksum = "c1e853fcba4b2dd76c2940774700777f"

player1_password = input("Player 1 password: ")
authenticate(player1_password, player1_password_checksum)

player2_password = input("Player 2 password: ")
authenticate(player2_password, player2_password_checksum)


player1_score = 0
player2_score = 0

for rounds in range(5):
    # p1score, p2score = play_round(player1_score, player2_score)
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

print("\n FINAL SCORES:")
print("Player 1 has " + str(player1_score) + " points!")
print("Player 2 has " + str(player2_score) + " points!")


if player1_score > player2_score:
    score_difference = player1_score - player2_score
    print("Player 1 beat player 2 by " + str(score_difference) + " points")
    player_name = input("Player 1: Please enter your name: ")
    winner_score = player1_score
else:
    score_difference = player2_score - player1_score
    print("Player 2 beat player 1 by " + str(score_difference) + " points")
    player_name = input("Player 2: Please enter your name: ")
    print()
    winner_score = player2_score

high_scores = open("high_scores.txt", "a")
high_scores.write(player_name + " " + str(winner_score) + " \n")
high_scores.close()

high_scores = open("high_scores.txt", "r")
scoreboard = TopPlayers()
for score in high_scores:
    ps = PlayerScore()
    scoreline = score.split(" ")
    sanitised_number = int(scoreline[1].strip())
    ps.score = sanitised_number
    ps.name = scoreline[0]
    scoreboard.insert_score(ps)
high_scores.close()

for player in scoreboard.top_5_players:
    print(player.name + " " + str(player.score))


'''
high_scores = open("high_scores.txt", "r")
sorted_scores = {

}
for score in high_scores:
    number = score.split(" ")
    sanitised_number = number[1].strip()
    sorted_scores.append(int(sanitised_number))
high_scores.close()

sorted_scores.sort(reverse=True)
top_5_scores = []
for top_5 in range(5):
    top_5_scores.append(sorted_scores[top_5])

high_scores = open("high_scores.txt", "r")
top_5_players = []
for position in top_5_scores:
    player_list = high_scores.readlines()
    for player in player_list:

        sanitised_number = number[1].strip()
        if int(sanitised_number) == position:
            top_5_players.append(score)

top_5_players.sort(reverse=True)
print("Here are the top 5 players:")
for ranking in range(5):
    print(top_5_players[ranking])
'''