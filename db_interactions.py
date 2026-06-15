import asyncpg

pool = None


async def init_db():
    global pool
    pool = await asyncpg.create_pool(
        host="localhost", user="silletr", password="Silletr123", database="notes"
    )


async def get_notes():
    async with pool.acquire() as conn:
        return await conn.fetch("SELECT * FROM notes")


async def write_notes(note_name: str, note_text: str):
    async with pool.acquire() as conn:
        db = await conn.fetchval("SELECT current_database()")
        print("CONNECTED DB:", db)

        await conn.execute(
            """
            INSERT INTO notes(note_name, note_text)
            VALUES($1, $2)
            ON CONFLICT (note_name)
        DO UPDATE SET note_text = EXCLUDED.note_text
            """,
            note_name,
            note_text,
        )
