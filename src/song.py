class Song:
    def __init__(self, name, artist, length, genre):
        self.name = name
        self.artist = artist
        self.length = length
        self.genre = genre

    def format_song_length(self):
        minutes = self.length // 60
        seconds = self.length % 60
        return f"{minutes}:{seconds}"