import tkinter as tk
from tkinter import ttk, messagebox
import os

class LibrarySystemGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the main window
        self.title("PUP Library System")
        self.geometry("1000x600")
        self.configure(bg="white")

        # Create header
        self.create_header()

        # Create main body
        self.create_main_body()

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

    def create_main_body(self):
        main_body = tk.Frame(self, bg="white")
        main_body.pack(fill=tk.BOTH, expand=True, pady=20)

        welcome_label = tk.Label(main_body, text="WELCOME TO PUP LIBRARY!", bg="white", fg="black", font=("Arial", 24, "bold"))
        welcome_label.pack(pady=20)

        cards_frame = tk.Frame(main_body, bg="white")
        cards_frame.pack()

        # Create cards
        self.create_card(cards_frame, "team.png", "Student Login", self.student_login)
        self.create_card(cards_frame, "books.png", "Reserve a Book", self.reserve_book)
        self.create_card(cards_frame, "notification.png", "News", self.news)

    def create_card(self, parent, image_path, text, command):
        card = tk.Frame(parent, bg="lightgray", width=200, height=250, relief=tk.RAISED, bd=2)
        card.pack(side=tk.LEFT, padx=20, pady=10)

        if os.path.exists(image_path):
            image = tk.PhotoImage(file=image_path)
            image = image.subsample(4, 4)  # Adjust to fit the card
            image_label = tk.Label(card, image=image, bg="lightgray")
            image_label.image = image  # Keep a reference to avoid garbage collection
            image_label.pack(pady=10)
        else:
            placeholder_label = tk.Label(card, text="[Image]", bg="lightgray", fg="black", font=("Arial", 16))
            placeholder_label.pack(pady=10)

        text_label = tk.Label(card, text=text, bg="lightgray", fg="black", font=("Arial", 14, "bold"))
        text_label.pack(pady=10)

        button = tk.Button(card, text="Go", command=command)
        button.pack(pady=10)

    def create_footer(self):
        footer_height = 30
        footer_frame = tk.Frame(self, bg="#890606", height=footer_height)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        footer_text = tk.Label(footer_frame, text="© 2024 All Rights Reserved", bg="#890606", fg="#F1C732", font=("Arial", 12))
        footer_text.pack(pady=5)


    def student_login(self):
        self.destroy()
        os.system("python LoginGUI.py")


    def reserve_book(self):
        self.destroy()
        os.system("python ReservationGUI.py")

    def news(self):
       messagebox.showinfo("Notif", "Hello Good Day, I have a news for you. This system is a friendly user! Enjoy")

if __name__ == "__main__":
    app = LibrarySystemGUI()
    app.mainloop()
