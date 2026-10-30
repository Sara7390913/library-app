from tools.validation import (date_borrowed_validator, return_date_validator)
from tools.logger import Logger


class Borrow:
    def __init__(self, borrow_id, member, book, date_borrowed):
        self.borrow_id = borrow_id
        self.member = member
        self.book = book
        self.date_borrowed = date_borrowed
        self.return_date = None
        Logger.info(f"Book borrowed: {self.book.title} by {self.member.name}")
    @property
    def borrow_id(self):
        return self.__borrow_id

    @borrow_id.setter
    def borrow_id(self, borrow_id):
        try:
            borrow_id = int(borrow_id)
            if borrow_id > 0:
                self.__borrow_id = borrow_id
            else:
                raise ValueError("Borrow ID must be positive.")

        except (ValueError, TypeError):
            raise ValueError("Invalid borrow ID.")

    @property
    def member(self):
        return self.__member

    @member.setter
    def member(self, member):
        from model.member import Member

        if not isinstance(member, Member):
            raise TypeError("Member must be a Member Object.")

        self.__member = member

    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, book):
        from model.book import Book

        if not isinstance(book, Book):
            raise TypeError("Book must be a Book Object.")
        self.__book = book

    @property
    def date_borrowed(self):
        return self.__date_borrowed


    @date_borrowed.setter
    def date_borrowed(self, date_borrowed):
        date_borrowed_validator(date_borrowed)
        self.__date_borrowed = date_borrowed

    @property
    def return_date(self):
        return self.__return_date

    @return_date.setter
    def return_date(self, return_date):
        return_date_validator(return_date)
        self.__return_date = return_date

    def return_book(self, return_date):
        self.return_date = return_date
        Logger.info(f"Book returned: {self.book.title} by {self.member.name}")

    def is_returned(self):
        return self.return_date is not None

    def get_info(self):
        return (f"borrow_id: {self.borrow_id},"
                f" member: {self.member.name},"
                f"book: {self.book.title}," 
                f"date borrowed: {self.date_borrowed}," 
                f"return_date: {self.return_date}")









