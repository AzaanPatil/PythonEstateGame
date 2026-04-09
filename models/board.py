class Board:
    def __init__(self, tiles):
        self.tiles = list(tiles)

    def move_player(self, player, steps):
        previous_position = player.position
        player.position = (player.position + steps) % len(self.tiles)
        passed_start = player.position < previous_position
        return self.tiles[player.position], passed_start

    def get_tile(self, position):
        return self.tiles[position % len(self.tiles)]
