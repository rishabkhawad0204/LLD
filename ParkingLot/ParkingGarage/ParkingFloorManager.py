from .ParkingSpot import *
from strategies import ParkingStrategy
from models import ticket,Vehicle
import datetime

class ParkingFloorManager:
    def __init__(self,spots:list[ParkingSpot]) -> None:
        self.spots = spots

    def find_parking_spot(self,vehicle:Vehicle,parking_strategy:ParkingStrategy):

        return parking_strategy.find_spot(self.spots,vehicle)

    def reserve_parking_spot(self,spot:ParkingSpot,vehicle) -> ticket:
        spot.is_available = False
        return ticket(datetime.datetime.now(),vehicle,spot)
    
    def free_parking_spot(self,spot:ParkingSpot):
        spot.is_available = True

