from show import show
from Person import user
from seat import seat

class movieTicket:
    def __init__(self,user:user,transaction_id:int,show:show,seats:list[seat]) -> None:
        self.user = user
        self.transaction_id = transaction_id
        self.show = show
        self.hall_name = show.hall_name
        self.seats = seats

    def print_ticket(self):
        ticket_str = f"{self.user.name} - {self.show.theater_name} - {self.show.hall_name} - {self.seats}"
        print(ticket_str)

        