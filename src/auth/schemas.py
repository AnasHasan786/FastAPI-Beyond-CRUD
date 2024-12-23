from pydantic import BaseModel, Field
from src.books.schemas import Book
from src.reviews.schemas import ReviewModel
from typing import List
import uuid
from datetime import datetime


class UserCreateModel(BaseModel):
    firstname: str = Field(max_length=25)
    lastname: str = Field(max_length=25)
    username: str = Field(max_length=8)
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)


class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    firstname: str
    lastname: str
    is_verified: bool
    password_hash: str = Field(exclude=True)
    created_at: datetime
    update_at: datetime


class UserBooksModel(UserModel):
    books: List[Book]
    reviews: List[ReviewModel]


class UserLoginModel(BaseModel):
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)


class EmailModel(BaseModel):
    addresses: List[str]


class PasswordResetRequestModel(BaseModel):
    email: str


class PasswordResetConfirmModel(BaseModel):
    new_password: str
    confirm_new_password: str
