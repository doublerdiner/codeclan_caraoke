class Reception:
    def __init__(self, till, entry_fee, coat_capacity):
        self.till = till
        self.entry_fee = entry_fee
        self.coat_capacity = coat_capacity
        self.coat_list = []
        self.room_list = []

    def does_room_have_capacity(self, room):
        if room.capacity > len(room.guest_list):
            return True
        else:
            return False
        
    def check_guest_in(self, guest, room):
        if self.does_room_have_capacity(room):
            guest.pay_money(5.00)
            if guest.has_enough_money:
                room.guest_list.append(guest)
                return "Enjoy your night!"
            else:
                return "I'm sorry the entry fee is £5.00."
        else:
            return "I'm sorry. That room is full."
    
    def check_guest_out(self, guest, room):
        room.guest_list.remove(guest)

    def add_coat_to_cloakroom(self, guest):
        if guest.has_coat:
            guest.pay_money(2.00)
            if guest.has_enough_money:
                self.coat_list.append(guest)
                return "Thank you for your coat."
            else:
                return "I'm sorry. The cloakroom is £2.00."
        return "You must be chilly."

    def retrieve_coat_from_cloakroom(self, guest):
        for person in self.coat_list:
            if person.name == guest.name:
                self.coat_list.remove(person)
                return "Here's your coat."
            else:
                return "We don't appear to have a coat for you."

    