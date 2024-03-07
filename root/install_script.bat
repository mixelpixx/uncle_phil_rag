@echo off
setlocal

:: Check if Python is installed
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found. Please install Python and rerun this script.
    exit /b
)

:: Install necessary Python packages
python -m pip install --upgrade pip
python -m pip install flask flask_cors openai chromadb

:: Set PATH variable
set PATH=%PATH%;%~dp0

:: Run the Flask server
python main.py