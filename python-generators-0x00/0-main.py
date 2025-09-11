#!/usr/bin/python3
import seed

if __name__ == "__main__":
    print("Starting script...")

    connection = seed.connect_db()
    if connection:
        print("Connected to MySQL server")
        seed.create_database(connection)
        connection.close()
        print("Database creation checked. Connection closed.")

        connection = seed.connect_to_prodev()
        if connection:
            print("Connected to ALX_prodev database")
            seed.create_table(connection)
            print("Table checked/created.")
            seed.insert_data(connection, 'user_data.csv')
            print("Data insertion attempted.")

            cursor = connection.cursor()
            cursor.execute(
                "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev';"
            )
            result = cursor.fetchone()
            if result:
                print("Database ALX_prodev is present")

            cursor.execute("SELECT * FROM user_data LIMIT 5;")
            rows = cursor.fetchall()
            print("Sample rows:", rows)
            cursor.close()
    else:
        print("❌ Could not connect to MySQL server")

