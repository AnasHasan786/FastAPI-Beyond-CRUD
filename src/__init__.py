from fastapi import FastAPI, status
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.reviews.routes import review_router
from contextlib import asynccontextmanager
from .errors import register_all_errors
from .middleware import register_middleware

version = "v1"
version_prefix = f"/api/{version}"

app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version=version,
    contact={"name": "Anas Hasan", "email": "anas.hassan9417@gmail.com"},
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
)

register_all_errors(app)
register_middleware(app)

app.include_router(book_router, prefix=f"{version_prefix}/books", tags=["books"])

app.include_router(auth_router, prefix=f"{version_prefix}/auths", tags=["auths"])

app.include_router(review_router, prefix=f"{version_prefix}/reviews", tags=["reviews"])
