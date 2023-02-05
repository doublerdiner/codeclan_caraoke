import unittest
from src.reception import Reception
from src.guest import Guest
from src.room import Room
from src.bar import Bar

class TestReception(unittest.TestCase):
    def setUp(self):
        self.reception = Reception(300.00, 7.50, 20)
        self.guest_1 = Guest("David Byrne", 50.00, "Psycho Killer", True)
        self.guest_2 = Guest("Thom Yorke", 10.00, "Karma Police", False)
        self.room_1 = Room(6)
        self.room_2 = Room(1)
        self.bar = Bar("If You Like Pina Coladas", 150.00)

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

# Didn't need to use the room list
    # def test_reception_room_list_empty(self):
    #     self.assertEqual(0, len(self.reception.room_list))

# Test 6 & 7 - Does room have capacity
    def test_does_room_have_capacity__True(self):
        result = self.reception.does_room_have_capacity(self.room_1)
        self.assertEqual(True, result)
    
    def test_does_room_have_capacity__False(self):
        self.room_1.capacity = 0
        result = self.reception.does_room_have_capacity(self.room_1)
        self.assertEqual(False, result)

# Test 8 - Add coat to cloakroom - enough money
    def test_add_coat_to_cloakroom__guests_have_money(self):
        result = self.reception.add_coat_to_cloakroom(self.guest_1)
        self.assertEqual(48, self.guest_1.money)
        self.assertEqual("Thank you for your coat.", result)
        self.assertEqual(1, len(self.reception.coat_list))

# Test 8 - Add coat to cloakroom - no money
    def test_add_coat_to_cloakroom__guests_have_no_money(self):
        self.guest_1.money = 1.50
        result = self.reception.add_coat_to_cloakroom(self.guest_1)
        self.assertEqual(1.50, self.guest_1.money)
        self.assertEqual("I'm sorry. The cloakroom is £2.00.", result)
        self.assertEqual(0, len(self.reception.coat_list))
    
# Test 9 - Add coat to cloakroom - Guest doesn't have a coat
    def test_add_coat_to_cloakroom__guest_has_no_coat(self):
        result = self.reception.add_coat_to_cloakroom(self.guest_2)
        self.assertEqual(10, self.guest_2.money)
        self.assertEqual("You must be chilly.", result)
        self.assertEqual(0, len(self.reception.coat_list))
    
# Test 10 - Return coat to guest - cloakroom holding coat
    def test_retrieve_coat_from_cloakroom(self):
        self.reception.add_coat_to_cloakroom(self.guest_1)
        self.guest_2.has_coat = True
        self.reception.add_coat_to_cloakroom(self.guest_2)
        result = self.reception.retrieve_coat_from_cloakroom(self.guest_1)
        self.assertEqual("Here's your coat.", result)
        self.assertEqual(1, len(self.reception.coat_list))
        self.assertEqual(self.guest_2.name, self.reception.coat_list[0])

# Test 11 - Return coat to guest - cloakroom not holding coat
    def test_retrieve_coat_from_cloakroom__no_coat_held(self):
        self.reception.add_coat_to_cloakroom(self.guest_1)
        result = self.reception.retrieve_coat_from_cloakroom(self.guest_2)
        self.assertEqual("We don't appear to have a coat for you.", result)
        self.assertEqual(1, len(self.reception.coat_list))

# Test 12 - Add guest to room
    def test_check_guest_in(self):
        result = self.reception.check_guest_in(self.guest_1, self.room_1)
        self.assertEqual(1, len(self.room_1.guest_list))
        self.assertEqual(42.50, self.guest_1.money)
        self.assertEqual(result, "Enjoy your night!")
        self.assertEqual(307.50, self.reception.till)

# Test 13 - Add guest to room - Room is full
    def test_check_guest_in__room_is_full(self):
        self.reception.check_guest_in(self.guest_1, self.room_2)
        result = self.reception.check_guest_in(self.guest_2, self.room_2)
        self.assertEqual(1, len(self.room_2.guest_list))
        self.assertEqual(42.50, self.guest_1.money)
        self.assertEqual(10.00, self.guest_2.money)
        self.assertEqual(307.50, self.reception.till)
        self.assertEqual(result, "I'm sorry. That room is full.")

# Test 14 - Add guest to room - Guest has no money
    def test_check_guest_in__guest_has_no_money(self):
        self.guest_2.money = 3.00
        result = self.reception.check_guest_in(self.guest_2, self.room_1)
        self.assertEqual(0, len(self.room_1.guest_list))
        self.assertEqual(3.00, self.guest_2.money)
        self.assertEqual(300, self.reception.till)
        self.assertEqual(result, "I'm sorry the entry fee is £7.50.")

# Test 15 - Check guest out
    def test_check_guest_out(self):
        self.reception.check_guest_in(self.guest_1, self.room_1)
        self.reception.check_guest_out(self.guest_1, self.room_1, self.bar)
        self.assertEqual(0, len(self.room_1.guest_list))
    
# Test 16 - Guest tries to leave without paying their bill
    def test_check_guest_out_unpaid_tab(self):
        self.reception.check_guest_in(self.guest_1, self.room_1)
        self.bar.bar_tab[self.room_1] = ["example"]
        result = self.reception.check_guest_out(self.guest_1, self.room_1, self.bar)
        self.assertEqual(1, len(self.room_1.guest_list))
        self.assertEqual("I'm sorry. You can't leave until you've settled your bar tab.", result)

# Test 17 - Add coat to cloakroom. Cloakroom is full
    def test_cloakroom_is_full(self):
        self.reception.coat_capacity = 1
        self.reception.add_coat_to_cloakroom(self.guest_1)
        result = self.reception.add_coat_to_cloakroom(self.guest_1)
        self.assertEqual(1, len(self.reception.coat_list))
        self.assertEqual("I'm sorry the cloakroom is full.", result)