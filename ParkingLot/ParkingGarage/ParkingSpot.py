from enums import ParkingSpotType

class ParkingSpot:
    def __init__(self,spot_type:ParkingSpotType,id:int) -> None:
        self.is_available = True
        self.type = spot_type
        self.id = id
        
