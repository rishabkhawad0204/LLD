from abc import ABC, abstractmethod

class ParkingStrategy(ABC):
    @abstractmethod
    def find_spot(self,spots:list,vehicle_type):
        pass