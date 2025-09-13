#!/usr/bin/python3
import time
import psycopg2
import functools

def with_db_connection(func):
    """
    Decorator to open and close PostgreSQL connection automatically.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="48922000",
            dbname="alx_prodev",
            port=5432
        )
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

def retry_on_failure(retries=3, delay=2):
    """
    Decorator to retry function execution if an exception occurs.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    print(f"[RETRY] Attempt {attempt} failed with error: {e}")
                    if attempt < retries:
                        print(f"⏳ Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        print("❌ All retry attempts failed.")
                        raise
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data;")
    rows = cursor.fetchall()
    cursor.close()
    return rows


if __name__ == "__main__":
    try:
        users = fetch_users_with_retry()
        print("Users:", users)
    except Exception as e:
        print("Final Error:", e)
