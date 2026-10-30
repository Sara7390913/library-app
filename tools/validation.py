import re
from datetime import datetime


# =============================================
# book validator
# =============================================

def title_validator(title):
    if not isinstance(title, str):
        raise ValueError("Invalid title")

    if not re.fullmatch(r"^[A-Za-zآ-ی\s]{3,100}$", title):
        raise ValueError("Invalid title")


def author_validator(author):
    if not isinstance(author, str):
        raise ValueError("Invalid author")

    if not re.fullmatch(r"[a-zA-Zآ-ی\s]{3,50}", author):
        raise ValueError("Invalid author")


def page_count_validator(page_count):
    if not isinstance(page_count, int) or isinstance(page_count, bool):
        raise ValueError("Invalid page_counts")

    if page_count <= 0:
        raise ValueError("page counts must be positive.")


def publisher_validator(publisher):
    if not isinstance(publisher, str):
        raise ValueError("Invalid publisher")

    if not re.fullmatch(r"[a-zA-Zآ-ی\s]{2,100}", publisher):
        raise ValueError("Invalid publisher")


def category_validator(category):
    if not isinstance(category, str):
        raise ValueError("Invalid category")

    if not re.fullmatch(r"[a-zA-Zآ-ی\s]{2,50}", category):
        raise ValueError("Invalid category")


def language_validator(language):
    if not isinstance(language, str):
        raise ValueError("Invalid language")

    if not re.fullmatch(r"[a-zA-Zآ-ی\S]{2,30}", language):
        raise ValueError("Invalid language")


# =============================================
# member validator
# =============================================

def name_validator(name):
    if not isinstance(name, str):
        raise ValueError("Invalid name")

    if not re.fullmatch(r"[a-zA-Zآ-ی\s]{3,50}", name):
        raise ValueError("Invalid name")


def family_validator(family):
    if not isinstance(family, str):
        raise ValueError("Invalid family")

    if not re.fullmatch(r"[a-zA-Zآ-ی\s]{3,50}", family):
        raise ValueError("Invalid family")


def age_validator(age):
    if not isinstance(age, int) or isinstance(age, bool):
        raise ValueError("Age must be an integer.")

    if not 1 <= age <= 120:
        raise ValueError("Age must be between 1 and 120.")


def mobile_number_validator(mobile_number):
    if not isinstance(mobile_number, str):
        raise ValueError("Invalid mobile number")

    if not re.fullmatch(r"09\d{9}", mobile_number):
        raise ValueError("Invalid mobile number")


def national_code_validator(national_code):
    if not isinstance(national_code, str):
        raise ValueError("Invalid national code")

    if not re.fullmatch(r"\d{10}", national_code):
        raise ValueError("Invalid national code")


# =============================================
# storage validator
# =============================================

def storage_id_validator(storage_id):
    if not isinstance(storage_id, int) or isinstance(storage_id, bool):
        raise ValueError("Storage id must be an integer.")

    if storage_id <= 0:
        raise ValueError("Storage id must be positive.")


def capacity_validator(capacity):
    if not isinstance(capacity, int) or isinstance(capacity, bool):
        raise ValueError("Capacity must be an integer.")

    if capacity <= 0:
        raise ValueError("Capacity must be positive.")


def location_validator(location):
    if not isinstance(location, str):
        raise ValueError("Location must be an string.")

    if not location.strip():
        raise ValueError("Location must not be empty.")


def book_validator(book):
    if not isinstance(book, list):
        raise ValueError("Books must be a list")

    for item in book:
        if not hasattr(item, "book_id") or not hasattr(item, "title"):
            raise ValueError("All items must be Book objects .")


# =============================================
# borrow validator
# =============================================

def date_borrowed_validator(date_borrowed):
    if not isinstance(date_borrowed, str):
        raise ValueError("Date_borrowed must be an string.")

    try:
        datetime.strptime(date_borrowed, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date_borrowed")


def return_date_validator(return_date):
    if return_date is None:
        return

    if not isinstance(return_date, str):
        raise ValueError("Return_date must be an string.")

    try:
        datetime.strptime(return_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid return_date")
