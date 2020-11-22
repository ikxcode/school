
class PlayerScore:
    name = ""
    score = 0


class TopPlayers:
    top_5_players = []


    def insert_score(self, new_player):
        num_of_players = len(self.top_5_players)
        if num_of_players > 4:
            if new_player.score > self.top_5_players[-1].score:
                self.remove_lowest_player()
                self.add_new_player(new_player)
        else:
            self.add_new_player(new_player)

    def remove_lowest_player(self):
        del self.top_5_players[-1]

    def add_new_player(self, new_player):
        num_of_players = len(self.top_5_players)
        if num_of_players > 0:
            added_score = False
            for i in range(num_of_players):
                if new_player.score > self.top_5_players[i].score:
                    self.top_5_players.insert(i, new_player)
                    added_score = True
                    break
            if not added_score:
                self.top_5_players.append(new_player)
        else:
            self.top_5_players.append(new_player)


def return_score(entry):
    return entry.player


