from datetime import datetime
from src.models.vehicle import Vehicle, VehicleStatus
from src.models.rental import RentalMode
from src.models.vehicle_database import VehicleDatabase


class RentalService:
    @staticmethod
    def check_vehicle_validity():
        vehicle_id = int(input("Enter vehicle ID to rent: "))
        vehicle = VehicleDatabase().get_vehicle_by_id(vehicle_id)
        if vehicle and vehicle.status == VehicleStatus.AVAILABLE:
            return vehicle
        print("Vehicle not available or invalid.")
        return None

    @staticmethod
    def check_user_age():
        age = int(input("Enter your age: "))
        if age >= 18:
            return age
        else:
            print("You must be at least 18 years old to rent a vehicle.")
            return None

    @staticmethod
    def check_user_driving_license():
        license_valid = input("Do you have a valid driving license? (yes/no): ")
        if license_valid.lower() == "yes":
            return "valid"
        else:
            print("You cannot rent a vehicle without a valid driving license.")
            return None

    @staticmethod
    def choose_rental_mode():
        print("Choose rental mode:")
        print("1. Hourly")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly")
        choice = int(input("Enter choice (1-4): "))
        return RentalMode(choice)

    @staticmethod
    def calculate_price(rental):
        days = (rental.end_date - rental.start_date).days
        price_calculation = {
            RentalMode.HOURLY: lambda: rental.vehicle.daily_rate * days * 0.2,
            RentalMode.DAILY: lambda: rental.vehicle.daily_rate * days,
            RentalMode.WEEKLY: lambda: rental.vehicle.daily_rate * (days / 7) * 5,
            RentalMode.MONTHLY: lambda: rental.vehicle.daily_rate * (days / 30) * 20,
        }
        return price_calculation.get(rental.mode, lambda: 0)()

    @staticmethod
    def make_reservation(
        vehicle: Vehicle, start_date: datetime, end_date: datetime, client_name: str
    ):
        if vehicle.status == VehicleStatus.AVAILABLE:
            vehicle.update_status(VehicleStatus.RESERVED)
            return vehicle
        return None
