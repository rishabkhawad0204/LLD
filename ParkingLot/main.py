from ParkingGarage import ParkingLot
from enums import ParkingSpotType,VehicleType
from models import Vehicle
from strategies import FirstStop

spot_types_each_floor = {ParkingSpotType.COMPACT: 2,
                      ParkingSpotType.LARGE: 5, ParkingSpotType.SMALL: 10}

pg = ParkingLot(5,spot_types_each_floor)

v1 = Vehicle(VehicleType.COMPACT,"1")
v2 = Vehicle(VehicleType.LARGE,"2")
v3 = Vehicle(VehicleType.COMPACT,"3")
v4 = Vehicle(VehicleType.COMPACT,"4")

ticket1 = pg.create_ticket(v1,FirstStop())
ticket1.print_ticket()

ticket2 = pg.create_ticket(v2,FirstStop())
ticket2.print_ticket()

ticket3 = pg.create_ticket(v3,FirstStop())
ticket3.print_ticket()

pg.exit_car(ticket1)

ticket = pg.create_ticket(v4,FirstStop())
ticket.print_ticket()



