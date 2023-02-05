class Guest:
    def __init__(self, name, money, favourite_song, has_coat):
        self.name = name
        self.money = money
        self.favourite_song = favourite_song
        self.has_coat = has_coat
        self.has_drink = False
        self.has_food = False
        self.has_enough_money = True

    def eat_and_drink(self):
        self.has_drink = False
        self.has_food = False

    def favourite_song_in_playlist(self, room):
        for song in room.playlist:
            if song.name == self.favourite_song:
                return "I can't belive this song is in the playlist. I love this song!"
    
    def pay_money(self, amount):
        self.has_enough_money = True
        if amount > self.money:
            self.has_enough_money = False
            return "Not enough money to pay"
        else:
            self.money -= amount