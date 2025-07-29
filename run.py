#!/usr/bin/env python3
"""
Password Forge Launcher
Simple launcher script for the GUI application
"""

import sys
import os

def check_dependencies():
    """Check if all required dependencies are available"""
    try:
        import tkinter
        print("✓ Tkinter is available")
    except ImportError:
        print("❌ Error: Tkinter is not available")
        print("Please install Python with Tkinter support")
        return False
    
    try:
        import pyperclip
        print("✓ pyperclip is available")
    except ImportError:
        print("❌ Error: pyperclip is not installed")
        print("Please run: pip install pyperclip")
        return False
    
    return True

def main():
    """Main launcher function"""
    print("🔐 Password Forge Launcher")
    print("=" * 30)
    
    # Check dependencies
    if not check_dependencies():
        print("\nPlease fix the dependency issues and try again.")
        input("Press Enter to exit...")
        sys.exit(1)
    
    print("\n🚀 Starting Password Forge...")
    
    try:
        # Import and run the main application
        from app import root
        root.mainloop()
    except ImportError as e:
        print(f"❌ Error importing app.py: {e}")
        print("Make sure app.py is in the same directory as this script.")
        input("Press Enter to exit...")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main() 