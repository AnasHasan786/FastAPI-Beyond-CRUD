from pydantic import BaseModel
import uuid
from datetime import datetime, date
from src.reviews.schemas import ReviewModel
from typing import List


# Creating pydantic base model
class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    update_at: datetime


class BookDetailModel(Book):
    reviews: List[ReviewModel]


class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


# Creating pydantic base model for updating book
class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
