#!/usr/bin/python3
import psycopg2
import functools

def log_queries(func):
    """
    Decorator to log SQL queries before executing.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = None
        if args:
            query = args[0]
        elif "query" in kwargs:
            query = kwargs["query"]

        if query:
            print(f"[LOG] Executing SQL Query: {query}")

        return func(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="48922000",
        dbname="alx_prodev",
        port=5432
    )
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    users = fetch_all_users(query="SELECT * FROM user_data;")
    print("Users:", users)
