import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length < 6:
        messagebox.showerror("Error", "Password length should be at least 6 characters.")
        return
    
    password_characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(password_characters) for _ in range(password_length))
    password_label.config(text="Generated Password: " + generated_password, font=("Arial", 16, "bold"))


root = tk.Tk()
root.title("Password Generator")
root.geometry("500x430")
root.configure(bg="white")

length_label = tk.Label(root, text="Enter Password Length:", font=("Arial", 14))
length_label.pack()
length_entry = tk.Entry(root, font=("Arial", 14))
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", font=("Arial", 14), command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="Generated Password:", font=("Arial", 16, "bold"))
password_label.pack()

root.mainloop()
