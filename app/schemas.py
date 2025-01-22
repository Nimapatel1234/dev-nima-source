 
# from pydantic import BaseModel
# from typing import List, Optional

# class BooksAuthorBase(BaseModel):
#     id: int
#     name: str
#     birth_year: Optional[int] = None
#     death_year: Optional[int] = None

#     class Config:
#         orm_mode = True

# class BooksBookBase(BaseModel):
#     id: int
#     title: str
#     media_type: str
#     download_count: Optional[int] = None
#     gutenberg_id: int
#     authors: List[BooksAuthorBase] = []

#     class Config:
#         orm_mode = True


from pydantic import BaseModel
from typing import List, Optional

# Author schema
class BooksAuthorBase(BaseModel):
    id: int
    name: str
    birth_year: Optional[int] = None
    death_year: Optional[int] = None

    class Config:
        orm_mode = True

# Book schema
class BooksBookBase(BaseModel):
    id: int
    title: str
    media_type: str
    download_count: Optional[int] = None
    gutenberg_id: int
    authors: List[BooksAuthorBase] = []

    class Config:
        orm_mode = True
