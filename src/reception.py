class Reception:
    def __init__(self, till, entry_fee, coat_capacity):
        self.till = till
        self.entry_fee = entry_fee
        self.coat_capacity = coat_capacity
        self.coat_list = []
  
    def does_room_have_capacity(self, room):
        if room.capacity > len(room.guest_list):
            return True
        else:
            return False
        
    def check_guest_in(self, guest, room):
        if self.does_room_have_capacity(room):
            guest.pay_money(self.entry_fee)
            if guest.has_enough_money:
                self.till += self.entry_fee
                room.add_guest_to_guest_list(guest)
                return "Enjoy your night!"
            else:
                return f"I'm sorry the entry fee is £{self.entry_fee:.2f}."
        else:
            return "I'm sorry. That room is full."
    
    def check_guest_out(self, guest, room, bar):
        if room in bar.bar_tab:
            return "I'm sorry. You can't leave until you've settled your bar tab."
        room.remove_guest_from_guest_list(guest)
        room.wealth_of_the_room = 0
        room.guest_money = 0

    def add_coat_to_cloakroom(self, guest):
        if len(self.coat_list) == self.coat_capacity:
            return "I'm sorry the cloakroom is full."
        elif guest.has_coat:
            guest.pay_money(2.00)
            if guest.has_enough_money:
                guest.has_coat = False
                self.coat_list.append(guest.name)
                return "Thank you for your coat."
            else:
                return "I'm sorry. The cloakroom is £2.00."
        return "You must be chilly."

    def retrieve_coat_from_cloakroom(self, guest):
        for person in self.coat_list:
            if person == guest.name:
                self.coat_list.remove(person)
                guest.has_coat = True
                return "Here's your coat."
            else:
                return "We don't appear to have a coat for you."

    