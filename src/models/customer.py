from datetime import datetime
from src.models.rental import Rental
from src.models.vehicle import VehicleStatus, Vehicle, TypeOfVehicle
from src.models.vehicle_database import VehicleDatabase
from src.services.rental_service import RentalService
from src.models.json_operations import JSONManager


class Menu:
    def __init__(self):
        self.__is_running = True
        self.vehicle_db = VehicleDatabase()
        self.options = {
            "1": self.add_vehicle,
            "2": self.rent_vehicle,
            "3": self.return_vehicle,
            "4": self.show_all_vehicles,
            "5": self.show_available_vehicles,
            "6": self.show_reserved_vehicles,
            "7": self.show_unavailable_vehicles,
            "8": self.exit,
        }
        self.file_manager = JSONManager()

    def run(self):
        while self.__is_running:
            self.show_menu()
            self.get_and_execute_option()

    @staticmethod
    def show_menu():
        print("=== Welcome to the Car Rental Service! ===")
        print("1. Add vehicle")
        print("2. Rent a vehicle")
        print("3. Return a vehicle")
        print("4. Show all vehicles")
        print("5. Show available vehicles")
        print("6. Show reserved vehicles")
        print("7. Show unavailable vehicles")
        print("8. Exit")

    def get_and_execute_option(self):
        option = input("Enter your option: ")
        self.options.get(option, self.show_error)()

    def add_vehicle(self):
        print("=== Add New Vehicle ===")
        brand = input("Enter vehicle model: ")
        year = int(input("Enter vehicle year: "))
        vehicle_id = int(input("Enter vehicle ID: "))
        max_speed = int(input("Enter max speed: "))
        color = input("Enter vehicle color: ")
        daily_rate = int(input("Enter daily rate: "))
        print("selected type of vehicle: \n1.Car\n2.Truck\n3.Motorbike")

        type_choice = input("Enter your choice: ")

        vehicle_type = {
            "1": TypeOfVehicle.CAR,
            "2": TypeOfVehicle.TRUCK,
            "3": TypeOfVehicle.MOTORBIKE,
        }.get(type_choice, "Invalid vehicle type")

        self.file_manager.save_to_json(
            self.vehicle_db.vehicles, "vehicle_database.json"
        )

        if not vehicle_type:
            print("Invalid vehicle type.")
            return

        new_vehicle = Vehicle(
            brand=brand,
            year=year,
            vehicle_id=vehicle_id,
            status=VehicleStatus.AVAILABLE,
            max_speed=max_speed,
            color=color,
            daily_rate=daily_rate,
            type_of_vehicle=vehicle_type,
        )

        self.vehicle_db.add_vehicle(new_vehicle)
        print(f"Vehicle {brand} added successfully.")
        self.file_manager.save_to_json(
            self.vehicle_db.vehicles, "vehicle_database.json"
        )

    def rent_vehicle(self):

        vehicle = RentalService.check_vehicle_validity()
        if not vehicle:
            print("Invalid vehicle selected.")
            return

        client_name = input("Enter client name: ")
        client_age = RentalService.check_user_age()
        if not client_age:
            print("Invalid age. You must be at least 18 years old to rent a vehicle.")
            return

        client_valid_driving_license = RentalService.check_user_driving_license()
        if not client_valid_driving_license:
            print("Invalid driving license. Exiting...")
            return

        mode = RentalService.choose_rental_mode()

        start_date_str = input("Enter start date (YYYY-MM-DD): ")
        end_date_str = input("Enter end date (YYYY-MM-DD): ")

        try:

            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Exiting...")
            return
        if vehicle and vehicle.status == VehicleStatus.AVAILABLE:
            vehicle.update_status(VehicleStatus.RESERVED)

            rental = Rental(
                vehicle=vehicle,
                mode=mode,
                start_date=start_date,
                end_date=end_date,
                client_name=client_name,
                client_age=client_age,
                client_valid_driving_license=client_valid_driving_license,
            )

            total_price = RentalService.calculate_price(rental)
            print(
                f"Vehicle {vehicle} rented. Total price: {total_price:.2f} PLN. Enjoy your ride!"
            )

            print("\nRental Summary:")
            print(f"Client Name: {client_name}")
            print(f"Vehicle: {vehicle}")
            print(f"Rental Mode: {mode.name}")
            print(f"Start Date: {start_date_str}")
            print(f"End Date: {end_date_str}")
            print(f"Total Price for the Rental: {total_price:.2f}")

            return rental
        else:
            print(f"Vehicle: {vehicle} is not available.")

    def make_reservation(self):
        vehicle_id = int(input("Enter vehicle ID to make reservation: "))
        vehicle = self.vehicle_db.get_vehicle_by_id(vehicle_id)
        if vehicle and vehicle.status == VehicleStatus.AVAILABLE:
            vehicle.update_status(VehicleStatus.RESERVED)
            print(f"Vehicle {vehicle_id} reserved.")
            self.file_manager.save_to_json(
                self.vehicle_db.vehicles, "vehicle_database.json"
            )
        else:
            print(f"Vehicle with ID {vehicle_id} is not available or not found.")

    def return_vehicle(self):
        vehicle_id = int(input("Enter vehicle ID to return: "))
        vehicle = self.vehicle_db.get_vehicle_by_id(vehicle_id)
        if vehicle and vehicle.status == VehicleStatus.RESERVED:
            vehicle.update_status(VehicleStatus.AVAILABLE)
            print(f"Vehicle {vehicle_id} returned.")
            self.file_manager.save_to_json(
                self.vehicle_db.vehicles, "vehicle_database.json"
            )
        else:
            print(f"Vehicle with ID {vehicle_id} is not reserved or not found.")

    def show_all_vehicles(self):

        loaded_data = self.file_manager.load_from_json("vehicle_database.json")

        for vehicle in loaded_data:
            print(vehicle)

    def show_available_vehicles(self):
        for vehicle in self.vehicle_db.vehicles:
            if vehicle.status == VehicleStatus.AVAILABLE:
                print(vehicle)

    def show_reserved_vehicles(self):
        for vehicle in self.file_manager.load_from_json("vehicle_database.json"):
            if vehicle.status == VehicleStatus.RESERVED:
                print(vehicle)

    def show_unavailable_vehicles(self):
        for vehicle in self.file_manager.load_from_json("vehicle_database.json"):
            if vehicle.status == VehicleStatus.UNAVAILABLE:
                print(vehicle)

    @staticmethod
    def show_error():
        print("Invalid option. Please try again.")

    def exit(self):
        self.__is_running = False
        print("Goodbye! Thank you for using our rental service.")
