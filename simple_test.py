#!/usr/bin/env python3
"""
Simple test to debug password generation issue
"""

import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    """Simple password generation function"""
    print("Generate function called!")
    
    # Get values
    length = length_var.get()
    use_upper = upper_var.get()
    use_digits = digit_var.get()
    use_symbols = symbol_var.get()
    
    print(f"Length: {length}, Upper: {use_upper}, Digits: {use_digits}, Symbols: {use_symbols}")
    
    # Build character set
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    print(f"Character set length: {len(characters)}")
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated: {password}")
    
    # Set the password
    password_var.set(password)
    print("Password set in variable!")

# Create window
root = tk.Tk()
root.title("Simple Password Test")
root.geometry("400x300")

# Variables
length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()

# Create widgets
tk.Label(root, text="Password Length:").pack()
tk.Spinbox(root, from_=4, to=32, textvariable=length_var).pack()

tk.Checkbutton(root, text="Uppercase", variable=upper_var).pack()
tk.Checkbutton(root, text="Digits", variable=digit_var).pack()
tk.Checkbutton(root, text="Symbols", variable=symbol_var).pack()

# Generate button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

# Password display
tk.Label(root, text="Generated Password:").pack()
password_entry = tk.Entry(root, textvariable=password_var, font=("Courier", 12), width=30)
password_entry.pack(pady=5)

# Test button to check if variable is working
def test_var():
    print(f"Current password_var value: '{password_var.get()}'")
    messagebox.showinfo("Test", f"Password: {password_var.get()}")

tk.Button(root, text="Test Variable", command=test_var).pack(pady=5)

print("Starting simple test...")
root.mainloop() 