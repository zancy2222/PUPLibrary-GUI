import tkinter as tk
from tkinter import ttk, messagebox
import os
import mysql.connector

class LoginGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the main window
        self.title("Login - PUP Library System")
        self.geometry("1000x600")
        self.configure(bg="white")

        # Database connection
        self.conn = self.connect_to_db()
        self.cursor = self.conn.cursor()

        # Create header
        self.create_header()

        # Create main body for login
        self.create_login_body()

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

    def login_user(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if email and password:
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            self.cursor.execute(query, (email, password))
            result = self.cursor.fetchone()

            if result:
                messagebox.showinfo("Login Success", "Welcome to the PUP Library System!")
                self.open_main_window()
            else:
                messagebox.showwarning("Login Failed", "Invalid email or password. Please register first.")
        else:
            messagebox.showwarning("Input Error", "Please fill in both email and password.")

    def open_main_window(self):
        self.destroy()
        os.system("python LibrarySystemGUI.py")  # Ensure MainWindow.py is in the same directory or provide the full path

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

        

    def create_login_body(self):
        login_body = tk.Frame(self, bg="white")
        login_body.pack(fill=tk.BOTH, expand=True, pady=50)

        # Left side (login form)
        login_form = tk.Frame(login_body, bg="white", width=500, height=400, relief="solid", bd=1)
        login_form.pack(side=tk.LEFT, padx=10, pady=10)
        login_form.pack_propagate(False)

        email_label = tk.Label(login_form, text="Email", bg="white", font=("Arial", 14))
        email_label.pack(pady=10)

        self.email_entry = tk.Entry(login_form, width=30, font=("Arial", 12))
        self.email_entry.pack(pady=5)

        password_label = tk.Label(login_form, text="Password", bg="white", font=("Arial", 14))
        password_label.pack(pady=10)

        self.password_entry = tk.Entry(login_form, show="*", width=30, font=("Arial", 12))
        self.password_entry.pack(pady=5)

        login_button = tk.Button(login_form, text="Login", bg="#890606", fg="#F1C732", width=10, font=("Arial", 12), command=self.login_user)
        login_button.pack(pady=20)

        # Right side (register link)
        right_side = tk.Frame(login_body, bg="#890606", width=500, height=400)
        right_side.pack(side=tk.RIGHT, padx=10, pady=10)
        right_side.pack_propagate(False)

        welcome_label = tk.Label(right_side, text="Welcome to\nPUP Library Log!", bg="#890606", fg="white", font=("Arial", 24, "bold"))
        welcome_label.pack(pady=50)

        register_label = tk.Label(right_side, text="Don't have an account?", bg="#890606", fg="white", font=("Arial", 14))
        register_label.pack(pady=10)

        register_button = tk.Button(right_side, text="Register", bg="#F1C732", fg="#890606", width=10, font=("Arial", 12), command=self.register_here)
        register_button.pack(pady=10)

    def create_footer(self):
        footer_height = 30
        footer_frame = tk.Frame(self, bg="#890606", height=footer_height)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        footer_text = tk.Label(footer_frame, text="© 2024 All Rights Reserved", bg="#890606", fg="#F1C732", font=("Arial", 12))
        footer_text.pack(pady=5)

    def my_books(self):
      messagebox.showwarning("Login Failed", "Please register first.")

    def register_here(self):
        self.destroy()
        os.system("python RegisterGUI.py")

if __name__ == "__main__":
    app = LoginGUI()
    app.mainloop()
