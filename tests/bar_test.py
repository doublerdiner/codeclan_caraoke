import unittest
from src.bar import Bar
from src.drink import Drink
from src.food import Food
from src.guest import Guest

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar("If You Like Pina Coladas", 150.00)
        self.drink_1 = Drink("Beer", 4.50)
        self.drink_2 = Drink("Mojito", 11.00)
        self.food_1 = Food("Burger", 8.99)
        self.food_2 = Food("Nachos", 6.50)
        self.guest_1 = Guest("David Byrne", 50.00, "Psycho Killer", True)
        self.guest_2 = Guest("Thom Yorke", 10.00, "Karma Police", False)

# Test 1 & 2 - Bar has a name and a till
    def test_bar_has_name(self):
        self.assertEqual("If You Like Pina Coladas", self.bar.name)

    def test_bar_has_till(self):
        self.assertEqual(150, self.bar.till)

# Test 3 - 5 - Bar has an empty bar_tab, drinks_list and foods_list
    def test_bar_tab_is_empty(self):
        self.assertEqual(0, len(self.bar.bar_tab))
    
    def test_bar_drinks_list_is_empty(self):
        self.assertEqual(0, len(self.bar.drinks_list))

    def test_bar_foods_list_is_empty(self):
        self.assertEqual(0, len(self.bar.foods_list))

    