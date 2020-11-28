import score_keeper


def write_score(player_name, winner_score):
    high_scores = open("high_scores.txt", "a")
    high_scores.write(player_name + " " + str(winner_score) + " \n")
    high_scores.close()

    high_scores = open("high_scores.txt", "r")
    scoreboard = score_keeper.TopPlayers()
    for score in high_scores:
        ps = score_keeper.PlayerScore()
        scoreline = score.split(" ")
        sanitised_number = int(scoreline[1].strip())
        ps.score = sanitised_number
        ps.name = scoreline[0]
        scoreboard.insert_score(ps)
    high_scores.close()

    for player in scoreboard.top_5_players:
        print(player.name + " " + str(player.score))
