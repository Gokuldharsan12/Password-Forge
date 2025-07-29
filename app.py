import tkinter as tk
from tkinter import ttk, messagebox
import string
import random
import pyperclip

def generate_password():
    length = length_var.get()
    use_upper = upper_var.get()
    use_digits = digit_var.get()
    use_symbols = symbol_var.get()

    if length < 4:
        messagebox.showerror("Error", "Password length must be at least 4")
        return

    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)
    print(f"[DEBUG] Generated password: {password}")

    password_entry.update_idletasks()
    password_entry.focus_set()
    password_entry.select_range(0, tk.END)
    password_entry.config(bg="#d5f4e6")
    root.after(500, lambda: password_entry.config(bg="#ffffff"))

    password_status_label.config(text="✅ Password generated successfully!", fg="#27ae60")
    root.lift()
    root.attributes('-topmost', True)
    root.attributes('-topmost', False)

def copy_to_clipboard():
    password = password_var.get()
    if password:
        try:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy to clipboard: {e}")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

def clear_password():
    password_var.set("")
    password_status_label.config(text="Click 'Generate Password' to create a new password", fg="#7f8c8d")

def toggle_password_visibility():
    if password_entry.cget('show') == "":
        password_entry.config(show="*")
        eye_button.config(text="👁️")
    else:
        password_entry.config(show="")
        eye_button.config(text="🙈")

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Forge")
root.geometry("450x420")
root.configure(bg="#f5f5f5")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')

# Title
tk.Label(
    root, text="🔐 Password Forge",
    font=("Helvetica", 20, "bold"),
    bg="#f5f5f5", fg="#2c3e50"
).pack(pady=15)

# Variables
length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()

# Main frame
main_frame = tk.Frame(root, bg="#f5f5f0", relief="raised", bd=2)
main_frame.pack(pady=10, padx=20, fill="both", expand=True)

# Settings frame
settings_frame = tk.Frame(main_frame, bg="#f5f5f0")
settings_frame.pack(pady=15, padx=20, fill="x")

# Password Length
length_frame = tk.Frame(settings_frame, bg="#f5f5f0")
length_frame.pack(fill="x", pady=5)

tk.Label(length_frame, text="Password Length:", bg="#f5f5f0", font=("Helvetica", 12, "bold"), fg="#34495e").pack(side="left")
tk.Spinbox(length_frame, from_=4, to=64, textvariable=length_var, font=("Helvetica", 12), width=8, relief="sunken", bd=2).pack(side="right", padx=(10, 0))

# Checkboxes
checkbox_frame = tk.Frame(settings_frame, bg="#f5f5f0")
checkbox_frame.pack(fill="x", pady=10)

tk.Checkbutton(checkbox_frame, text="Include Uppercase Letters (A-Z)", variable=upper_var, bg="#f5f5f0", font=("Helvetica", 11), fg="#2c3e50", selectcolor="#ecf0f1").pack(anchor="w", pady=3)
tk.Checkbutton(checkbox_frame, text="Include Numbers (0-9)", variable=digit_var, bg="#f5f5f0", font=("Helvetica", 11), fg="#2c3e50", selectcolor="#ecf0f1").pack(anchor="w", pady=3)
tk.Checkbutton(checkbox_frame, text="Include Symbols (!@#$%^&*)", variable=symbol_var, bg="#f5f5f0", font=("Helvetica", 11), fg="#2c3e50", selectcolor="#ecf0f1").pack(anchor="w", pady=3)

# Generate Button
tk.Button(main_frame, text="🔧 Generate Password", command=generate_password, bg="#27ae60", fg="white", font=("Helvetica", 12, "bold"), width=20, relief="raised", bd=2, cursor="hand2").pack(pady=5)

# Password display
password_frame = tk.Frame(main_frame, bg="#f5f5f0")
password_frame.pack(pady=10, fill="x", padx=20)

tk.Label(password_frame, text="Generated Password:", bg="#f5f5f0", font=("Helvetica", 11, "bold"), fg="#34495e").pack(anchor="w", pady=(0, 5))

# Entry + Eye Button Frame
password_entry_frame = tk.Frame(password_frame, bg="#f5f5f0")
password_entry_frame.pack(fill="x")

password_entry = tk.Entry(
    password_entry_frame, textvariable=password_var,
    font=("Courier", 18, "bold"), justify="center",
    bd=2, relief="groove", bg="#ffffff", fg="#2c3e50",
    show="*"
)
password_entry.pack(side="left", fill="x", expand=True, ipady=10)

eye_button = tk.Button(
    password_entry_frame,
    text="👁️",
    command=toggle_password_visibility,
    bg="#ffffff", relief="flat",
    font=("Helvetica", 12),
    cursor="hand2"
)
eye_button.pack(side="right", padx=5)

# Info Label
password_status_label = tk.Label(password_frame, text="Click 'Generate Password' to create a new password", bg="#f5f5f0", font=("Helvetica", 9), fg="#7f8c8d")
password_status_label.pack(anchor="w", pady=(2, 0))

# Buttons frame
action_frame = tk.Frame(main_frame, bg="#f5f5f0")
action_frame.pack(pady=10)

tk.Button(action_frame, text="📋 Copy to Clipboard", command=copy_to_clipboard, bg="#3498db", fg="white", font=("Helvetica", 11, "bold"), relief="raised", bd=2, cursor="hand2").pack(side="left", padx=5)
tk.Button(action_frame, text="🗑️ Clear", command=clear_password, bg="#e74c3c", fg="white", font=("Helvetica", 11, "bold"), relief="raised", bd=2, cursor="hand2").pack(side="left", padx=5)

# Status bar
status_frame = tk.Frame(root, bg="#34495e", height=25)
status_frame.pack(side="bottom", fill="x")
status_frame.pack_propagate(False)

status_label = tk.Label(status_frame, text="Ready to generate passwords", bg="#34495e", fg="white", font=("Helvetica", 9))
status_label.pack(side="left", padx=10, pady=5)

# Start app
root.mainloop()
