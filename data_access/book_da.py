class BookDA:
    def __init__(self):
        self.__book_list = []

    def save(self, book):
        self.__book_list.append(book)

    def find_all(self):
        return self.__book_list

    def find_by_id(self, book_id):
        for book in self.__book_list:
            if book.book_id == book_id:
                return book
        return None
