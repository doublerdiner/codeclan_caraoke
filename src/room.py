class Room:
    def __init__(self, capacity):
        self.capacity = capacity
        self.guest_list = []
        self.playlist = []

    def add_song_to_playlist(self, song):
        self.playlist.append(song)
    
    def format_playlist_length(self):
        total_length = 0
        for song in self.playlist:
            total_length += song.length
        hours = total_length // 3600
        minutes = (total_length % 3600) // 60
        seconds = ((total_length % 3600) % 60) % 60
        if hours == 0:
            return f"{minutes}:{seconds}"
        else:
            return f"{hours}:{minutes}:{seconds}"

    
    def wealth_of_the_room(self):
        total = 0
        for person in self.guest_list:
            total += person.money
        return total
    
    def play_song(self):
        self.playlist.pop(0)