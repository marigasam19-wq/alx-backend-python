#!/usr/bin/python3
import psycopg2


class DatabaseConnection:
    """
    Custom class-based context manager for PostgreSQL database connections.
    Automatically opens the connection on __enter__ and closes it on __exit__.
    """

    def __init__(self, db_name, user, password, host="localhost", port=5432):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def __enter__(self):
        self.conn = psycopg2.connect(
            dbname=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()
        return False


if __name__ == "__main__":
    with DatabaseConnection(
        db_name="alx_prodev",
        user="postgres",
        password="48922000", 
        host="localhost",
        port=5432
    ) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_data;")
        results = cursor.fetchall()
        print("Users:", results)
