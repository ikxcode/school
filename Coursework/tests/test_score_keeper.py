from score_keeper import PlayerScore, TopPlayers

scoreboard = TopPlayers()
scores = {"c": 3, "a": 7, "b": 2, "e": 5, "f": 6, "d": 1}
for key, value in scores.items():
    ps = PlayerScore()
    ps.score = value
    ps.name = key
    scoreboard.insert_score(ps)
    print("Adding: " + key + "," + str(value))

for player in scoreboard.top_5_players:
    print(player.name + " " + str(player.score))
