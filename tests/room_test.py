import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room(6)
        self.room_2 = Room(2)
        self.guest_1 = Guest("David Byrne", 50.00, "Psycho Killer", True)
        self.guest_2 = Guest("Thom Yorke", 10.00, "Karma Police", False)
        self.song_1 = Song("Girl U Want", "Devo", 177, "New Wave")
        self.song_2 = Song("Psycho Killer", "Talking Heads", 261, "New Wave")

# Test 1 - Room has a capacity
    def test_room_capacity(self):
        self.assertEqual(6, self.room_1.capacity)
    
# Test 2 & 3 - Room has an empty guest_list and playlist
    def test_guest_list_empty(self):
        self.assertEqual(0, len(self.room_1.guest_list))

    def test_playlist_empty(self):
        self.assertEqual(0, len(self.room_1.playlist))