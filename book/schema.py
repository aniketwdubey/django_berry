import strawberry
from typing import List
from .types import BookType
from .models import Book
@strawberry.type
class Query:
    @strawberry.field
    def books(self, author:str = None) -> List[BookType]:
        if author:
            books = Book.objects.filter(author=author)
            return books
        else:
            return Book.objects.all()
        
@strawberry.type
class Mutation:
    @strawberry.field 
    #post method
    def create_book(self, title:str, author:str) -> BookType:
        book = Book(title=title, author=author)
        book. save()
        return book
    
    @strawberry.field
    #put method
    def update_book(self, book_id:int, title:str, author:str) -> BookType:
        book = Book.objects.get(book_id=book_id)
        book.title = title
        book.author = author
        book. save()
        return book 
    
    @strawberry.field
    def delete_book(self, book_id:int) -> bool:
        book = Book.objects.get(book_id=book_id)
        book.delete()
        return True
     
schema = strawberry.Schema(query=Query, mutation=Mutation)
