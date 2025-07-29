# 🚀 Password Forge - Quick Start Guide

## ⚡ Get Started in 3 Steps

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application

**Option A: GUI Version (Recommended)**
```bash
python app.py
```

**Option B: Command Line Version**
```bash
python cli.py
```

**Option C: Use Launcher Scripts**
- Windows: Double-click `run.bat`
- Linux/macOS: `./run.sh`

### 3. Generate Your First Password

**GUI:**
1. Set password length (4-64 characters)
2. Choose character types (uppercase, numbers, symbols)
3. Click "🔧 Generate Password"
4. Click "📋 Copy to Clipboard"

**CLI:**
```bash
# Default password (12 chars, all types)
python cli.py

# Custom length
python cli.py -l 16

# No symbols
python cli.py -l 8 --no-symbols

# Multiple passwords
python cli.py -c 5
```

## 🎯 Common Use Cases

### Strong Website Password
```bash
python cli.py -l 16
```

### Simple PIN (numbers only)
```bash
python cli.py -l 6 --no-uppercase --no-symbols
```

### Memorable Password (letters only)
```bash
python cli.py -l 12 --no-symbols
```

### Multiple Passwords
```bash
python cli.py -l 12 -c 10
```

## 🔧 Troubleshooting

**"Tkinter not found"**
- Windows: Usually included with Python
- Ubuntu: `sudo apt-get install python3-tk`
- macOS: Usually included with Python

**"pyperclip not found"**
```bash
pip install pyperclip
```

**GUI not opening**
- Try running `python run.py` for detailed error messages
- Check if Python and tkinter are properly installed

## 📱 Features at a Glance

- ✅ **Custom Length**: 4-64 characters
- ✅ **Character Types**: Uppercase, numbers, symbols
- ✅ **Copy to Clipboard**: One-click copying
- ✅ **Multiple Passwords**: Generate several at once (CLI)
- ✅ **Cross-Platform**: Windows, macOS, Linux
- ✅ **Modern GUI**: Clean, intuitive interface

## 🎨 GUI Screenshots

The application features:
- Clean, modern design
- Intuitive controls
- Real-time status updates
- Professional styling

---

**Ready to generate secure passwords? Start with `python app.py`! 🔐** 