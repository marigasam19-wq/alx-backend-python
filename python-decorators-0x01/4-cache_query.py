#!/usr/bin/python3
import psycopg2
import functools

query_cache = {}

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
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper


def cache_query(func):
    """
    Decorator to cache results of SQL queries to avoid redundant calls.
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query = kwargs.get("query") or (args[0] if args else None)
        if query in query_cache:
            print(f"[CACHE] Returning cached result for query: {query}")
            return query_cache[query]
        
        print(f"[DB] Executing and caching query: {query}")
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


if __name__ == "__main__":

    users = fetch_users_with_cache(query="SELECT * FROM user_data;")
    print("Users (first call):", users)

    users_again = fetch_users_with_cache(query="SELECT * FROM user_data;")
    print("Users (second call):", users_again)
