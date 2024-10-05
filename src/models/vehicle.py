from dataclasses import dataclass
from enum import Enum


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
    model: str
    year: int
    color: str
    status: VehicleStatus
    daily_rate: float
    type_of_vehicle: TypeOfVehicle

    def get_details(self):
        return {
            "id": self.vehicle_id,
            "type": self.type_of_vehicle.value,
            "model": self.model,
            "year": self.year,
            "color": self.color,
            "status": self.status.value,
            "daily_rate": self.daily_rate,
        }

    def __str__(self):
        return f"{self.get_details()}"


vehicle = Vehicle(
    vehicle_id=1,
    max_speed=200,
    model="BMW",
    year=2020,
    status=VehicleStatus.RESERVED,
    color="red",
    daily_rate=100.0,
    type_of_vehicle=TypeOfVehicle.CAR,
)
print(vehicle)


@dataclass
class Motorbike(Vehicle):
    engine_capacity: int

    def __str__(self):
        return f"{super().__str__()} -Engine capacity: {self.engine_capacity}cc"


motorbike = Motorbike(
    vehicle_id=2,
    max_speed=180,
    model="Yamaha",
    year=2021,
    color="blue",
    status=VehicleStatus.UNAVAILABLE,
    daily_rate=50.0,
    engine_capacity=1000,
    type_of_vehicle=TypeOfVehicle.MOTORBIKE,
)

print(motorbike)


@dataclass
class Truck(Vehicle):
    carrying_capacity: int

    def __str__(self):
        return f"{super().__str__()} - Carrying capacity: {self.carrying_capacity}kg"


truck = Truck(
    vehicle_id=3,
    max_speed=250,
    model="Scania",
    year=2022,
    color="green",
    status=VehicleStatus.RESERVED,
    daily_rate=150.0,
    carrying_capacity=2000,
    type_of_vehicle=TypeOfVehicle.TRUCK,
)

print(truck)
