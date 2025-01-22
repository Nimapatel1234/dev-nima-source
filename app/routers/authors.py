 
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from .. import crud, schemas, database
# from typing import List  # Add this import

# router = APIRouter()

# @router.get("/", response_model=List[schemas.BooksAuthorBase])
# def list_authors(db: Session = Depends(database.get_db)):
#     return db.query(database.models.BooksAuthor).all()



  #####################  
  
  
# router/author.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database
from typing import List

router = APIRouter()

@router.get("/", response_model=List[schemas.BooksAuthorBase])
def list_authors(db: Session = Depends(database.get_db)):
    return db.query(database.models.BooksAuthor).all()
