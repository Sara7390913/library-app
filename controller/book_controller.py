from service.book_service import BookService
from tools.logger import Logger

class BookController:
    def __init__(self):
         self.book_service = BookService()

    def save(self, book):
        try:
            self.book_service.save(book)
            Logger.info("BookController: book saved successfully")
        except (ValueError, TypeError) as e:
            Logger.error(f"Error saving book: {e}")
            raise

    def find_all(self):
        try:
            return self.book_service.find_all()
        except Exception as e:
            Logger.error(f"Error finding books: {e}")
            raise

    def find_by_id(self, book_id):
        return self.book_service.find_by_id(book_id)

