#!/usr/bin/python3
import seed

if __name__ == "__main__":
    print("Starting script...")

    seed.create_database()

    connection = seed.connect_db()
    if connection:
        print("Connected to PostgreSQL (alx_prodev)")

        seed.create_table(connection)
        print("Table checked/created.")

        seed.insert_data(connection, 'user_data.csv')
        print("Data insertion attempted.")
        cursor = connection.cursor()
        cursor.execute("""
            SELECT datname 
            FROM pg_database 
            WHERE datname = 'alx_prodev';
        """)
        result = cursor.fetchone()
        if result:
            print("✅ Database alx_prodev is present")

        cursor.execute("SELECT * FROM user_data LIMIT 5;")
        rows = cursor.fetchall()
        print("Sample rows:", rows)

        cursor.close()
        connection.close()
        print("Connection closed.")
    else:
        print("❌ Could not connect to PostgreSQL server")
