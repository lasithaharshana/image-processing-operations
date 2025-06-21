@echo off
REM run_image_processing.bat

echo ===== IMAGE PROCESSING OPERATIONS =====
echo.

REM Check if Python is installed
python --version > nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in your PATH.
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Install required packages
echo Installing required packages...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error installing packages. Please check your internet connection.
    pause
    exit /b 1
)
echo Packages installed successfully.
echo.

REM Create directories if they don't exist
if not exist "input" mkdir input
if not exist "output" mkdir output

REM Check for input image
if not exist "input\sample_image.jpg" (
    echo WARNING: No sample image found.
    echo Please place an image file named 'sample_image.jpg' in the 'input' folder.
    echo.
    pause
    exit /b 1
)

REM Run the main program
echo Starting image processing...
cd src
python main.py

echo.
echo Program execution completed.
pause
