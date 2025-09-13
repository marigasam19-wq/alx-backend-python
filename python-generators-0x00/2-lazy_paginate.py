#!/usr/bin/python3
import psycopg2.extras
import seed  # your seed.py with connect_db()

def paginate_users(page_size, offset):
    """Fetch a page of users with limit and offset from PostgreSQL."""
    connection = seed.connect_db()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s;", (page_size, offset))
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return [dict(row) for row in rows]


def lazy_pagination(page_size):
    """
    Generator to lazily fetch pages of users from DB.
    Yields one page (list of dicts) at a time.
    """
    offset = 0
    while True:
        rows = paginate_users(page_size, offset)
        if not rows:
            break
        yield rows
        offset += page_size
