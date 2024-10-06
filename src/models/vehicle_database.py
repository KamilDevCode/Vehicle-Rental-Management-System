from src.models.vehicle import Vehicle, VehicleStatus, TypeOfVehicle


class VehicleDatabase:
    def __init__(self):
        self.vehicles = [
            Vehicle(
                vehicle_id=1,
                max_speed=180,
                model="BMW",
                year=2020,
                color="Red",
                status=VehicleStatus.AVAILABLE,
                daily_rate=100,
                type_of_vehicle=TypeOfVehicle.CAR,
            ),
            Vehicle(
                vehicle_id=2,
                max_speed=250,
                model="Scania",
                year=2022,
                color="Green",
                status=VehicleStatus.AVAILABLE,
                daily_rate=150,
                type_of_vehicle=TypeOfVehicle.TRUCK,
            ),
            Vehicle(
                vehicle_id=3,
                max_speed=200,
                model="Yamaha",
                year=2021,
                color="Blue",
                status=VehicleStatus.AVAILABLE,
                daily_rate=50,
                type_of_vehicle=TypeOfVehicle.MOTORBIKE,
            ),
        ]

    def get_vehicle_by_id(self, vehicle_id: int):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
