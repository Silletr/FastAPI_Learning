import asyncpg
import asyncio
from loguru import logger


passwd = input("Enter Password: ")  # For safety xD

conn = asyncpg.connect(
    port=5432, host="localhost", user="silletr", password=passwd, database="notes"
)


#  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
async def main():
    logger.success("Connected to 'notes' DB btw")
    await conn.fetch(
        """
        SELECT * FROM notes
        """,
    )
    rows = await conn.fetch("SELECT * FROM notes")
    print(rows)

    await conn.close()


#  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
async def write_notes(note: str):
    logger.info("Starting writing notes in DB")
    await conn.execute(
        """
            INSERT INTO notes(text)
            VALUES($1)
            ON CONFLICT (text) DO NOTHING
            """,
        note.strip(),
    )
    logger.success("As long as I 'now it's added. But I dunno, check it out, ig")


#  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if __name__ == "__main__":
    asyncio.run(main())
