from hall import hall
from seat import seat
from enums import SeatType

class show:
    def __init__(self,show_id,start_time,movie,theater_name,hall_name,premium_price,normal_price) -> None:
        self.id = show_id
        self.start_time = start_time
        self.movie = movie
        self.theater_name = theater_name
        self.hall_name = hall_name
        self.premium_price = premium_price
        self.normal_price = normal_price
        self.show_seats = {}


    def add_seats_for_show(self,hall:hall):
        cnt = 1
        for row in range(hall.rows):
            for col in range(hall.cols):
                seat_id = f"{row}-{col}"
                seat_type = SeatType.Premium if row <= 2 else SeatType.Regular
                price = self.premium_price if seat_type == SeatType.Premium else self.normal_price
                new_seat = seat(seat_id, price)
                self.show_seats[seat_id] = new_seat


        