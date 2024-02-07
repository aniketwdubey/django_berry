import strawberry
from .models import Book
@strawberry.django.type(Book)
class BookType:
    book_id: int
    title: str
    author: str