import unittest
from src.reception import Reception
from src.guest import Guest
from src.room import Room

class TestReception(unittest.TestCase):
    def setUp(self):
        self.reception = Reception(300.00, 7.50, 20)
        self.guest_1 = Guest("David Byrne", 50.00, "Psycho Killer", True)
        self.guest_2 = Guest("Thom Yorke", 10.00, "Karma Police", False)
        self.room_1 = Room(6)
        self.room_2 = Room(2)

# Test 1 - 3 - Reception has a till, entry_fee and coat_capacity
    def test_reception_has_till(self):
        self.assertEqual(300, self.reception.till)

    def test_reception_has_entry_fee(self):
        self.assertEqual(7.50, self.reception.entry_fee)

    def test_reception_has_coat_capacity(self):
        self.assertEqual(20, self.reception.coat_capacity)

# Test 4 & 5 - Reception coat_list and room_list are empty
    def test_reception_coat_list_empty(self):
        self.assertEqual(0, len(self.reception.coat_list))

    def test_reception_room_list_empty(self):
        self.assertEqual(0, len(self.reception.room_list))