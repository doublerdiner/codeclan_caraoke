class Reception:
    def __init__(self, till, entry_fee, coat_capacity):
        self.till = till
        self.entry_fee = entry_fee
        self.coat_capacity = coat_capacity
        self.coat_list = []
        self.room_list = []

    def does_room_have_capacity(self, room):
        pass

    def check_guest_in(self, guest, room):
        pass
    
    def check_guest_out(self, guest, room):
        pass

    def add_coat_to_cloakroom(self, guest):
        pass

    def retrieve_coat_from_cloakroom(self, guest):
        pass
    