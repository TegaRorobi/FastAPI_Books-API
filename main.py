
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


@app.get('/books/{book_id}')
def retrieve_book(book_id:UUID):
    "Retrieve the detils of a specific book"
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(
        status_code=404, 
        detail=f"Book item with id {book_id} not found")


@app.put('/books/{book_id}')
def update_book(book_id:UUID, book:Book):
    "Update the details of a book"
    for idx, existing_book in enumerate(BOOKS):
        if existing_book.id == book_id:
            BOOKS[idx] = book 
            return book
    raise HTTPException(
        status_code=404, 
        detail=f"Book item with id {book_id} not found")




if __name__ == '__main__':
    import uvicorn 
    filename:str = __file__.split('\\')[-1].split('.')[0]
    uvicorn.run(f'{filename}:app', reload=True)