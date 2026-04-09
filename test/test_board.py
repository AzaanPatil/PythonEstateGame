import unittest
from models.board import Board
from models.tile import Tile
from models.player import Player

class TestBoard(unittest.TestCase):

    def test_movement(self):
        tiles = [Tile("start"), Tile("tax"), Tile("card")]
        board = Board(tiles)

        player = Player("Test")
        board.move_player(player, 2)

        self.assertEqual(player.position, 2)

    def test_wraparound(self):
        tiles = [Tile("start"), Tile("tax"), Tile("card")]
        board = Board(tiles)

        player = Player("Test")
        board.move_player(player, 5)

        self.assertEqual(player.position, 2)

if __name__ == "__main__":
    unittest.main()