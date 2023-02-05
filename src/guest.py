class Guest:
    def __init__(self, name, money, favourite_song, has_coat):
        self.name = name
        self.money = money
        self.favourite_song = favourite_song
        self.has_coat = has_coat
        self.has_drink = False
        self.has_food = False
        self.has_enough_money = True

    def order_drink(self, drink, bar):
        pass

    def order_food(self, food, bar):
        pass
 
    def eat_and_drink(self):
        self.has_drink = False
        self.has_food = False

    def hears_favourite_song(self, song):
        pass
    
    def pay_money(self, amount):
        self.has_enough_money = True
        if amount > self.money:
            self.has_enough_money = False
            return "Not enough money to pay"
        else:
            self.money -= amount