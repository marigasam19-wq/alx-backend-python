#!/usr/bin/python3
import psycopg2



class ExecuteQuery:
    """
    Context manager to execute a query with parameters
    and automatically handle connection, cursor, and cleanup.
    """

    def __init__(self, query, params=None):
        self.query = query
        self.params = params
        self.conn = None
        self.cursor = None
        self.results = None

    def __enter__(self):
        # Connect to PostgreSQL
        self.conn = psycopg2.connect(
            host="localhost",
            database="alx_prodev",
            user="postgres",
            password="48922000",
            port=5432
        )
        self.cursor = self.conn.cursor()

        # Execute query with parameters if provided
        if self.params:
            self.cursor.execute(self.query, self.params)
        else:
            self.cursor.execute(self.query)

        # Fetch all results immediately
        self.results = self.cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close resources
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    query = "SELECT * FROM user_data WHERE age > %s"
    params = (25,)

    with ExecuteQuery(query, params) as results:
        for row in results:
            print(row)
