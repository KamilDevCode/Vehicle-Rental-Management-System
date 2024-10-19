from datetime import datetime
from src.models.vehicle import Vehicle, VehicleStatus
from src.models.rental import RentalMode
from src.models.json_operations import JSONManager


class RentalService:
    @staticmethod
    def check_vehicle_validity():
        vehicle_id = int(input("Enter vehicle ID: "))
        vehicle = JSONManager().load_from_json("vehicle_database.json")
        for v in vehicle:
            if v.vehicle_id == vehicle_id:
                return v
        else:
            print("Vehicle not found.")

    @staticmethod
    def check_user_age() -> int | str:
        age = int(input("Enter your age: "))
        return (
            age
            if age >= 18
            else print("You must be at least 18 years old to rent a vehicle.")
        )

    @staticmethod
    def check_user_driving_license() -> bool:
        licence_expiry_date = input(
            "Enter your driving license expiry date (YYYY-MM-DD): "
        )
        expiry_date = datetime.strptime(licence_expiry_date, "%Y-%m-%d")
        if expiry_date > datetime.now():
            return True
        else:
            print("Your driving license has expired. Please renew it.")
            return False

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
    def calculate_price(rental) -> float:
        days = (rental.end_date - rental.start_date).days
        price_calculation = {
            RentalMode.HOURLY: lambda: rental.vehicle.daily_rate * days * 0.2,
            RentalMode.DAILY: lambda: rental.vehicle.daily_rate * days,
            RentalMode.WEEKLY: lambda: rental.vehicle.daily_rate * (days / 7) * 5,
            RentalMode.MONTHLY: lambda: rental.vehicle.daily_rate * (days / 30) * 20,
        }
        return price_calculation.get(rental.mode, lambda: 0)()

    @staticmethod
    def make_reservation(rental):
        rental.vehicle.update_status(VehicleStatus.RESERVED)
        print(
            f"Vehicle {rental.vehicle.vehicle_id} reserved for {rental.end_date - rental.start_date} days."
        )
