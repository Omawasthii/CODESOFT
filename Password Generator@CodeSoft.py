import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 8:
            messagebox.showerror("Error", "Password length must be at least 8 characters.")
            return
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length.")

# Create a tkinter window
window = tk.Tk()
window.title("Password Generator")

# Label for password
password_label = tk.Label(window, text="Generated Password:", font=("Helvetica", 12))
password_label.pack(pady=10)

# Entry for displaying generated password
password_entry = tk.Entry(window, font=("Courier", 12), width=20)
password_entry.pack()

# Label and entry for password length
length_label = tk.Label(window, text="Password Length:", font=("Helvetica", 12))
length_label.pack()
length_entry = tk.Entry(window, font=("Helvetica", 12), width=10)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password, font=("Helvetica", 12))
generate_button.pack(pady=10)

# Start the tkinter main loop
window.mainloop()
