class Bar:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.bar_tab = {}
        self.drinks_list = []
        self.foods_list = []

    def add_drink_to_bar(self, drink):
        self.drinks_list.append(drink)

    def add_food_to_bar(self, food):
        self.foods_list.append(food)
        
    def sell_drink(self, drink, guest, room):
        if guest.has_drink == True:
            return "You already appear to have a drink."
        elif drink not in self.drinks_list:
            return "We don't have that drink in stock."
        elif room not in self.bar_tab:
            self.bar_tab[room] = []        
        if room.wealth_of_the_room > drink.price:
            self.drinks_list.remove(drink)
            guest.has_drink == True
            room.wealth_of_the_room -= drink.price
            self.bar_tab[room].append(drink)
        else: 
            return "You don't appear to be able to buy this drink."

    def sell_food(self, food, guest, room):
        if guest.has_food == True:
            return "You already appear to have food."
        elif food not in self.foods_list:
            return "We don't have that food in stock."
        elif room not in self.bar_tab:
            self.bar_tab[room] = []        
        if room.wealth_of_the_room > food.price:
            self.foods_list.remove(food)
            guest.has_food == True
            room.wealth_of_the_room -= food.price
            self.bar_tab[room].append(food)
        else: 
            return "You don't appear to be able to buy this food."
    
    def settle_bill(self, room):
        total = 0
        for item in self.bar_tab[room]:
            total += item.price
        room.guest_money -= total
        self.till += total
        for person in room.guest_list:
            person.money = round(room.guest_money / len(room.guest_list), 2)
        self.bar_tab.pop(room)