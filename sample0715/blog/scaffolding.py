from generic_scaffold import CrudManager
from blog.models import BookData

class BookCrudManager(CrudManager):
    model = BookData
    prefix = 'books'
