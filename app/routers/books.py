 
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List  # Add this import
# from .. import crud, schemas, database



# router = APIRouter()

# @router.get("/", response_model=List[schemas.BooksBookBase])
# def list_books(db: Session = Depends(database.get_db)):
#     return crud.get_books(db)

# @router.get("/{book_id}/", response_model=schemas.BooksBookBase)
# def get_book(book_id: int, db: Session = Depends(database.get_db)):
#     book = crud.get_book_by_id(db, book_id)
#     if not book:
#         raise HTTPException(status_code=404, detail="Book not found")
#     return book

# router/books.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List  # Add this import
from .. import crud, schemas, database

router = APIRouter()

@router.get("/", response_model=List[schemas.BooksBookBase])
def list_books(db: Session = Depends(database.get_db)):
    return crud.get_books(db)

@router.get("/{book_id}/", response_model=schemas.BooksBookBase)
def get_book(book_id: int, db: Session = Depends(database.get_db)):
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
