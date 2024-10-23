from models.vehicles import Vehicle
import json


class JSONManager:

    # def __init__(self):
    #     self.vehicle_db = VehicleDatabase()

    @staticmethod
    def save_to_json(data: list, filename: str):
        with open(filename, "w") as file:
            serialized_data = [vehicle.to_dict() for vehicle in data]
            json.dump(serialized_data, file, indent=4, ensure_ascii=False)
            print("Data saved successfully to JSON")

    @staticmethod
    def load_from_json(filename: str) -> list:
        with open(filename, "r") as file:
            serialized_data = json.load(file)
            return [Vehicle.from_dict(vehicle) for vehicle in serialized_data]
