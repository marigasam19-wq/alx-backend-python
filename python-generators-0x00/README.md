### 0. Getting Started with Python Generators (seed.py)

Objective: Set up the database ALX_prodev with a user_data table.

Functions:

connect_db() → connect to MySQL server
create_database(connection) → create DB if not exists
connect_to_prodev() → connect to ALX_prodev DB
create_table(connection) → create user_data table
insert_data(connection, data) → populate from user_data.csv

✅ Tested via 0-main.py

### 1. Stream Users (0-stream_users.py)

Objective: Use a generator to fetch rows one by one.

Function:

def stream_users():
    """Yields rows from user_data one at a time."""


Constraint: Only 1 loop inside function.

Example (1-main.py):

{'user_id': 'uuid', 'name': 'Alice', 'email': 'alice@example.com', 'age': 25}

### 2. Batch Processing (1-batch_processing.py)

Objective: Fetch and process data in batches.

Functions:

def stream_users_in_batches(batch_size):  # yields lists of rows
def batch_processing(batch_size):         # filters users age > 25


Constraint: Max 3 loops in total.

Example (2-main.py):

{'user_id': 'uuid1', 'name': 'Alice', 'age': 30}
{'user_id': 'uuid2', 'name': 'Bob', 'age': 45}

### 3. Lazy Pagination (2-lazy_paginate.py)

Objective: Implement lazy page fetching with LIMIT + OFFSET.

Functions:

def paginate_users(page_size, offset):  # fetch one page
def lazy_pagination(page_size):         # generator yielding pages


Constraint: Only 1 loop in lazy generator.

Example (3-main.py):

{'user_id': 'uuid1', 'name': 'Alice', 'age': 25}
{'user_id': 'uuid2', 'name': 'Bob', 'age': 40}

### 4. Memory-Efficient Aggregation (4-stream_ages.py)

Objective: Compute average age without SQL AVG() or loading all rows.

Functions:

def stream_user_ages():  # yields one age at a time
def calculate_average_age():  # computes average using generator


Constraint: Only 2 loops (one in generator, one in aggregator).

Example:
Average age of users: 62.38


