
from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

class Book(BaseModel):
    id: UUID | int
    title: str = Field(min_length=1, default='')
    author: str = Field(min_length=1, max_length=100, default='')
    description: str = Field(min_length=1, max_length=300, default='')
    rating : int = Field(gt=0, lt=101, default=0)

    def __str__(self):
        return self.title 
