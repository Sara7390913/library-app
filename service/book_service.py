from data_access.book_da import BookDA
from tools.logger import Logger

class BookService:
    def __init__(self):
        self.__book_da = BookDA()

    def save(self, book):
        self.__book_da.save(book)
        Logger.info(f"BookService: book saved - {book.title}")

    def find_all(self):
        return self.__book_da.find_all()

    def find_by_id(self, book_id):
        return self.__book_da.find_by_id(book_id)