import tkinter as tk
from tkinter import ttk
import os
import mysql.connector
from tkinter import messagebox

class RegisterGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the main window
        self.title("Register - PUP Library System")
        self.geometry("1000x900")
        self.configure(bg="white")

        # Database connection
        self.conn = self.connect_to_db()
        self.cursor = self.conn.cursor()

        # Create header
        self.create_header()

        # Create main body for registration
        self.create_registration_body()

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

    def register_user(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        middle_name = self.middle_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        program = self.program_entry.get()
        year = self.year_entry.get()
        section = self.section_entry.get()

        if all([first_name, last_name, middle_name, email, password, program, year, section]):
            query = ("INSERT INTO users (first_name, last_name, middle_name, email, password, program, year, section) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
            values = (first_name, last_name, middle_name, email, password, program, year, section)

            try:
                self.cursor.execute(query, values)
                self.conn.commit()
                messagebox.showinfo("Success", "User registered successfully!")
                self.clear_entries()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")

    def clear_entries(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.middle_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.program_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.section_entry.delete(0, tk.END)

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

    def create_registration_body(self):
        registration_body = tk.Frame(self, bg="white")
        registration_body.pack(fill=tk.BOTH, expand=True, pady=50)

        # Left side (registration form)
        register_form = tk.Frame(registration_body, bg="white", width=500, height=700, relief="solid", bd=1)
        register_form.pack(side=tk.LEFT, padx=10, pady=10)
        register_form.pack_propagate(False)

        self.first_name_entry = self.create_entry(register_form, "First Name")
        self.last_name_entry = self.create_entry(register_form, "Last Name")
        self.middle_name_entry = self.create_entry(register_form, "Middle Name")
        self.email_entry = self.create_entry(register_form, "Email")
        self.password_entry = self.create_entry(register_form, "Password", show="*")
        self.program_entry = self.create_entry(register_form, "Program")
        self.year_entry = self.create_entry(register_form, "Year")
        self.section_entry = self.create_entry(register_form, "Section")

        register_button = tk.Button(register_form, text="Register", bg="#890606", fg="#F1C732", width=10, font=("Arial", 12), command=self.register_user)
        register_button.pack(pady=20)

        # Right side (welcome message)
        right_side = tk.Frame(registration_body, bg="#890606", width=500, height=400)
        right_side.pack(side=tk.RIGHT, padx=10, pady=10)
        right_side.pack_propagate(False)

        welcome_label = tk.Label(right_side, text="Join the\nPUP Library!", bg="#890606", fg="white", font=("Arial", 24, "bold"))
        welcome_label.pack(pady=50)

        login_label = tk.Label(right_side, text="Already have an account?", bg="#890606", fg="white", font=("Arial", 14))
        login_label.pack(pady=10)

        login_button = tk.Button(right_side, text="Login", bg="#F1C732", fg="#890606", width=10, font=("Arial", 12), command=self.logins_here)
        login_button.pack(pady=10)

    def create_footer(self):
        footer_height = 30
        footer_frame = tk.Frame(self, bg="#890606", height=footer_height)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        footer_text = tk.Label(footer_frame, text="© 2024 All Rights Reserved", bg="#890606", fg="#F1C732", font=("Arial", 12))
        footer_text.pack(pady=5)

    def my_books(self):
      messagebox.showwarning("Login Failed", "Please register first.")

    def create_entry(self, parent, label_text, show=None):
        label = tk.Label(parent, text=label_text, bg="white", font=("Arial", 14))
        label.pack(pady=5)
        entry = tk.Entry(parent, width=30, font=("Arial", 12), show=show)
        entry.pack(pady=5)
        return entry
    
    def logins_here(self):
        self.destroy()
        os.system("python LoginGUI.py")

if __name__ == "__main__":
    app = RegisterGUI()
    app.mainloop()
