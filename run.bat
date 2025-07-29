@echo off
title Password Forge Launcher
echo.
echo ========================================
echo    🔐 Password Forge Launcher
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if requirements are installed
echo Checking dependencies...
python -c "import pyperclip" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ Error: Failed to install requirements
        pause
        exit /b 1
    )
)

echo.
echo 🚀 Starting Password Forge...
echo.

REM Run the application
python app.py

REM If there was an error, pause to show the message
if errorlevel 1 (
    echo.
    echo ❌ Application exited with an error
    pause
) 