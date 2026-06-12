from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    note_name: str
    note_text: str
