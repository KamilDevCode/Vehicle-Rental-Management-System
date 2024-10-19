from dataclasses import dataclass, asdict
from enum import Enum
from datetime import datetime


class TypeOfVehicle(Enum):
    ID = "id: 1 - car, 2 - truck, 3 - motorbike"
    CAR = "car"
    TRUCK = "truck"
    MOTORBIKE = "motorbike"


class VehicleStatus(Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    RESERVED = "reserved"


@dataclass
class Vehicle:
    vehicle_id: int
    max_speed: int
    brand: str
    year: int
    color: str
    status: VehicleStatus
    daily_rate: float
    type_of_vehicle: TypeOfVehicle | str
    time: datetime = datetime.now()

    def get_details(self):

        return {
            "id": self.vehicle_id,
            "type": self.type_of_vehicle,
            "brand": self.brand,
            "year": self.year,
            "color": self.color,
            "status": self.status,
            "daily_rate": self.daily_rate,
            "time": self.time.strftime("%Y-%m-%d %H:%M:%S"),
        }

    def __str__(self):
        return f"{self.get_details()}"

    # @classmethod
    # def get_all_vehicles(cls):
    #     return [
    #         cls.get_vehicle_by_id(1),
    #         cls.get_vehicle_by_id(2),
    #         cls.get_vehicle_by_id(3),
    #     ]

    def update_status(self, new_status: VehicleStatus):
        self.status = new_status

    def to_dict(self):
        data = asdict(self)
        data["status"] = self.status.value
        data["type_of_vehicle"] = self.type_of_vehicle.value
        data["time"] = self.time.strftime("%Y-%m-%d %H:%M:%S")
        return data

    @classmethod
    def from_dict(cls, data):
        # Dodaj "time" do argumentów przekazywanych do klasy
        data["time"] = datetime.strptime(data["time"], "%Y-%m-%d %H:%M:%S")
        data["status"] = VehicleStatus[data["status"].upper()]
        return cls(**data)


@dataclass
class Motorbike(Vehicle):
    engine_capacity: int = 0

    def __str__(self):
        return f"{super().__str__()} Engine capacity: {self.engine_capacity}cc"


@dataclass
class Truck(Vehicle):
    carrying_capacity: int = 0

    def __str__(self):
        return f"{super().__str__()} Carrying capacity: {self.carrying_capacity}kg"
