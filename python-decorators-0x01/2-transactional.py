#!/usr/bin/python3
import psycopg2
import functools

def with_db_connection(func):
    """
    Decorator to open and close PostgreSQL database connection automatically.
    Passes the connection object to the wrapped function.
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
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper


def transactional(func):
    """
    Decorator to manage transactions: commit if success, rollback if error.
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            print("[LOG] Transaction committed ✅")
            return result
        except Exception as e:
            conn.rollback()
            print("[ERROR] Transaction rolled back ❌:", e)
            raise
    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE user_data SET email = %s WHERE id = %s", (new_email, user_id))
    print(f"[LOG] Updated user {user_id} with new email: {new_email}")
    cursor.close()


if __name__ == "__main__":
    # Example update
    update_user_email(user_id=1, new_email="Crawford_Cartwright@hotmail.com")
