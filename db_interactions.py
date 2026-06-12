import asyncpg
import asyncio
from loguru import logger


passwd = input("Enter Password: ")


async def main():
    conn = await asyncpg.connect(
        port=5432, host="localhost", user="silletr", password=passwd, database="notes"
    )
    logger.success("Connected to 'notes' DB btw")
    await conn.execute("INSERT INTO notes(text) VALUES($1)", "Hello there")
    rows = await conn.fetch("SELECT * FROM notes")
    print(rows)

    await conn.close()


asyncio.run(main())
