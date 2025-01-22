 
from fastapi import FastAPI
from .routers import books, authors

app = FastAPI(title="FastAPI PostgreSQL Integration")

# Include routers
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(authors.router, prefix="/authors", tags=["Authors"])

