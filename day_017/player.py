class Player:
    def __init__(self, name, games_played=0):
        self.name = name
        self.games_played = games_played

    def play_game(self):
        self.games_played += 1

    def show_stats(self):
        return self.games_played