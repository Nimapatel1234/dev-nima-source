 
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

# @router.get("/{book_id}/", response_model=schemas.BooksBookBase)
# def get_book(book_id: int, db: Session = Depends(database.get_db)):
#     book = crud.get_book_by_id(db, book_id)
#     if not book:
#         raise HTTPException(status_code=404, detail="Book not found")
#     return book


######################################

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from .. import crud, schemas, database

# router = APIRouter()

# @router.get("/", response_model=List[schemas.BooksBookBase])
# def list_books(db: Session = Depends(database.get_db)):
#     books = crud.get_books(db)  # Fetch books
#     # Eager-load authors for each book
#     for book in books:
#         book.authors = (
#             db.query(models.BooksAuthor)
#             .join(models.BooksBookAuthors)
#             .filter(models.BooksBookAuthors.book_id == book.id)
#             .all()
#         )
#     return books

# @router.get("/{book_id}/", response_model=schemas.BooksBookBase)
# def get_book(book_id: int, db: Session = Depends(database.get_db)):
#     book = crud.get_book_by_id(db, book_id)
#     if not book:
#         raise HTTPException(status_code=404, detail="Book not found")
#     return book

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, database

router = APIRouter()

# List all books and their authors
@router.get("/", response_model=List[schemas.BooksBookBase])
def list_books(db: Session = Depends(database.get_db)):
    books = crud.get_books(db)
    return books

# Get a single book by ID, along with its authors
@router.get("/{book_id}/", response_model=schemas.BooksBookBase)
def get_book(book_id: int, db: Session = Depends(database.get_db)):
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
