#!/usr/bin/python3
import asyncio
import asyncpg
print(asyncpg.__version__)


async def async_fetch_users():
    conn = await asyncpg.connect(
        user="postgres",
        password="48922000",
        database="alx_prodev",
        host="localhost",
        port=5432
    )
    rows = await conn.fetch("SELECT * FROM user_data")
    await conn.close()
    print("All user_data:", rows)
    return rows


async def async_fetch_older_users():
    conn = await asyncpg.connect(
        user="postgres",
        password="48922000",
        database="alx_prodev",
        host="localhost",
        port=5432
    )
    rows = await conn.fetch("SELECT * FROM user_data WHERE age > $1", 40)
    await conn.close()
    print("Users older than 40:", rows)
    return rows


async def fetch_concurrently():
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    return results


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
