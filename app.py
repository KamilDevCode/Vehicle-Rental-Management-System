from database.utils import create_vehicle_table
from models import Menu


def start_app():
    create_vehicle_table()

    menu = Menu()
    menu.run()


if __name__ == "__main__":
    start_app()
