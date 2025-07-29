# 🔐 Password Forge

A modern, user-friendly password generator built with Python and Tkinter. Generate secure, customizable passwords with just a few clicks!

## ✨ Features

- **Customizable Password Length**: Generate passwords from 4 to 64 characters
- **Character Type Selection**: Choose to include:
  - Uppercase letters (A-Z)
  - Numbers (0-9)
  - Special symbols (!@#$%^&*)
- **One-Click Generation**: Generate secure passwords instantly
- **Copy to Clipboard**: Copy generated passwords with a single click
- **Modern GUI**: Clean, intuitive interface with status updates
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd password-forge
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

## 🚀 Usage

1. **Set Password Length**: Use the spinbox to set your desired password length (4-64 characters)

2. **Choose Character Types**: Check/uncheck the boxes for:
   - Uppercase letters
   - Numbers
   - Special symbols

3. **Generate Password**: Click the "🔧 Generate Password" button

4. **Copy Password**: Click "📋 Copy to Clipboard" to copy the password

5. **Clear**: Use "🗑️ Clear" to clear the password field

## 📋 Requirements

- `tkinter` - GUI framework (included with Python)
- `pyperclip` - Clipboard functionality
- `string` - String manipulation (built-in)
- `random` - Random number generation (built-in)

## 🎨 Features in Detail

### Password Generation
- Uses Python's `random` module for secure randomization
- Ensures at least one character type is selected
- Validates minimum password length (4 characters)
- Generates truly random passwords

### User Interface
- **Modern Design**: Clean, professional appearance
- **Status Bar**: Real-time feedback on actions
- **Responsive Layout**: Well-organized interface
- **Color-Coded Buttons**: Intuitive visual feedback

### Security Features
- **Read-only Password Display**: Prevents accidental modification
- **Input Validation**: Ensures valid settings before generation
- **Error Handling**: User-friendly error messages

## 🔧 Customization

You can easily customize the application by modifying `app.py`:

- **Colors**: Change the color scheme by modifying hex values
- **Fonts**: Adjust font families and sizes
- **Window Size**: Modify the geometry settings
- **Default Values**: Change initial settings for length and character types

## 📱 Screenshots

The application features:
- Clean, modern interface
- Intuitive controls
- Status feedback
- Professional styling

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests
- Improving documentation

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

### Common Issues

1. **Import Error for pyperclip**
   ```bash
   pip install pyperclip
   ```

2. **Tkinter not found**
   - On Ubuntu/Debian: `sudo apt-get install python3-tk`
   - On CentOS/RHEL: `sudo yum install tkinter`
   - On macOS: Tkinter is usually included with Python

3. **Clipboard not working**
   - Ensure you have the necessary permissions
   - Try running as administrator (Windows)
   - Check if your system supports clipboard operations

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Review the error messages in the application
3. Ensure all dependencies are properly installed

---

**Happy Password Generating! 🔐✨** 