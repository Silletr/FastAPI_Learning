from fastapi import FastAPI
from pydantic import BaseModel
from db_interactions import write_notes  # your existing local import

app = FastAPI()


class InputData(BaseModel):
    note_name: str
    note_text: str


@app.get("/notes")
async def writing_note_to_db():
    return {"notes": []}  # Will work later - wait a min pls


@app.post("/notes")
async def create_note(data: InputData):
    await write_notes(data.note_text)
    return {"status": "ok", "note_text": data.note_text}
