#!/usr/bin/python3
import psycopg2
import psycopg2.extras

def stream_users():
    """
    Generator that streams rows from user_data table one by one.
    Uses yield to avoid loading the whole dataset into memory.
    """
    try:
        connection = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="48922000", 
            dbname="alx_prodev",
            port=5432,
        )

        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM user_data;")

        for row in cursor:
            yield dict(row) 

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error while streaming users: {e}")
        return
