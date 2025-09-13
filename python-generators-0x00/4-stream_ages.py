#!/usr/bin/python3
import psycopg2
import psycopg2.extras

def stream_user_ages():
    """
    Generator that yields user ages one by one from PostgreSQL.
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
        cursor.execute("SELECT age FROM user_data;")

        for row in cursor:
            yield int(row["age"])  

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"❌ Error streaming ages: {e}")


def calculate_average_age():
    """
    Calculate average age using the generator without loading all data.
    """
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1

    if count == 0:
        print("No users found.")
    else:
        average = total / count
        print(f"Average age of users: {average:.2f}")


if __name__ == "__main__":
    calculate_average_age()
