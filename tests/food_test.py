import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food_1 = Food("Burger", 8.99)
        self.food_2 = Food("Nachos", 6.50)

# Test 1 & 2 - Food has a name and price
    def test_food_has_name(self):
        self.assertEqual("Burger", self.food_1.name)

    def test_food_has_price(self):
        self.assertEqual(8.99, self.food_1.price)
