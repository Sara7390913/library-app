from tools.logger import Logger
import json
import os
from model.book import Book

class BookDA:
    def __init__(self):
        self.__book_list = []
        self.__file_name = "books.json"

        if os.path.exists(self.__file_name):
            try:
                with open(self.__file_name, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    for item in data:
                        book = Book(item["book_id"], item["title"], item["author"], item["page_count"], item["publisher"], item["category"],
                                    item["language"])
                        self.__book_list.append(book)

            except (json.JSONDecodeError, OSError) as error:
                Logger.error(f"Error loading books: {error}")

    def save(self, book):
        self.__book_list.append(book)
        data = []
        for item in self.__book_list:
            data.append({"book_id": item.book_id, "title": item.title, "author": item.author, "page_count": item.page_count,
                         "publisher": item.publisher, "category": item.category, "language": item.language})

            try:
                with open(self.__file_name, "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                Logger.info(f"Book saved: {book.title}")

            except OSError as error:
                Logger.error(f"Error saving book: {error}")
                raise

    def find_all(self):
        return self.__book_list

    def find_by_id(self, book_id):
        for book in self.__book_list:
            if book.book_id == book_id:
                return book
        return None