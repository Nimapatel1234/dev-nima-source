 
# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from .database import Base

# class BooksBook(Base):
#     __tablename__ = "books_book"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     media_type = Column(String)
#     download_count = Column(Integer, nullable=True)
#     gutenberg_id = Column(Integer, unique=True, nullable=False)

#     authors = relationship("BooksAuthor", secondary="books_book_authors", back_populates="books")


# class BooksAuthor(Base):
#     __tablename__ = "books_author"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     birth_year = Column(Integer, nullable=True)
#     death_year = Column(Integer, nullable=True)

#     books = relationship("BooksBook", secondary="books_book_authors", back_populates="authors")


# class BooksBookAuthors(Base):
#     __tablename__ = "books_book_authors"

#     book_id = Column(Integer, ForeignKey("books_book.id"), primary_key=True)
#     author_id = Column(Integer, ForeignKey("books_author.id"), primary_key=True)


########################################################

# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from .database import Base

# # Book model
# class BooksBook(Base):
#     __tablename__ = "books_book"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     media_type = Column(String)
#     download_count = Column(Integer, nullable=True)
#     gutenberg_id = Column(Integer, unique=True, nullable=False)

#     # Relationships
#     authors = relationship("BooksAuthor", secondary="books_book_authors", back_populates="books")

# # Author model
# class BooksAuthor(Base):
#     __tablename__ = "books_author"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     birth_year = Column(Integer, nullable=True)
#     death_year = Column(Integer, nullable=True)

#     # Relationship with books
#     books = relationship("BooksBook", secondary="books_book_authors", back_populates="authors")

# # Association table for many-to-many relationship between Books and Authors
# class BooksBookAuthors(Base):
#     __tablename__ = "books_book_authors"

#     book_id = Column(Integer, ForeignKey("books_book.id"), primary_key=True)
#     author_id = Column(Integer, ForeignKey("books_author.id"), primary_key=True)


###############################


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Book model
class BooksBook(Base):
    __tablename__ = "books_book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    media_type = Column(String)
    download_count = Column(Integer, nullable=True)
    gutenberg_id = Column(Integer, unique=True, nullable=False)

    authors = relationship("BooksAuthor", secondary="books_book_authors", back_populates="books")

# Author model
class BooksAuthor(Base):
    __tablename__ = "books_author"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birth_year = Column(Integer, nullable=True)
    death_year = Column(Integer, nullable=True)

    books = relationship("BooksBook", secondary="books_book_authors", back_populates="authors")

# Association table for many-to-many relationship between Books and Authors
class BooksBookAuthors(Base):
    __tablename__ = "books_book_authors"

    book_id = Column(Integer, ForeignKey("books_book.id"), primary_key=True)
    author_id = Column(Integer, ForeignKey("books_author.id"), primary_key=True)
