import tkinter as tk
from tkinter import ttk
import sqlite3

# 1. Database Initialization
DATABASE_NAME = 'customer_info.db'

def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birthday TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            preferred_contact TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_table()

# 2. GUI Design
root = tk.Tk()
root.title("Customer Information Form")

# Input fields
name_label = ttk.Label(root, text="Name:")
name_entry = ttk.Entry(root)

birthday_label = ttk.Label(root, text="Birthday (YYYY-MM-DD):")
birthday_entry = ttk.Entry(root)

email_label = ttk.Label(root, text="Email:")
email_entry = ttk.Entry(root)

phone_label = ttk.Label(root, text="Phone:")
phone_entry = ttk.Entry(root)

address_label = ttk.Label(root, text="Address:")
address_entry = ttk.Entry(root)

contact_label = ttk.Label(root, text="Preferred Contact:")
contact_options = ["Email", "Phone", "Mail"]
preferred_contact = tk.StringVar(root)
preferred_contact.set(contact_options[0])  # Set a default value
contact_dropdown = ttk.OptionMenu(root, preferred_contact, contact_options[0], *contact_options)

# Submit button function
def submit_data():
    name = name_entry.get()
    birthday = birthday_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    contact = preferred_contact.get()

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, birthday, email, phone, address, preferred_contact) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, birthday, email, phone, address, contact))
    conn.commit()
    conn.close()

    # Clear the form
    name_entry.delete(0, tk.END)
    birthday_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    preferred_contact.set(contact_options[0]) # Reset dropdown

submit_button = ttk.Button(root, text="Submit", command=submit_data)

# 3. GUI Layout (using grid)
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

birthday_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
birthday_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

phone_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
phone_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

address_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
address_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

contact_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
contact_dropdown.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

submit_button.grid(row=6, column=0, columnspan=2, pady=10)

# Configure column weights for resizing
root.grid_columnconfigure(1, weight=1)

# 4. Run the application
root.mainloop()
