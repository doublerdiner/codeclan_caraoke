import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room(6)
        self.room_2 = Room(1)
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

# Test 4 - Song can be added to playlist
    def test_song_can_be_added_to_playlist(self):
        self.room_1.add_song_to_playlist(self.song_1)
        self.assertEqual(1, len(self.room_1.playlist))
        self.assertEqual(self.song_1, self.room_1.playlist[0])

# Test 5 - The playlist length can be formatted to hh:mm:ss
    def test_format_playlist_length_HHMMSS(self):
        self.song_2.length = 12345
        self.room_1.add_song_to_playlist(self.song_1)
        self.room_1.add_song_to_playlist(self.song_2)
        result = self.room_1.format_playlist_length()
        self.assertEqual("03:28:42", result)

    
# Test 6 - The playlist length can be formatted to mm:ss
    def test_format_playlist_length(self):
        self.room_1.add_song_to_playlist(self.song_1)
        self.room_1.add_song_to_playlist(self.song_2)
        result = self.room_1.format_playlist_length()
        self.assertEqual(2, len(self.room_1.playlist))
        self.assertEqual("07:18", result)

# Test 7 - Check the wealth of the room
    def test_wealth_of_the_room(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.room_1.add_guest_to_guest_list(self.guest_2)
        result = self.room_1.wealth_of_the_room
        self.assertEqual(result, 60)

# Test 8 - Play a song
    def test_play_song(self):
        self.room_1.add_song_to_playlist(self.song_1)
        self.room_1.add_song_to_playlist(self.song_2)
        self.room_1.play_song()
        self.assertEqual(1, len(self.room_1.playlist))
        self.assertEqual(self.song_2, self.room_1.playlist[0])

# Test 9 - Add guest to room
    def test_add_guest_to_guest_list(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.room_1.add_guest_to_guest_list(self.guest_2)
        self.assertEqual(2, len(self.room_1.guest_list))

# Test 10 - Remove guest from room
    def test_remove_guest_from_guest_list(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.room_1.add_guest_to_guest_list(self.guest_2)
        self.room_1.remove_guest_from_guest_list(self.guest_1)
        self.assertEqual(1, len(self.room_1.guest_list))
        self.assertEqual(self.guest_2, self.room_1.guest_list[0])
