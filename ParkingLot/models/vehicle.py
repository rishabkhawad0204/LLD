from enums import VehicleType

class Vehicle:
    def __init__(self,vehicle_type: VehicleType, numberPlate:str) -> None:
        
        self.type_of_vehicle = vehicle_type
        self.id = numberPlate
    
    def getType(self):
        return self.type_of_vehicle



