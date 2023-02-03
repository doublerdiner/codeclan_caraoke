import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Beer", 4.50)
        self.drink_2 = Drink("Mojito", 11.00)

# Test 1 & 2 - Drink has a name and price
    def test_drink_has_name(self):
        self.assertEqual("Beer", self.drink_1.name)

    def test_drink_has_price(self):
        self.assertEqual(4.50, self.drink_1.price)