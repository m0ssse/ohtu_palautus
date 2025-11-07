class Player:
    def __init__(self, data):
        self.name = data['name']
        self.nationality = data['nationality']
        self.assists = data['assists']
        self.goals = data['goals']
        self.team = data['team']
        self.games = data['games']
        self.id = data['id']

    def score(self):
        return self.goals+self.assists

    def __str__(self):
        return f"{self.name:20}{self.team:20}{self.goals:>3} + {self.goals:<3} ={self.score():>4}"
