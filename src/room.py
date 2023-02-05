import time

class Room:
    def __init__(self, capacity):
        self.capacity = capacity
        self.guest_list = []
        self.playlist = []
        self.wealth_of_the_room = 0
        self.guest_money = 0

    def add_song_to_playlist(self, song):
        self.playlist.append(song)
    
    def format_playlist_length(self):
        total_length = 0
        for song in self.playlist:
            total_length += song.length
        if total_length >= 3600:
            return time.strftime("%H:%M:%S", time.gmtime(total_length))
        return time.strftime("%M:%S", time.gmtime(total_length))
      
    def play_song(self):
        self.playlist.pop(0)

    def add_guest_to_guest_list(self, guest):
        self.guest_list.append(guest)
        self.wealth_of_the_room += guest.money
        self.guest_money += guest.money

    def remove_guest_from_guest_list(self, guest):
        self.guest_list.remove(guest)