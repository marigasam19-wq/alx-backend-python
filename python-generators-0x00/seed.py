#!/usr/bin/python3
import psycopg2
from psycopg2 import sql
import csv
import uuid


def connect_db():
    """Connect to PostgreSQL (alx_prodev database)."""
    try:
        print("Trying to connect to PostgreSQL server...")
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="48922000",
            dbname="alx_prodev",
            port=5432,
        )
        print("✅ Successfully connected to PostgreSQL")
        return connection
    except Exception as e:
        print(f"❌ Error while connecting to PostgreSQL: {e}")
        return None


def create_database():
    """Create database alx_prodev if it doesn’t exist."""
    try:
        # connect without dbname, to postgres system db
        conn = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="48922000",
            dbname="postgres",
            port=5432,
        )
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM pg_database WHERE datname='alx_prodev';")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute("CREATE DATABASE alx_prodev;")
            print("✅ Database alx_prodev created")
        else:
            print("ℹ️ Database alx_prodev already exists")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error creating database: {e}")


def create_table(connection):
    """Create table user_data if not exists."""
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id UUID PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age NUMERIC NOT NULL
            );
        """)
        connection.commit()
        cursor.close()
        print("✅ Table user_data created successfully")
    except Exception as e:
        print(f"❌ Error creating table: {e}")


def insert_data(connection, csv_file):
    """Insert data into user_data from a CSV file."""
    try:
        cursor = connection.cursor()
        with open(csv_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                user_id = str(uuid.uuid4())
                name = row["name"]
                email = row["email"]
                age = row["age"]

                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, name, email, age))

        connection.commit()
        cursor.close()
        print("✅ Data inserted successfully")
    except Exception as e:
        print(f"❌ Error inserting data: {e}")
    except FileNotFoundError:
        print(f"❌ CSV file {csv_file} not found")
