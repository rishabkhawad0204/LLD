from .ParkingStrategy import ParkingStrategy
from ParkingGarage import ParkingSpot
from models import Vehicle

class FirstStop(ParkingStrategy):
    
    def find_spot(self, spots: list[ParkingSpot], vehicle:Vehicle):
        for spot in spots:
            if spot.is_available and spot.type.value==vehicle.type_of_vehicle.value:
                return spot
        return None