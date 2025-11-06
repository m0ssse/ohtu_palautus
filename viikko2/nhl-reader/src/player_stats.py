class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
    
    def top_scores_from_country(self, country):
        return sorted([player for player in self.reader.read_player_data() if player.nationality==country], key = lambda x: (-x.goals-x.assists))