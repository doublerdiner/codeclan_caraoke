import unittest
from src.bar import Bar
from src.drink import Drink
from src.food import Food
from src.guest import Guest
from src.room import Room

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar("If You Like Pina Coladas", 150.00)
        self.drink_1 = Drink("Beer", 4.50)
        self.drink_2 = Drink("Mojito", 11.00)
        self.food_1 = Food("Burger", 8.99)
        self.food_2 = Food("Nachos", 6.50)
        self.guest_1 = Guest("David Byrne", 50.00, "Psycho Killer", True)
        self.guest_2 = Guest("Thom Yorke", 10.00, "Karma Police", False)
        self.room_1 = Room(6)
        self.room_2 = Room(2)

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

# Test 6 - Add drink to bar
    def test_add_drink_to_bar(self):
        self.bar.add_drink_to_bar(self.drink_1)
        self.bar.add_drink_to_bar(self.drink_2)
        self.assertEqual(2, len(self.bar.drinks_list))

# Test 7 - Add food to bar
    def test_add_food_to_bar(self):
        self.bar.add_food_to_bar(self.food_1)
        self.bar.add_food_to_bar(self.food_2)
        self.assertEqual(2, len(self.bar.foods_list))

# Test 8 - Sell drink to guest - Guest does not have a drink already, and has money
# Adding 2 guests to room, adding 2 drinks to bar, selling 1 drink. 
# Checking the room has been added to bar_tab dictionary
# Checking the drink has been removed from the bar drinks list
# Checking the wealth of the room has been lowered by the price of the drink
# Checking the bar tab for the room has added the drink (added as {room: [drinks], room:[drinks]})
    def test_sell_drink__guest_has_money_and_has_drink__False(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.room_1.add_guest_to_guest_list(self.guest_2)
        self.bar.add_drink_to_bar(self.drink_1)
        self.bar.add_drink_to_bar(self.drink_2)
        self.bar.sell_drink(self.drink_1, self.guest_1, self.room_1)
        self.assertEqual(1, len(self.bar.bar_tab))
        self.assertEqual(1, len(self.bar.drinks_list))
        self.assertEqual(55.50, self.room_1.wealth_of_the_room)
        self.assertEqual([self.drink_1], self.bar.bar_tab[self.room_1])
    
# # Test 9 - Sell drink to guest - guest is already holding a drink
# # Same criteria as test 8
    def test_sell_drink__guest_has_money_and_has_drink__True(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.room_1.add_guest_to_guest_list(self.guest_2)
        self.bar.add_drink_to_bar(self.drink_1)
        self.bar.add_drink_to_bar(self.drink_2)
        self.guest_1.has_drink = True
        result = self.bar.sell_drink(self.drink_1, self.guest_1, self.room_1)
        self.assertEqual(0, len(self.bar.bar_tab))
        self.assertEqual(2, len(self.bar.drinks_list))
        self.assertEqual(60, self.room_1.wealth_of_the_room)
        self.assertEqual("You already appear to have a drink.", result)

# Test 10 - Sell drink to guest - Guest has no money
    def test_sell_drink__guest_has_no_money(self):
        self.guest_1.money = 2.00
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.bar.add_drink_to_bar(self.drink_1)
        self.bar.add_drink_to_bar(self.drink_2)
        self.bar.sell_drink(self.drink_1, self.guest_1, self.room_1)
        self.assertEqual(1, len(self.bar.bar_tab))
        self.assertEqual(2, len(self.bar.drinks_list))
        self.assertEqual(2, self.room_1.wealth_of_the_room)
        self.assertEqual([], self.bar.bar_tab[self.room_1])

# Test 11 - Sell drink to guest - Multiple rooms
    def test_sell_drink__guest_has_money_and_has_drink__False_multiple_rooms(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.room_2.add_guest_to_guest_list(self.guest_2)
        self.bar.add_drink_to_bar(self.drink_1)
        self.bar.add_drink_to_bar(self.drink_1)
        self.bar.add_drink_to_bar(self.drink_2)
        self.bar.sell_drink(self.drink_1, self.guest_1, self.room_1)
        self.bar.sell_drink(self.drink_2, self.guest_1, self.room_1)
        self.bar.sell_drink(self.drink_1, self.guest_2, self.room_2)
        self.assertEqual(2, len(self.bar.bar_tab))
        self.assertEqual(0, len(self.bar.drinks_list))
        self.assertEqual(34.50, self.room_1.wealth_of_the_room)
        self.assertEqual(5.50, self.room_2.wealth_of_the_room)
        self.assertEqual([self.drink_1, self.drink_2], self.bar.bar_tab[self.room_1])
        self.assertEqual([self.drink_1], self.bar.bar_tab[self.room_2])
    
    # Test 11 - Sell drink to guest - Drink not available
    def test_sell_drink__drink_not_in_stock(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.bar.add_drink_to_bar(self.drink_1)
        self.bar.sell_drink(self.drink_1, self.guest_1, self.room_1)
        result = self.bar.sell_drink(self.drink_1, self.guest_1, self.room_1)
        self.assertEqual(1, len(self.bar.bar_tab))
        self.assertEqual(0, len(self.bar.drinks_list))
        self.assertEqual(45.50, self.room_1.wealth_of_the_room)
        self.assertEqual([self.drink_1], self.bar.bar_tab[self.room_1])
        self.assertEqual("We don't have that drink in stock.", result)
