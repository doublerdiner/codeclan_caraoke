import unittest
from src.guest import Guest
from src.food import Food
from src.drink import Drink
from src.bar import Bar
from src.reception import Reception
from src.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("David Byrne", 50.00, "Psycho Killer", True)
        self.guest_2 = Guest("Thom Yorke", 10.00, "Karma Police", False)
        self.room_1 = Room(6)
        self.room_2 = Room(2)
        self.reception = Reception(300.00, 7.50, 20)
        self.food_1 = Food("Burger", 8.99)
        self.food_2 = Food("Nachos", 6.50)
        self.drink_1 = Drink("Beer", 4.50)
        self.drink_2 = Drink("Mojito", 11.00)
        self.bar = Bar("If You Like Pina Coladas", 150.00)

# Test 1 - 5 - Guest has a name, money, favourite song and coat

    def test_guest_has_name(self):
        self.assertEqual("David Byrne", self.guest_1.name)

    def test_guest_has_money(self):
        self.assertEqual(50, self.guest_1.money)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Psycho Killer", self.guest_1.favourite_song)
 
    def test_guest_has_a_coat__True(self):
        self.assertEqual(True, self.guest_1.has_coat)

    def test_guest_has_a_coat__False(self):
        self.guest_1 = Guest("David Byrne", 50.00, "Psycho Killer", False)
        self.assertEqual(False, self.guest_1.has_coat)