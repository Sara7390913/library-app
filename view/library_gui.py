import tkinter as tk
from tkinter import ttk
from controller.book_controller import BookController
from controller.storage_controller import StorageController
from controller.borrow_controller import BorrowController
from controller.member_controller import MemberController
from tkinter import messagebox
from model.book import Book
from model.borrow import Borrow
from model.member import Member
from datetime import date
from model.storage import Storage


class LibraryGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Library Management System")
        self.root.geometry("800x600")
        self.root.minsize(700, 500)
        self.book_controller = BookController()
        self.storage_controller = StorageController()
        self.borrow_controller = BorrowController()
        self.member_controller = MemberController()

        self.create_widgets()

    def create_widgets(self):
        title_label = ttk.Label(self.root, text="Library Management System", font=("Arial", 22, "bold"))

        title_label.pack(pady=30)

        subtitle_label = ttk.Label(self.root, text="Welcome to the Library", font=("Arial", 12))

        subtitle_label.pack(pady=20)

        button_frame = ttk.Frame(self.root, padding=20)
        button_frame.pack(pady=20)

        ttk.Button(button_frame, text="Manage Books", width=25, command=self.show_books).grid(row=0, column=0, padx=10,
                                                                                              pady=10)

        ttk.Button(button_frame, text="Manage Members", width=25, command=self.show_members).grid(row=1, column=0,
                                                                                                  padx=10, pady=10)

        ttk.Button(button_frame, text="Manage Storages", width=25, command=self.show_storages).grid(row=2, column=0,
                                                                                                    padx=10, pady=10)

        ttk.Button(button_frame, text="Borrow Book", width=25, command=self.borrow_book).grid(row=3, column=0, padx=10,
                                                                                              pady=10)

        ttk.Button(button_frame, text="Return Book", width=25, command=self.return_book).grid(row=4, column=0, padx=10,
                                                                                              pady=10)

        ttk.Button(button_frame, text="Borrowing Information", width=25, command=self.show_borrowing).grid(row=5,
                                                                                                           column=0,
                                                                                                           padx=10,
                                                                                                           pady=10)

    def show_books(self):
        books = self.book_controller.find_all()

        books_window = tk.Toplevel(self.root)
        books_window.title("Manage Books")
        books_window.geometry("700x600")

        ttk.Label(books_window, text="Book ID:").pack(pady=5)
        book_id_entry = ttk.Entry(books_window)
        book_id_entry.pack(pady=5)

        ttk.Label(books_window, text="Title:").pack(pady=5)
        title_entry = ttk.Entry(books_window)
        title_entry.pack(pady=5)

        ttk.Label(books_window, text="Author:").pack(pady=5)
        author_entry = ttk.Entry(books_window)
        author_entry.pack(pady=5)

        ttk.Label(books_window, text="Page Count:").pack(pady=5)
        page_count_entry = ttk.Entry(books_window)
        page_count_entry.pack(pady=5)

        ttk.Label(books_window, text="Publisher:").pack(pady=5)
        publisher_entry = ttk.Entry(books_window)
        publisher_entry.pack(pady=5)

        ttk.Label(books_window, text="Category:").pack(pady=5)
        category_entry = ttk.Entry(books_window)
        category_entry.pack(pady=5)

        ttk.Label(books_window, text="Language:").pack(pady=5)
        language_entry = ttk.Entry(books_window)
        language_entry.pack(pady=5)

        def save_book():
            try:
                book = Book(int(book_id_entry.get()), title_entry.get(), author_entry.get(),
                            int(page_count_entry.get()), publisher_entry.get(),
                            category_entry.get(), language_entry.get())

                self.book_controller.save(book)
                messagebox.showinfo("Success", "Book saved successfully.")

                for widget in books_window.winfo_children():
                    widget.destroy()

                self.show_books()

            except (ValueError, TypeError) as error:
                messagebox.showerror("Error", str(error))

        ttk.Button(books_window, text="Save Book", command=save_book).pack(pady=10)

        ttk.Label(books_window, text="Saved Books").pack(pady=10)

        for book in self.book_controller.find_all():
            ttk.Label(books_window, text=f"ID: {book.book_id} | Title: {book.title} | Author: {book.author}").pack(
                pady=3)

    def show_members(self):
        members_window = tk.Toplevel(self.root)
        members_window.title("Manage Members")
        members_window.geometry("500x600")

        ttk.Label(members_window, text="Member ID:").pack(pady=5)
        member_id_entry = ttk.Entry(members_window)
        member_id_entry.pack(pady=5)

        ttk.Label(members_window, text="Name:").pack(pady=5)
        name_entry = ttk.Entry(members_window)
        name_entry.pack(pady=5)

        ttk.Label(members_window, text="Family:").pack(pady=5)
        family_entry = ttk.Entry(members_window)
        family_entry.pack(pady=5)

        ttk.Label(members_window, text="Age:").pack(pady=5)
        age_entry = ttk.Entry(members_window)
        age_entry.pack(pady=5)

        ttk.Label(members_window, text="Mobile Number:").pack(pady=5)
        mobile_number_entry = ttk.Entry(members_window)
        mobile_number_entry.pack(pady=5)

        ttk.Label(members_window, text="National Code:").pack(pady=5)
        national_code_entry = ttk.Entry(members_window)
        national_code_entry.pack(pady=5)

        def save_member():
            try:
                from model.member import Member

                member = Member(
                    int(member_id_entry.get()),
                    name_entry.get(),
                    family_entry.get(),
                    int(age_entry.get()),
                    mobile_number_entry.get(),
                    national_code_entry.get(),
                )

                self.member_controller.save(member)

                messagebox.showinfo("Success", "Member saved successfully.")

            except (ValueError, TypeError, AttributeError) as error:
                messagebox.showerror("Error", str(error))

        ttk.Button(members_window, text="Save Member", command=save_member).pack(pady=10)

        ttk.Label(members_window, text="Registered Members").pack(pady=10)

        for member in self.member_controller.find_all():
            ttk.Label(members_window, text=(f"ID: {member.member_id} |"
                                            f"Name: {member.name} {member.family}")).pack(pady=3)

    def show_storages(self):
        storages_window = tk.Toplevel(self.root)
        storages_window.title("Manage Storages")
        storages_window.geometry("500x400")

        ttk.Label(storages_window, text="Storage Management", font=("Arial", 16, "bold")).pack(pady=15)

        ttk.Label(storages_window, text="Registered Storages").pack(pady=10)

        ttk.Label(storages_window, text="Storage ID:").pack(pady=5)
        storage_id_entry = ttk.Entry(storages_window)
        storage_id_entry.pack(pady=5)

        ttk.Label(storages_window, text="Location:").pack(pady=5)
        location_entry = ttk.Entry(storages_window)
        location_entry.pack(pady=5)

        ttk.Label(storages_window, text="Capacity:").pack(pady=5)
        capacity_entry = ttk.Entry(storages_window)
        capacity_entry.pack(pady=5)


        for storage in self.storage_controller.find_all():
            ttk.Label(storages_window, text=(f"ID: {storage.storage_id} |"
                                             f"Location: {storage.location} |"
                                             f"Capacity: {storage.capacity} |"
                                             f"Books: {len(storage.book)}")).pack(pady=5)

        def save_storage():
            try:
                storage_id = int(storage_id_entry.get())
                location = location_entry.get()
                capacity = int(capacity_entry.get())

                storage = Storage(storage_id, location, capacity, [])

                self.storage_controller.save(storage)
                messagebox.showinfo("Success", "Storage saved successfully.")

                storages_window.destroy()
                self.show_storages()

            except (ValueError, TypeError) as error:
                messagebox.showerror("Error", str(error))

        ttk.Button(storages_window, text="Save Storage", command=save_storage).pack(pady=10)
    def show_borrowing(self):
        borrowing_window = tk.Toplevel(self.root)
        borrowing_window.title("Borrowing Information")
        borrowing_window.geometry("600x400")

        ttk.Label(borrowing_window, text="Borrowing Information:", font=("Arial", 14, "bold")).pack(pady=10)

        for borrow in self.borrow_controller.find_all():
            ttk.Label(borrowing_window, text=borrow.get_info()).pack(pady=5)

    def borrow_book(self):
        borrow_window = tk.Toplevel(self.root)
        borrow_window.title("Borrow Book")
        borrow_window.geometry("350x250")

        ttk.Label(borrow_window, text="Book ID:").pack(pady=5)
        book_id_entry = ttk.Entry(borrow_window)
        book_id_entry.pack(pady=5)

        ttk.Label(borrow_window, text="Member ID:").pack(pady=5)
        member_id_entry = ttk.Entry(borrow_window)
        member_id_entry.pack(pady=5)

        ttk.Button(borrow_window, text="Borrow", command=lambda: self.save_borrow(book_id_entry.get(),
                                                                                  member_id_entry.get(),
                                                                                  borrow_window)).pack(pady=5)

    def save_borrow(self, book_id, member_id, borrow_window):
        try:
            book_id = int(book_id)
            member_id = int(member_id)

            book = self.book_controller.find_by_id(book_id)
            member = self.member_controller.find_by_id(member_id)

            if book is None or member is None:
                messagebox.showerror("Error", "Book or Member not found.")
                return

            borrow = Borrow(borrow_id=1, member=member, book=book, date_borrowed=date.today().strftime("%Y-%m-%d"))

            self.borrow_controller.save(borrow)

            messagebox.showinfo("Success", "Book borrowed successfully.")
            borrow_window.destroy()

        except(ValueError, TypeError, AttributeError) as error:
            messagebox.showerror("Error", str(error))

    def return_book(self):
        return_window = tk.Toplevel(self.root)
        return_window.title("Return Book")
        return_window.geometry("350x200")

        ttk.Label(return_window, text="Borrow ID:").pack(pady=5)

        borrow_id_entry = ttk.Entry(return_window)
        borrow_id_entry.pack(pady=5)

        ttk.Button(return_window, text="Return",
                   command=lambda: self.save_return(borrow_id_entry.get(), return_window)).pack(pady=10)

    def save_return(self, borrow_id, return_window):
        try:
            borrow_id = int(borrow_id)

            borrows = self.borrow_controller.find_all()

            for borrow in borrows:
                if borrow.borrow_id == borrow_id:
                    if borrow.is_returned():
                        messagebox.showinfo("Warning", "This book has already been returned.")
                        return

                    return_date = date.today().strftime("%Y-%m-%d")
                    borrow.return_book(return_date)

                    # save the update borrowing information
                    self.borrow_controller.save(borrow)
                    messagebox.showinfo("Success", "Book returned successfully.")

                    return_window.destroy()
                    return

            messagebox.showerror("Error", "Borrowing record not found.")

        except (ValueError, TypeError, AttributeError) as error:
            messagebox.showerror("Error", str(error))

    def run(self):
        self.root.mainloop()
