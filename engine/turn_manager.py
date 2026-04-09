class TurnManager:
    def __init__(self, players):
        self.players = list(players)
        self.current_index = 0

    def get_current_player(self):
        return self.players[self.current_index] if self.players else None

    def advance(self):
        if not self.players:
            return
        self.current_index = (self.current_index + 1) % len(self.players)

    def remove_player(self, player):
        if player not in self.players:
            return

        removed_index = self.players.index(player)
        self.players.remove(player)

        if not self.players:
            self.current_index = 0
            return

        if removed_index < self.current_index:
            self.current_index -= 1

        self.current_index %= len(self.players)
