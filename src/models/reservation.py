from dataclasses import dataclass
from datetime import datetime
from src.models import Vehicle


@dataclass
class Reservation:
    vehicle: Vehicle
    start_date: datetime
    end_date: datetime
    client_name: str
    client_age: int
    client_valid_driving_license: str

    def __str__(self):
        return (
            f"Vehicle: {self.vehicle.model}\n"
            f"Client: {self.client_name} (Age: {self.client_age})\n"
            f"License: {self.client_valid_driving_license}\n"
            f"Reservation Period: {self.start_date.strftime('%Y-%m-%d')} to {self.end_date.strftime('%Y-%m-%d')}"
        )
