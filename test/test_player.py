import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):

    def test_initial_values(self):
        p = Player("Test")
        self.assertEqual(p.balance, 10000)
        self.assertEqual(p.position, 0)
        self.assertEqual(len(p.properties), 0)

    def test_dice_roll(self):
        p = Player("Test")
        roll = p.roll_dice()
        self.assertTrue(1 <= roll <= 6)

if __name__ == "__main__":
    unittest.main()