#!/bin/bash

echo "========================================"
echo "   🔐 Password Forge Launcher"
echo "========================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3 from https://python.org"
    exit 1
fi

# Check if requirements are installed
echo "Checking dependencies..."
if ! python3 -c "import pyperclip" &> /dev/null; then
    echo "Installing required packages..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ Error: Failed to install requirements"
        exit 1
    fi
fi

echo
echo "🚀 Starting Password Forge..."
echo

# Run the application
python3 app.py

# Check if there was an error
if [ $? -ne 0 ]; then
    echo
    echo "❌ Application exited with an error"
    read -p "Press Enter to continue..."
fi 