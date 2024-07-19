import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    if length < 8:
        messagebox.showerror("Error", "Password length should be at least 8 characters.")
        return
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Success", "Password copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=lambda: generate_password(int(length_entry.get())))
generate_button.pack()

password_entry = tk.Entry(root, width=40)
password_entry.pack()

copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.pack()

root.mainloop()
