#!/usr/bin/python3
import psycopg2
import functools

def with_db_connection(func):
    """Decorator that opens and closes a PostgreSQL DB connection automatically."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="48922000",
            dbname="alx_prodev",
            port=5432
        )
        try:
            result = func(conn, *args, **kwargs) 
            return result
        finally:
            conn.close() 
    return wrapper


@with_db_connection
def get_user_by_id(conn, user_id):
    """Fetch a user by ID from the user_data table."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    return result


if __name__ == "__main__":
    user = get_user_by_id(user_id="37454b44-ae79-4e6f-88d5-1928700e8c0c")
    print("Fetched user:", user)

