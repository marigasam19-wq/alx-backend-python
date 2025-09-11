#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def stream_users():
    """
    Generator that streams rows from user_data table one by one.
    Uses yield to avoid loading the whole dataset into memory.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sam@4892",
            database="ALX_prodev",
            auth_plugin='mysql_native_password',
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM user_data;")

            for row in cursor:
                yield row

            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error while streaming users: {e}")
        return