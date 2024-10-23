import sqlite3

DATABASE_NAME = "database.sql"


class Session:
    """
    Wykorzystanie Contex Managera
    """

    def __init__(self, database_name=DATABASE_NAME):
        self.database_name = database_name
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Zakończenie połączenia, niezależnie od tego, czy wystąpił wyjątek
        if isinstance(exc_val, Exception):
            self.connection.rollback()
            print(f"Błąd: {exc_val}")
        else:
            self.connection.commit()

        self.connection.close()

    # def execute_query(self, query):
    #     self.cursor.execute(query)
    #     self.connection.commit()
    #
    # def fetch_all_data(self, query):
    #     self.cursor.execute(query)
    #     return self.cursor.fetchall()
