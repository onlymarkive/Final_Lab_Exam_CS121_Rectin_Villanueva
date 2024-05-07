class Score:

def __init__(self)
    self.rounds_played = 0
    self.player_wins = 0
    self.opponent_wins = 0

def add_round(self):
    self.rounds_played += 1

def add_player_win(self):
    self.player_wins += 1 

def add_opponent_win(self):
    self.opponent_wins += 1

def calculate_points(self):
    if self.player_wins == 3:
        return 3
    else:
        return self.player_wins
