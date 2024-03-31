import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.isbn not in self.books:
            self.books[book.isbn] = book
            messagebox.showinfo("Success", f"Book '{book.title}' added successfully.")
        else:
            messagebox.showerror("Error", "Book with ISBN already exists.")

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            messagebox.showinfo("Success", "Book removed successfully.")
        else:
            messagebox.showerror("Error", "Book not found.")

    def display_books(self):
        if self.books:
            book_list = "\n".join([str(book) for book in self.books.values()])
            messagebox.showinfo("Available Books", book_list)
        else:
            messagebox.showinfo("Available Books", "No books available.")

class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author

    def __str__(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}"

def add_book():
    isbn = isbn_entry.get()
    title = title_entry.get()
    author = author_entry.get()

    if isbn and title and author:
        book = Book(isbn, title, author)
        library.add_book(book)
        clear_entries()
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def remove_book():
    isbn = isbn_entry.get()
    if isbn:
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to remove this book?")
        if confirmation:
            library.remove_book(isbn)
            clear_entries()
    else:
        messagebox.showerror("Error", "Please enter the ISBN of the book to remove.")

def display_books():
    library.display_books()

def clear_entries():
    isbn_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Library Management System")

# Create library instance
library = Library()

# Labels and entries
tk.Label(root, text="ISBN:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
isbn_entry = tk.Entry(root, font=("Helvetica", 12))
isbn_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Title:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=10, pady=5)
title_entry = tk.Entry(root, font=("Helvetica", 12))
title_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Author:", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", padx=10, pady=5)
author_entry = tk.Entry(root, font=("Helvetica", 12))
author_entry.grid(row=2, column=1, padx=10, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Book", font=("Helvetica", 12), command=add_book)
add_button.grid(row=3, column=0, columnspan=2, pady=5)

remove_button = tk.Button(root, text="Remove Book", font=("Helvetica", 12), command=remove_book)
remove_button.grid(row=4, column=0, columnspan=2, pady=5)

display_button = tk.Button(root, text="Display Available Books", font=("Helvetica", 12), command=display_books)
display_button.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
