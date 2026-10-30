from model.book import Book
from tools.validation import (storage_id_validator, capacity_validator, location_validator, book_validator)
from tools.logger import Logger

class Storage:

    def __init__(self, storage_id, location, capacity, book):
        self.storage_id = storage_id
        self.location = location
        self.capacity = capacity
        self.book = book

    @property
    def storage_id(self):
        return self.__storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        storage_id_validator(storage_id)
        self.__storage_id = storage_id

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        location_validator(location)
        self.__location = location

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        capacity_validator(capacity)
        self.__capacity = capacity

    def add_book(self, book):
        if len(self.book) < self.capacity:
            self.book.append(book)
            Logger.info(f"Book added to storage: {book.title}")
        else:
            raise ValueError("Storage is full.")

    def remove_book(self, book):
        if book in self.book:
            self.book.remove(book)
            Logger.info(f"Book removed to storage: {book.title}")
        else:
            raise ValueError("Book not found.")

    def find_book(self, book_id):
        for book in self.book:
            if book.book_id == book_id:
                return book
        return None

    def get_book(self):
        return self.book

    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, book):
        book_validator(book)
        self.__book = book