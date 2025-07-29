#!/usr/bin/env python3
"""
Simple GUI test to verify Tkinter is working
"""

import tkinter as tk
from tkinter import messagebox

def test_gui():
    """Test basic GUI functionality"""
    print("Creating test window...")
    
    # Create a simple test window
    root = tk.Tk()
    root.title("GUI Test - Password Forge")
    root.geometry("300x200")
    root.configure(bg="#f0f0f0")
    
    # Add a label
    label = tk.Label(
        root, 
        text="🔐 Password Forge\nGUI Test Successful!", 
        font=("Helvetica", 14, "bold"),
        bg="#f0f0f0",
        fg="#2c3e50"
    )
    label.pack(pady=50)
    
    # Add a button
    def show_message():
        messagebox.showinfo("Success", "GUI is working perfectly!")
    
    button = tk.Button(
        root,
        text="Test Button",
        command=show_message,
        bg="#27ae60",
        fg="white",
        font=("Helvetica", 12),
        width=15
    )
    button.pack(pady=20)
    
    print("GUI window should now be visible!")
    print("If you can see the window, the GUI is working correctly.")
    print("Close the window to continue...")
    
    # Start the GUI
    root.mainloop()
    
    print("GUI test completed!")

if __name__ == "__main__":
    test_gui() 