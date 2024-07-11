import tkinter as tk
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os
class MyBook(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the main window
        self.title("My Borrowed Books - PUP Library System")
        self.geometry("1000x600")
        self.configure(bg="white")

        # Create header
        self.create_header()

        # Display borrowed books
        self.display_borrowed_books()

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

    def display_borrowed_books(self):
        try:
            # Connect to MySQL database
            connection = mysql.connector.connect(
                 host="localhost",
                user="root",
                password="",
                database="library_db"
            )

            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)

                # Query to retrieve borrowed books
                cursor = connection.cursor()
                cursor.execute("SELECT title, author, date_published, isbn FROM borrowed_books")
                records = cursor.fetchall()

                # Display borrowed books in a Treeview
                library_body = tk.Frame(self, bg="white")
                library_body.pack(fill=tk.BOTH, expand=True, pady=20)

                columns = ("title", "author", "date_published", "isbn")
                tree = ttk.Treeview(library_body, columns=columns, show="headings", height=10)

                tree.heading("title", text="Book Title")
                tree.heading("author", text="Author")
                tree.heading("date_published", text="Date Published")
                tree.heading("isbn", text="ISBN")

                tree.column("title", anchor=tk.CENTER, width=200)
                tree.column("author", anchor=tk.CENTER, width=150)
                tree.column("date_published", anchor=tk.CENTER, width=100)
                tree.column("isbn", anchor=tk.CENTER, width=150)

                for record in records:
                    tree.insert("", tk.END, values=record)

                tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                # Display total count of borrowed books
                total_count_label = tk.Label(library_body, text=f"Total Borrowed Books: {len(records)}", bg="white", fg="#890606", font=("Arial", 12, "bold"))
                total_count_label.pack(side=tk.BOTTOM, pady=10)

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            # Close database connection
            if connection.is_connected():
            
                print("MySQL connection is done")

if __name__ == "__main__":
    app = MyBook()
    app.mainloop()
