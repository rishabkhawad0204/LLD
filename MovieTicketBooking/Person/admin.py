from .person import Iperson
from city import city
from theater import theater
from show import show
from hall import hall
from movie import movie
from MovieBookingSystem import MovieBookingSystem

class admin(Iperson):
    def __init__(self,system:MovieBookingSystem,name,email,id) -> None:
        self.mbs = system
        self.name = name
        self.email = email
        self.id = id

    def get_name(self):
        print(f"name of admin is {self.name}")


    def add_city(self,id,city_name,state_name):
        new_city =  city(id,city_name,state_name)
        self.mbs.cities[new_city.id] = new_city
    
    def add_theatre(self,id,city_id,theatre_name,theatre_coord):
        if city_id not in self.mbs.cities:
             raise Exception(f"given city id - {city_id} doesn't exist")

        new_theatre = theater(id,theatre_name,theatre_coord)
        self.mbs.cities[city_id].theaters[new_theatre.id]= new_theatre

    def add_hall(self,theater_id,city_id,hall_number,rows,cols,premium_rows):
        if city_id not in self.mbs.cities:
            raise Exception(f"given city - {city_id} doesn't exist")
        curr_city = self.mbs.cities[city_id]

        if theater_id not in curr_city.theaters:
            raise Exception(f"given theater - {theater_id} doesn't exist")
        
        curr_theater:theater = curr_city.theaters[theater_id]
        new_hall = hall(hall_number,rows,cols,premium_rows)
        curr_theater.halls[new_hall.hall_number] = new_hall

    
    def add_show(self,show_id,movie_id,start_time,theater_id,city_id,hall_number,premium_price,normal_price):

        if city_id not in self.mbs.cities:
            raise Exception(f"given city - {city_id} doesn't exist")
        curr_city = self.mbs.cities[city_id]

        if theater_id not in curr_city.theaters:
            raise Exception(f"given theater - {theater_id} doesn't exist")
        
        curr_theater:theater = curr_city.theaters[theater_id]

        if hall_number not in curr_theater.halls:
            raise Exception(f"given hall - {hall_number} doesn't exist in theatre - {theater_id}")
        
        curr_hall:hall = curr_theater.halls[hall_number]

        new_show = show(show_id,start_time,movie,curr_theater.name,curr_hall.hall_number,premium_price,normal_price)
        new_show.add_seats_for_show(curr_hall)

        if movie_id not in curr_theater.movie_shows:
            curr_theater.movie_shows[movie_id] = []

        curr_theater.movie_shows[movie_id].append(new_show)


    


        

            

