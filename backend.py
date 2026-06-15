from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel
from db_interactions import get_notes, init_db, write_notes


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


class InputData(BaseModel):
    note_name: str
    note_text: str


@app.post("/notes")
async def create_note(data: InputData):

    await write_notes(note_name=data.note_name, note_text=data.note_text)

    return {"status": "ok"}


@app.get("/notes")
async def get_note():

    notes = await get_notes()

    return notes
