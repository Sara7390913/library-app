from tools.logger import Logger
from tools.validation import (
    title_validator,
    author_validator,
    page_count_validator,
    publisher_validator,
    category_validator,
    language_validator)




class Book:
    def __init__(self, book_id, title, author, page_count, publisher, category, language):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.page_count = page_count
        self.publisher = publisher
        self.category = category
        self.language = language
        Logger.info(f"Book created: {self.title}")

    @property
    def book_id(self):
        return self.__book_id

    @book_id.setter
    def book_id(self, book_id):
        try:
            book_id = int(book_id)
        except(ValueError, TypeError):
            raise ValueError("Book ID must be an integer.")
        if book_id <= 0:
            raise ValueError("Book ID must be greater than 0.")

        self.__book_id = book_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        title_validator(title)
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        author_validator(author)
        self.__author = author

    @property
    def page_count(self):
        return self.__page_count

    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, bool):
            raise ValueError("Invalid page count.")

        try:
            page_count = int(page_count)

        except (ValueError, TypeError):
            raise ValueError("Invalid page count.")

        page_count_validator(page_count)
        self.__page_count = page_count

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher):
        publisher_validator(publisher)

        self.__publisher = publisher

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        category_validator(category)
        self.__category = category

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        language_validator(language)
        self.__language = language
