# # crud.py
# from sqlalchemy.orm import Session
# from . import models, schemas

# def get_books(db: Session):
#     return db.query(models.BooksBook).all()

# def get_book_by_id(db: Session, book_id: int):
#     return db.query(models.BooksBook).filter(models.BooksBook.id == book_id).first()

# def create_book(db: Session, book: schemas.BooksBookBase):
#     db_book = models.BooksBook(
#         title=book.title,
#         media_type=book.media_type,
#         download_count=book.download_count,
#         gutenberg_id=book.gutenberg_id
#     )
#     db.add(db_book)
#     db.commit()
#     db.refresh(db_book)
# #     return db_book

######################################################

# from sqlalchemy.orm import Session
# from . import models, schemas

# def get_books(db: Session):
#     return db.query(models.BooksBook).all()  # Lazy-loaded relationships

# def get_book_by_id(db: Session, book_id: int):
#     book = db.query(models.BooksBook).filter(models.BooksBook.id == book_id).first()
#     if book:
#         # Eager-load authors relationship
#         book.authors = (
#             db.query(models.BooksAuthor)
#             .join(models.BooksBookAuthors)
#             .filter(models.BooksBookAuthors.book_id == book_id)
#             .all()
#         )
# #     return book

# def get_book_by_id(db: Session, book_id: int):
#     # Query for the book by ID
#     book = db.query(models.BooksBook).filter(models.BooksBook.id == book_id).first()
    
#     if book:
#         # Eager-load authors relationship
#         authors = (
#             db.query(models.BooksAuthor)
#             .join(models.BooksBookAuthors)
#             .filter(models.BooksBookAuthors.book_id == book_id)
#             .all()
#         )
#         # Attach authors to book instance
#         book.authors = authors
#         return book  # Return the book along with authors
#     else:
#         return None  # No book found, return None


##########################################

# from sqlalchemy.orm import Session
# from . import models, schemas

# def get_books(db: Session):
#     return db.query(models.BooksBook).all()

# def get_book_by_id(db: Session, book_id: int):
#     book = db.query(models.BooksBook).filter(models.BooksBook.id == book_id).first()
#     if book:
#         # Eager load the authors for the book
#         book.authors = db.query(models.BooksAuthor).join(models.BooksBookAuthors).filter(
#             models.BooksBookAuthors.book_id == book.id).all()
#     return book

# crud.py
from sqlalchemy.orm import Session
from . import models

def get_books(db: Session):
    # Fetch all books along with their associated authors
    books = db.query(models.BooksBook).all()
    for book in books:
        # Eager-load authors for each book
        book.authors = db.query(models.BooksAuthor).join(models.BooksBookAuthors).filter(
            models.BooksBookAuthors.book_id == book.id).all()
    return books

def get_book_by_id(db: Session, book_id: int):
    # Fetch a single book along with its authors
    book = db.query(models.BooksBook).filter(models.BooksBook.id == book_id).first()
    if book:
        book.authors = db.query(models.BooksAuthor).join(models.BooksBookAuthors).filter(
            models.BooksBookAuthors.book_id == book.id).all()
    return book

