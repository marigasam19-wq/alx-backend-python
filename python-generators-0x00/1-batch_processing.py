#!/usr/bin/python3
import psycopg2
import psycopg2.extras

def stream_users_in_batches(batch_size):
    """
    Generator that streams rows from user_data in batches.
    Yields lists of rows (each of length <= batch_size).
    """
    try:
        print("Trying to connect to PostgreSQL server...")
        connection = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="48922000",
            dbname="alx_prodev",
            port=5432,
        )
        print("✅ Successfully connected to PostgreSQL")

        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM user_data;")

        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield [dict(row) for row in batch] 

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"❌ Error while streaming batches: {e}")
        return

def batch_processing(batch_size):
    """
    Processes each batch to filter users with age > 25.
    Uses the batch generator.
    """
    for batch in stream_users_in_batches(batch_size):
        print("Processing new batch of size:", len(batch))
        filtered = [user for user in batch if int(user["age"]) > 25]
        print("Filtered users:", filtered)


if __name__ == "__main__":
    batch_processing(3) 
