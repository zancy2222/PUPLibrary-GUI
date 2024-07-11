import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector
import os

class ReservationGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the main window
        self.title("Reservation - PUP Library System")
        self.geometry("1000x600")
        self.configure(bg="white")

        # Database connection
        self.conn = self.connect_to_db()
        self.cursor = self.conn.cursor()

        # Create header
        self.create_header()

        # Create main body for reservation
        self.create_reservation_body()

        # Create footer
        self.create_footer()

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
            messagebox.showerror("Database Error", f"Error: {err}")
            self.destroy()

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
        
        available_books_label = tk.Label(right_frame, text="Available Books", bg="#890606", fg="white", font=("Arial", 12), cursor="hand2")
        available_books_label.pack(side=tk.LEFT, padx=5)
        available_books_label.bind("<Button-1>", lambda e: self.available_books())
        
        home_label = tk.Label(right_frame, text="Home", bg="#890606", fg="white", font=("Arial", 12), cursor="hand2")
        home_label.pack(side=tk.LEFT, padx=5)
        home_label.bind("<Button-1>", lambda e: self.home())
        
    def my_books(self):
        self.destroy()
        os.system("python MyBook.py")
        
    def available_books(self):
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

    def create_reservation_body(self):
        # Frame for Make a Reservation section
        reservation_frame = tk.LabelFrame(self, text="Make a Reservation", padx=10, pady=10, bg="#F8F8F8", font=('Arial', 12, 'bold'))
        reservation_frame.place(relx=0.25, rely=0.3, width=500, height=220)

        # Reservation inputs
        tk.Label(reservation_frame, text="Type of Reservation:", bg="#F8F8F8", font=('Arial', 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.reservation_type = ttk.Combobox(reservation_frame, values=["BOOK"], state="readonly")
        self.reservation_type.grid(row=0, column=1, pady=5)

        tk.Label(reservation_frame, text="Book Title:", bg="#F8F8F8", font=('Arial', 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.book_title = ttk.Combobox(reservation_frame, values=[f"Book Title {i}" for i in range(1, 31)], state="readonly")
        self.book_title.grid(row=1, column=1, pady=5)

        tk.Label(reservation_frame, text="Date:", bg="#F8F8F8", font=('Arial', 10)).grid(row=2, column=0, sticky="w", pady=5)
        self.date_entry = DateEntry(reservation_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=2, column=1, pady=5)

        tk.Label(reservation_frame, text="Time:", bg="#F8F8F8", font=('Arial', 10)).grid(row=3, column=0, sticky="w", pady=5)
        self.time_entry = ttk.Entry(reservation_frame)
        self.time_entry.grid(row=3, column=1, pady=5)

        reserve_button = tk.Button(reservation_frame, text="RESERVE", bg="#890606", fg="white", font=('Arial', 10), command=self.reserve)
        reserve_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Frame for Current Reservation section
        self.current_reservation_frame = tk.LabelFrame(self, text="Current Reservation", padx=10, pady=10, bg="#F8F8F8", font=('Arial', 12, 'bold'))
        self.current_reservation_frame.place(relx=0.1, rely=0.55, width=450, height=180)

        # Frame for Summary of Reservation section
        self.summary_frame = tk.LabelFrame(self, text="Summary of Reservation", padx=10, pady=10, bg="#F8F8F8", font=('Arial', 12, 'bold'))
        self.summary_frame.place(relx=0.55, rely=0.55, width=400, height=180)

        # Summary details
        self.summary_label = tk.Label(self.summary_frame, text="**Details**", bg="#F8F8F8", font=('Arial', 10))
        self.summary_label.grid(row=0, column=0, pady=5)

        confirm_button = tk.Button(self.summary_frame, text="CONFIRM RESERVATION", bg="#FFD700", font=('Arial', 10), command=self.confirm_reservation)
        confirm_button.grid(row=1, column=0, pady=10)

    def reserve(self):
        reservation_type = self.reservation_type.get()
        book_title = self.book_title.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        # Display in Current Reservation
        reservation_details = f"{reservation_type}: {book_title} on {date} at {time}"
        tk.Label(self.current_reservation_frame, text=reservation_details, bg="#F8F8F8", font=('Arial', 10)).grid(sticky="w")

        # Display in Summary of Reservation
        self.summary_label.config(text=reservation_details)

    def confirm_reservation(self):
        reservation_type = self.reservation_type.get()
        book_title = self.book_title.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        try:
            sql = "INSERT INTO reservations (reservation_type, book_title, reservation_date, reservation_time) VALUES (%s, %s, %s, %s)"
            values = (reservation_type, book_title, date, time)
            self.cursor.execute(sql, values)
            self.conn.commit()
            messagebox.showinfo("Reservation Confirmation", "Reservation confirmed and saved to database.")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

if __name__ == "__main__":
    app = ReservationGUI()
    app.mainloop()
