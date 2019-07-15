from generic_scaffold import CrudManager
from blog.models import Book

class BookCrudManager(CrudManager):
    model = Book
    prefix = 'books'
