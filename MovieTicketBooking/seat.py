
class seat:
    def __init__(self,seat_id,price) -> None:

        self.seat_id = seat_id
        self.available = True
        self.price = price
    

    def free_seat(self):
        self.available = True

    
    def reserve_seat(self):
        self.available = False
        