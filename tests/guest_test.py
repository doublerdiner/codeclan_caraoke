import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("David Byrne", 50.00, "Psycho Killer", True)
        self.guest_2 = Guest("Thom Yorke", 10.00, "Karma Police", False)
        self.room_1 = Room(6)
        self.room_2 = Room(1)
        self.song_1 = Song("Girl U Want", "Devo", 177, "New Wave")
        self.song_2 = Song("Psycho Killer", "Talking Heads", 261, "New Wave")

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
    
# Test 6 - Guest can spend money
    def test_guest_can_spend_money(self):
        self.guest_1.pay_money(2)
        self.assertEqual(48, self.guest_1.money)
    
# Test 7 - Guest doesn't have enough money
    def test_guest_does_not_have_enough_money(self):
        result = self.guest_2.pay_money(12)
        self.assertEqual(10, self.guest_2.money)
        self.assertEqual("Not enough money to pay", result)
    
# Test 8 - Guest can eat & drink
    def test_guest_can_eat_and_drink(self):
        self.guest_1.has_food = True
        self.guest_1.has_drink = True
        self.guest_1.eat_and_drink()
        self.assertEqual(False, self.guest_1.has_food)
        self.assertEqual(False, self.guest_1.has_drink)

# Test 9 - Guest sees their favourite song in the playlist
    def test_favourite_song_in_playlist(self):
        self.room_1.add_song_to_playlist(self.song_2)
        result = self.guest_1.favourite_song_in_playlist(self.room_1)
        self.assertEqual("I can't belive this song is in the playlist. I love this song!", result)

# Test 10 - The guest's favourite song is not on the playlist
    def test_favourite_song_in_playlist__None(self):
        self.room_1.add_song_to_playlist(self.song_1)
        self.room_1.add_song_to_playlist(self.song_2)
        result = self.guest_2.favourite_song_in_playlist(self.room_1)
        self.assertEqual(None, result)
