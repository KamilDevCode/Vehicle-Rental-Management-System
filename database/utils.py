from database.manager import Session


def create_vehicle_table():
    query = """
        CREATE TABLE IF NOT EXISTS vehicles (
            vehicle_id INTEGER PRIMARY KEY,
            brand TEXT NOT NULL,
            year INTEGER NOT NULL,
            max_speed INTEGER,
            color TEXT,
            status TEXT NOT NULL,
            daily_rate REAL NOT NULL,
            type_of_vehicle TEXT NOT NULL,
            time TEXT NOT NULL
        )
    """
    with Session() as db:
        db.execute_query(query)

    # with Session() as session:
    #     session.execute_query(query)
