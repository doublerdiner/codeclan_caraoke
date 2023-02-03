class Song:
    def __init__(self, name, artist, length, genre):
        self.name = name
        self.artist = artist
        self.length = length
        self.genre = genre

    def format_song_length(self):
        minute = self.length // 60
        second = self.length % 60
        return f"{minute}:{second}"