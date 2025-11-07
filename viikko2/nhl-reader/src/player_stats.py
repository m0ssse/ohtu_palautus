class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scores_from_country(self, country):
        players = []
        for player in self.reader.read_player_data():
            if player.nationality==country:
                players.append(player)
        players.sort(key = lambda x: -x.score())
        return players