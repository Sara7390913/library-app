class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    @property
    def book_id(self):
        return self.__book_id

    @book_id.setter
    def book_id(self, book_id):
        try:
            book_id = int(book_id)
        except(ValueError, TypeError):
            raise ValueError("Book ID must be an integer.")
