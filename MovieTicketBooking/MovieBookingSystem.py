from city import city
from theater import theater
from show import show
from seat import seat
import datetime
from movie_ticket import movieTicket
from Person.user import user

class MovieBookingSystem:
    def __init__(self) -> None:
        self.cities:dict[str,city] = {}
        self.bookings = {}
        self.no_of_bookings = 0
    
    def get_all_shows(self,city_id,movie_id):
        selected_city = self.cities[city_id]
        list_of_shows = []
        for theater_id,theater in selected_city.theaters.items():
            if movie_id in theater.movie_shows:
                list_of_shows.append((theater_id,theater.movie_shows[movie_id]))
                
        return list_of_shows
    
    def make_transaction(self,total_price,user):
        print(f"{user.name} made payment of amount {total_price}")
        self.no_of_bookings+=1
        transaction_id = f"{datetime.datetime.now()}-{self.no_of_bookings}"
        return transaction_id

    def is_available(self,show:show,selected_seats:list[str]):
        for selected_seat_id in selected_seats:
            show_seat = show.show_seats.get(selected_seat_id)
            if not show_seat or not show_seat.available:
                print("seat now available ...",show_seat,show_seat.seat_id)
                return False
        return True
    
    def reserve_seats_and_return_price(self,show:show,selected_seats:list):
        total_price = 0
        for selected_seat_id in selected_seats:
            show_seat:seat = show.show_seats.get(selected_seat_id)
            show_seat.available = False
            total_price+=show_seat.price
        return total_price
    
    def make_booking(self,user:user,show:show,selected_seats:list[seat]):

        if self.is_available(show,selected_seats):
            print("all seats available ......")
            total_price = self.reserve_seats_and_return_price(show,selected_seats)
            transaction_id = self.make_transaction(total_price,user)
            ticket = movieTicket(user,transaction_id, show, selected_seats)
            self.bookings[transaction_id] = ticket
            user.bookings[transaction_id] = ticket
            return ticket
        else:
            raise Exception(f"selected seats not available - kindly retry")



        


    

                

        