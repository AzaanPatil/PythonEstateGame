import unittest
from models.player import Player
from models.property import Property
from systems.economy import buy_property, pay_rent

class TestEconomy(unittest.TestCase):

    def test_buy_property(self):
        p = Player("Buyer")
        prop = Property("Test", 500, 50)

        buy_property(p, prop)

        self.assertEqual(prop.owner, p)
        self.assertIn(prop, p.properties)

    def test_pay_rent(self):
        owner = Player("Owner")
        renter = Player("Renter")
        prop = Property("Test", 500, 50)

        prop.owner = owner
        pay_rent(renter, prop)

        self.assertEqual(renter.balance, 9950)
        self.assertEqual(owner.balance, 10050)

if __name__ == "__main__":
    unittest.main()