from dataclasses import dataclass
from src.models.vehicle import Vehicle
from datetime import datetime
from enum import Enum


class RentalMode(Enum):
    HOURLY = 1
    DAILY = 2
    WEEKLY = 3
    MONTHLY = 4


@dataclass
class Rental:
    vehicle: Vehicle
    mode: RentalMode
    start_date: datetime
    end_date: datetime
    client_name: str
    client_age: int
    client_valid_driving_license: str

    def __str__(self):
        return (
            f"Vehicle: {self.vehicle.get_details()}\n"
            f"Mode: {self.mode.name}\n"
            f"Start date: {self.start_date.strftime('%Y-%m-%d')}\n"
            f"End date: {self.end_date.strftime('%Y-%m-%d')}\n"
        )
