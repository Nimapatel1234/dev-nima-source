# crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def get_books(db: Session):
    return db.query(models.BooksBook).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.BooksBook).filter(models.BooksBook.id == book_id).first()

def create_book(db: Session, book: schemas.BooksBookBase):
    db_book = models.BooksBook(
        title=book.title,
        media_type=book.media_type,
        download_count=book.download_count,
        gutenberg_id=book.gutenberg_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
