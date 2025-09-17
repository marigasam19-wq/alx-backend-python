#!/usr/bin/python3
import psycopg2
import functools


# Decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get("query") if "query" in kwargs else (args[0] if args else None)
        print(f"[LOG] Executing SQL query: {query}")
        return func(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    # Open PostgreSQL connection
    conn = psycopg2.connect(
        user="postgres",
        password="48922000",
        database="alx_prodev",
        host="localhost",
        port=5432
    )
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# Fetch users while logging the query
if __name__ == "__main__":
    users = fetch_all_users(query="SELECT * FROM user_data;")
    print("Users:", users)
