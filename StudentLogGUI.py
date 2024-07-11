import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import os

class StudentLogGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the main window
        self.title("Student Log - PUP Library System")
        self.geometry("1000x650")
        self.configure(bg="white")

        # Create header
        self.create_header()

        # Create main body for student log
        self.create_student_log_body()

        # Create footer
        self.create_footer()

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


    def create_student_log_body(self):
        # Frame for Student Log section
        student_log_frame = tk.LabelFrame(self, text="Student Log", padx=10, pady=10, bg="#F8F8F8", font=('Arial', 12, 'bold'))
        student_log_frame.place(x=20, y=150, width=960, height=200)

        # Student Log inputs
        profile_image_path = "user.png"  # Update this to the full path if necessary
        if os.path.exists(profile_image_path):
            original_profile_image = tk.PhotoImage(file=profile_image_path)
            profile_image = original_profile_image.subsample(8, 8)  # Adjust the numbers to resize the profile image
            profile_image_label = tk.Label(student_log_frame, image=profile_image, bg="#F8F8F8")
            profile_image_label.image = profile_image  # Keep a reference to avoid garbage collection
            profile_image_label.grid(row=0, column=0, rowspan=3, padx=10, pady=10)
        else:
            placeholder_label = tk.Label(student_log_frame, text="[Profile Image]", bg="#F8F8F8", fg="black", font=("Arial", 12))
            placeholder_label.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

        tk.Label(student_log_frame, text="Student ID:", bg="#F8F8F8", font=('Arial', 10)).grid(row=0, column=1, sticky="w", pady=5)
        self.student_id_entry = ttk.Entry(student_log_frame)
        self.student_id_entry.grid(row=0, column=2, pady=5)

        tk.Label(student_log_frame, text="Student Name:", bg="#F8F8F8", font=('Arial', 10)).grid(row=1, column=1, sticky="w", pady=5)
        self.student_name_entry = ttk.Entry(student_log_frame)
        self.student_name_entry.grid(row=1, column=2, pady=5)

        tk.Label(student_log_frame, text="Date:", bg="#F8F8F8", font=('Arial', 10)).grid(row=2, column=1, sticky="w", pady=5)
        self.date_entry = ttk.Entry(student_log_frame)
        self.date_entry.grid(row=2, column=2, pady=5)

        # Frame for Purpose of Visit section
        purpose_frame = tk.LabelFrame(self, text="Purpose of Visit", padx=10, pady=10, bg="#F8F8F8", font=('Arial', 12, 'bold'))
        purpose_frame.place(x=20, y=370, width=460, height=150)

        self.purpose_var = tk.StringVar()

        # Purpose of Visit options
        borrow_book_rb = tk.Radiobutton(purpose_frame, text="Borrow Book", variable=self.purpose_var, value="Borrow Book", bg="#F8F8F8", font=('Arial', 10), indicatoron=0)
        borrow_book_rb.grid(row=0, column=0, sticky="w", pady=5)

        return_book_rb = tk.Radiobutton(purpose_frame, text="Return Book", variable=self.purpose_var, value="Return Book", bg="#F8F8F8", font=('Arial', 10), indicatoron=0)
        return_book_rb.grid(row=1, column=0, sticky="w", pady=5)

        study_rb = tk.Radiobutton(purpose_frame, text="Study", variable=self.purpose_var, value="Study", bg="#F8F8F8", font=('Arial', 10), indicatoron=0)
        study_rb.grid(row=0, column=1, sticky="w", pady=5)

        others_rb = tk.Radiobutton(purpose_frame, text="Others: ", variable=self.purpose_var, value="Others", bg="#F8F8F8", font=('Arial', 10), indicatoron=0)
        others_rb.grid(row=1, column=1, sticky="w", pady=5)
        self.others_entry = ttk.Entry(purpose_frame)
        self.others_entry.grid(row=1, column=2, pady=5)

        # Frame for Duration of Visit section
        duration_frame = tk.LabelFrame(self, text="Duration of Visit", padx=10, pady=10, bg="#F8F8F8", font=('Arial', 12, 'bold'))
        duration_frame.place(x=500, y=370, width=460, height=150)

        # Duration details
        tk.Label(duration_frame, text="Time in:", bg="#F8F8F8", font=('Arial', 10)).grid(row=0, column=0, pady=5, sticky="w")
        self.time_in_entry = ttk.Entry(duration_frame)
        self.time_in_entry.grid(row=0, column=1, pady=5)

        tk.Label(duration_frame, text="Time out:", bg="#F8F8F8", font=('Arial', 10)).grid(row=1, column=0, pady=5, sticky="w")
        self.time_out_entry = ttk.Entry(duration_frame)
        self.time_out_entry.grid(row=1, column=1, pady=5)

        # Submit button
        submit_button = tk.Button(self, text="SUBMIT", bg="#890606", fg="white", font=('Arial', 12, 'bold'), command=self.submit_log)
        submit_button.place(x=450, y=550, width=100, height=40)

    def submit_log(self):
        # Retrieve data from entries
        student_id = self.student_id_entry.get()
        student_name = self.student_name_entry.get()
        date = self.date_entry.get()
        purpose = self.purpose_var.get()
        time_in = self.time_in_entry.get()
        time_out = self.time_out_entry.get()

        # Insert into database
        try:
            sql = "INSERT INTO student_logs (student_id, student_name, date, purpose, time_in, time_out) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (student_id, student_name, date, purpose, time_in, time_out)
            self.cursor.execute(sql, values)
            self.conn.commit()
            messagebox.showinfo("Success", "Student log entry added successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

if __name__ == "__main__":
    app = StudentLogGUI()
    app.mainloop()
