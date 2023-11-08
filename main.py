
from fastapi import FastAPI, HTTPException
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


app = FastAPI()

BOOKS = []

@app.get('/books')
def get_books(count:int=None):
    "Retrieve multiple books"
    return BOOKS if count is None else BOOKS[:count]


@app.post('/books')
def create_book(book: Book):
    "Create and return a new book"
    BOOKS.append(book)
    return book 




if __name__ == '__main__':
    import uvicorn 
    filename:str = __file__.split('\\')[-1].split('.')[0]
    uvicorn.run(f'{filename}:app', reload=True)