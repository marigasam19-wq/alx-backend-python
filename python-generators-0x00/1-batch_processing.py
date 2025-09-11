#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

print("Importing batch processing module...")
def stream_users_in_batches(batch_size):
    print("Batch size:", batch_size)
    """
    Generator that streams rows from user_data in batches.
    Yields lists of rows (each of length <= batch_size).
    """
    try:
        print("Trying to connect to MySQL server...")
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sam@4892",
            database="ALX_prodev",
            port=3306,
            auth_plugin='mysql_native_password',
        )
        print("Connection object:", connection)

        if connection.is_connected():
            print("Successfully connected to MySQL server")
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM user_data;")

            while True:
                batch = cursor.fetchmany(batch_size)
                if not batch:
                    break
                yield batch

            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error while streaming batches: {e}")
        return


def batch_processing(batch_size):
    """
    Processes each batch to filter users with age > 25.
    Uses the batch generator.
    """
    for batch in stream_users_in_batches(batch_size):
        print("Processing new batch of size:", len(batch))
        filtered = [user for user in batch if int(user["age"]) > 25]
        yield filtered
