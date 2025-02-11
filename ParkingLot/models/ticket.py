from ParkingGarage import ParkingSpot
from models.vehicle import Vehicle

class ticket:
    def __init__(self,time,vehicle:Vehicle,spot:ParkingSpot) -> None:
        self.entry_time = time
        self.spot_id = spot
        self.vehicle = vehicle
    
    def print_ticket(self):
        print(f"ticket details : {self.vehicle.id} assigned {self.spot_id.id}")
    
    