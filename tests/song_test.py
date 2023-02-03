import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Girl U Want", "Devo", 177, "New Wave")
        self.song_2 = Song("Psycho Killer", "Talking Heads", 261, "New Wave")

# Test 1 - 4 - Song has an name, artist, length and genre
    def test_song_has_name(self):
        self.assertEqual("Girl U Want", self.song_1.name)

    def test_song_has_artist(self):
        self.assertEqual("Devo", self.song_1.artist)

    def test_song_has_length(self):
        self.assertEqual(177, self.song_1.length)

    def test_song_has_genre(self):
        self.assertEqual("New Wave", self.song_1.genre)

# Test 5 - Get the song length in 00:00 format
    def test_format_song_length(self):
        self.assertEqual("2:57", self.song_1.format_song_length())
