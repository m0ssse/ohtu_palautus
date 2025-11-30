class TennisGame:
    score_string = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        elif player_name == self.player2_name:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            if self.player1_score <= 2:
                score = f"{TennisGame.score_string[self.player1_score]}-All"
            else:
                score = "Deuce"
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score_difference = self.player1_score - self. player2_score

            if score_difference == 1:
                score = f"Advantage {self.player1_name}"
            elif score_difference == -1:
                score = f"Advantage {self.player2_name}"
            elif score_difference >= 2:
                score = f"Win for {self.player1_name}"
            else:
                score = f"Win for {self.player2_name}"
        else:
            score = f"{TennisGame.score_string[self.player1_score]}-{TennisGame.score_string[self.player2_score]}"

        return score
