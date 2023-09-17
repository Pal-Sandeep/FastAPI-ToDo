from pydantic import BaseModel
from fastapi import FastAPI

class ToDo(BaseModel):
    id: int
    item: str