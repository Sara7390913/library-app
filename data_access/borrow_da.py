from model.member import Member
from model.borrow import Borrow
from model.book import Book
import json
import os
from tools.logger import Logger

class BorrowDA:
    def __init__(self):
        self.__borrow_list = []
        self.__file_name = "borrow.json"

        if os.path.exists(self.__file_name):
            try:
                with open(self.__file_name, "r", encoding="utf-8") as file:
                    data = json.load(file)

                for item in data:
                    book = Book(
                        item["book_id"],
                        item["title"],
                        item["author"],
                        item["page_count"],
                        item["publisher"],
                        item["category"],
                        item["language"],
                    )
                    member = Member(
                        item["member_id"],
                        item["name"],
                        item["family"],
                        item["age"],
                        item["mobile_number"],
                        item["national_code"],
                    )
                    borrow = Borrow(
                        item["borrow_id"],
                        member,
                        book,
                        item["date_borrow"],
                    )

                    if item["return_date"] is not None:
                        borrow.return_book(item["return_date"])

                    self.__borrow_list.append(borrow)

            except (json.JSONDecodeError, OSError, KeyError, TypeError) as error:
                Logger.error(f"Error loading borrow: {error}")

    def save(self, borrow):
        found = False

        for index, item in enumerate(self.__borrow_list):
            if item.borrow_id == borrow.borrow_id:
                self.__borrow_list[index] = borrow
                found = True
                break

        if not found:
            self.__borrow_list.append(borrow)

        data = []

        for item in self.__borrow_list:
            data.append({
                "borrow_id": item.borrow_id,
                "book_id": item.book.book_id,
                "title": item.book.title,
                "author": item.book.author,
                "page_count": item.book.page_count,
                "publisher": item.book.publisher,
                "category": item.book.category,
                "language": item.book.language,
                "member_id": item.member.member_id,
                "name": item.member.name,
                "family": item.member.family,
                "age": item.member.age,
                "mobile_number": item.member.mobile_number,
                "national_code": item.member.national_code,
                "date_borrow": item.date_borrowed,
                "return_date": item.return_date,
            })
        try:
            with open(self.__file_name, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            Logger.info(f"Borrow saved: {borrow.book.title} by {borrow.member.name}")

        except OSError as error:
            Logger.error(f"Error saving borrow: {error}")
            raise


    def find_all(self):
        return self.__borrow_list