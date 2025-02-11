from ParkingGarage import ParkingFloorManager, ParkingSpot
from strategies import ParkingStrategy
from models import Vehicle, ticket
from enums import ParkingSpotType, VehicleType


class ParkingLot:
    def __init__(self, no_of_floors: int, spot_types_each_floor: dict):
        self.floors: int = no_of_floors
        self.floor_managers: list[ParkingFloorManager] = []
        self.spot_id: int = 1
        self.add_floor_managers(spot_types_each_floor)

    def add_floor_managers(self, spot_types_each_floor):
        for _ in range(self.floors):
            parking_spots = []
            for spot_type, count in spot_types_each_floor.items():
                for _ in range(count):
                    parking_spots.append(ParkingSpot(spot_type, self.spot_id))
                    self.spot_id += 1

            self.floor_managers.append(ParkingFloorManager(parking_spots))

    def create_ticket(self, vehicle: Vehicle, parking_strategy: ParkingStrategy):
        tkt = None
        for mgr in self.floor_managers:
            poss_spot = mgr.find_parking_spot(vehicle, parking_strategy)
            if poss_spot:
                tkt = mgr.reserve_parking_spot(poss_spot,vehicle)
                return tkt

        raise ValueError(f"No valid spot available for {vehicle}")
    
    def exit_car(self,ticket:ticket):
        print(f"{ticket.vehicle.id} exiting now")
        ticket.spot_id.is_available=True
