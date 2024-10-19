import json
from src.models.vehicle import Vehicle, VehicleStatus, TypeOfVehicle


class VehicleDatabase:
    def __init__(self):
        self.vehicles = [
            Vehicle(
                vehicle_id=1,
                max_speed=180,
                brand="BMW",
                year=2020,
                color="Red",
                status=VehicleStatus.AVAILABLE,
                daily_rate=100,
                type_of_vehicle=TypeOfVehicle.CAR,
            ),
            Vehicle(
                vehicle_id=2,
                max_speed=250,
                brand="Scania",
                year=2022,
                color="Green",
                status=VehicleStatus.AVAILABLE,
                daily_rate=150,
                type_of_vehicle=TypeOfVehicle.TRUCK,
            ),
            Vehicle(
                vehicle_id=3,
                max_speed=200,
                brand="Yamaha",
                year=2021,
                color="Blue",
                status=VehicleStatus.AVAILABLE,
                daily_rate=50,
                type_of_vehicle=TypeOfVehicle.MOTORBIKE,
            ),
        ]

    @staticmethod
    def get_vehicle_by_id(vehicle_id: int):
        json_data = json.load(open("vehicle_database.json"))
        for vehicle in json_data:
            if vehicle["vehicle_id"] == vehicle_id:
                return Vehicle.from_dict(vehicle)

    # @staticmethod
    # def get_vehicle_by_id(vehicle_id: int):
    #     # Wczytanie danych z pliku
    #     json_data = JSONManager.load_from_json("vehicle_database.json")
    #     for vehicle in json_data:
    #         if vehicle.vehicle_id == vehicle_id:
    #             return vehicle
    #     return None

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
        return vehicle
