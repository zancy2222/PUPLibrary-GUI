import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import os

class Header(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the main window
        self.title("PUP Library System")
        self.geometry("1000x600")
        self.configure(bg="white")

        # Create header
        self.create_header()

        # Create footer
        self.create_footer()

    def create_header(self):
        header_height = 50
        header_frame = tk.Frame(self, bg="#890606", height=header_height)
        header_frame.pack(fill=tk.X, side=tk.TOP)

        # Left side (logo and text)
        left_frame = tk.Frame(header_frame, bg="#890606")
        left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        logo_path = "PUPLogo.png"  # Update this to the full path if necessary
        if os.path.exists(logo_path):
            original_logo = tk.PhotoImage(file=logo_path)
            logo = original_logo.subsample(4, 4)  # Adjust the numbers to resize the logo
            logo_label = tk.Label(left_frame, image=logo, bg="#890606")
            logo_label.image = logo  # Keep a reference to avoid garbage collection
            logo_label.pack(side=tk.LEFT, padx=5)
        else:
            placeholder_label = tk.Label(left_frame, text="[Logo]", bg="#890606", fg="white", font=("Arial", 16))
            placeholder_label.pack(side=tk.LEFT, padx=5)

        lib_text = tk.Label(left_frame, text="PUP Library Log", bg="#890606", fg="white", font=("Arial", 16, "bold"))
        lib_text.pack(side=tk.LEFT, padx=5)

        # Right side (text, drop-down, search bar, user icon)
        right_frame = tk.Frame(header_frame, bg="#890606")
        right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        my_books_label = tk.Label(right_frame, text="My Books", bg="#890606", fg="white", font=("Arial", 12), cursor="hand2")
        my_books_label.pack(side=tk.LEFT, padx=5)
        my_books_label.bind("<Button-1>", lambda e: self.my_books())

        reservations_label = tk.Label(right_frame, text="Reservations", bg="#890606", fg="white", font=("Arial", 12), cursor="hand2")
        reservations_label.pack(side=tk.LEFT, padx=5)
        reservations_label.bind("<Button-1>", lambda e: self.reservations())

        student_logs_label = tk.Label(right_frame, text="Student Logs", bg="#890606", fg="white", font=("Arial", 12), cursor="hand2")
        student_logs_label.pack(side=tk.LEFT, padx=5)
        student_logs_label.bind("<Button-1>", lambda e: self.student_logs())
        
        student_logs_label = tk.Label(right_frame, text="Available Books", bg="#890606", fg="white", font=("Arial", 12), cursor="hand2")
        student_logs_label.pack(side=tk.LEFT, padx=5)
        student_logs_label.bind("<Button-1>", lambda e: self.AvailBooks())
        
        student_logs_label = tk.Label(right_frame, text="Home", bg="#890606", fg="white", font=("Arial", 12), cursor="hand2")
        student_logs_label.pack(side=tk.LEFT, padx=5)
        student_logs_label.bind("<Button-1>", lambda e: self.home())
        
        
    def my_books(self):
        self.destroy()
        os.system("python MyBook.py")
        
    def AvailBooks(self):
        self.destroy()
        os.system("python Header.py")    


    def reservations(self):
        self.destroy()
        os.system("python ReservationGUI.py")

    def home(self):
        self.destroy()
        os.system("python LibrarySystemGUI.py")
        
        
    def student_logs(self):
        self.destroy()
        os.system("python StudentLogGUI.py")

    def create_footer(self):
        footer_height = 30
        footer_frame = tk.Frame(self, bg="#890606", height=footer_height)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        footer_text = tk.Label(footer_frame, text="© 2024 All Rights Reserved", bg="#890606", fg="#F1C732", font=("Arial", 12))
        footer_text.pack(pady=5)



class LibraryGUI(Header):
    def __init__(self):
        super().__init__()

        # Create main body for library books
        self.create_library_body()

        # Database connection
        self.conn = self.connect_to_db()
        self.cursor = self.conn.cursor()

    def connect_to_db(self):
        try:
            conn = mysql.connector.connect(
                 host="localhost",
                user="root",
                password="",
                database="library_db"
            )
            return conn
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def create_library_body(self):
        library_body = tk.Frame(self, bg="white")
        library_body.pack(fill=tk.BOTH, expand=True, pady=20)

        columns = ("title", "author", "date_published", "isbn", "borrowed")
        self.tree = ttk.Treeview(library_body, columns=columns, show="headings", height=10)

        self.tree.heading("title", text="Book Title")
        self.tree.heading("author", text="Author")
        self.tree.heading("date_published", text="Date Published")
        self.tree.heading("isbn", text="ISBN")
        self.tree.heading("borrowed", text="Borrowed")

        self.tree.column("title", anchor=tk.CENTER, width=200)
        self.tree.column("author", anchor=tk.CENTER, width=150)
        self.tree.column("date_published", anchor=tk.CENTER, width=100)
        self.tree.column("isbn", anchor=tk.CENTER, width=150)
        self.tree.column("borrowed", anchor=tk.CENTER, width=100)

        # Sample data
        books = [
            ("Book 1", "Author 1", "2022-01-01", "1234567890"),
            ("Book 2", "Author 2", "2021-05-15", "0987654321"),
            ("Book 3", "Author 3", "2020-07-23", "1122334455"),
            ("Book 4", "Author 4", "2019-11-11", "9876543210"),
            ("Book 5", "Author 5", "2018-04-20", "5555555555"),
            ("Book 6", "Author 6", "2017-09-15", "6666666666"),
            ("Book 7", "Author 7", "2016-02-28", "7777777777"),
            ("Book 8", "Author 8", "2015-08-19", "8888888888"),
            ("Book 9", "Author 9", "2014-12-25", "9999999999"),
            ("Book 10", "Author 10", "2013-06-30", "0000000000"),
            ("Book 11", "Author 11", "2012-03-17", "1111111111"),
            ("Book 12", "Author 12", "2011-10-01", "2222222222"),
            ("Book 13", "Author 13", "2010-07-04", "3333333333"),
            ("Book 14", "Author 14", "2009-04-15", "4444444444"),
            ("Book 15", "Author 15", "2008-01-21", "5555555555"),
            ("Book 16", "Author 16", "2007-11-30", "6666666666"),
            ("Book 17", "Author 17", "2006-09-18", "7777777777"),
            ("Book 18", "Author 18", "2005-06-25", "8888888888"),
            ("Book 19", "Author 19", "2004-03-12", "9999999999"),
            ("Book 20", "Author 20", "2003-08-08", "0000000000"),
            ("Book 21", "Author 21", "2002-05-05", "1111111111"),
            ("Book 22", "Author 22", "2001-02-22", "2222222222"),
            ("Book 23", "Author 23", "2000-10-10", "3333333333"),
            ("Book 24", "Author 24", "1999-07-07", "4444444444"),
            ("Book 25", "Author 25", "1998-04-04", "5555555555"),
            ("Book 26", "Author 26", "1997-01-01", "6666666666"),
            ("Book 27", "Author 27", "1996-11-11", "7777777777"),
            ("Book 28", "Author 28", "1995-09-09", "8888888888"),
            ("Book 29", "Author 29", "1994-06-06", "9999999999"),
            ("Book 30", "Author 30", "1993-03-03", "0000000000"),
        ]

        for book in books:
            self.tree.insert("", tk.END, values=(*book, "Borrow"))

        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        borrow_button = ttk.Button(library_body, text="Borrow Selected", command=self.borrow_selected)
        borrow_button.pack(side=tk.BOTTOM, pady=10)

    def borrow_selected(self):
        selected_items = self.tree.selection()
        if not selected_items:
            return

        for item in selected_items:
            book_data = self.tree.item(item, "values")
            self.save_to_borrowed_books(book_data)

    def save_to_borrowed_books(self, book_data):
        try:
            sql = "INSERT INTO borrowed_books (title, author, date_published, isbn) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(sql, book_data[:4])
            self.conn.commit()
            messagebox.showwarning("Success", "Book Borrowed Successfuly.")
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")

if __name__ == "__main__":
    app = LibraryGUI()
    app.mainloop()
