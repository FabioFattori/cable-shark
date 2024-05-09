@echo off

rem Get Python version
for /f "tokens=2 delims= " %%v in ('python --version 2^>^&1') do (
    set py_version=%%v
)

rem Extract major and minor version numbers
for /f "tokens=1,2 delims=." %%a in ("%py_version%") do (
    set /a py_major_version=%%a
    set /a py_minor_version=%%b
)

rem Check if Python version is less than 3.11
if %py_major_version% leq 3 (
    if %py_minor_version% leq 10 (
        echo Python version is less than 3.11. Attempting to update...
        python -m pip install --upgrade python
        echo Python updated successfully.
    ) else (
        echo Python version is 3.11 or greater.
    )
) else (
    echo Python version is 3.11 or greater.
)

@echo off

REM Check if requirements.txt file exists
if not exist Dependencies/requirementsWindows.txt (
    echo Dependencies/requirementsWindows.txt file not found.
    exit /b 1
)

REM Read dependencies from requirements.txt
for /f %%i in (Dependencies/requirementsWindows.txt) do (
    REM Check if dependency is installed
    python -c "import %%i" >nul 2>&1
    if errorlevel 1 (
        echo %%i is not installed. Installing...
        REM Attempt to install dependency using pip
        pip install %%i
        if errorlevel 1 (
            echo Failed to install %%i. Please install it manually.
        ) else (
            echo %%i installed successfully.
        )
    ) else (
        echo %%i is already installed.
    )
)

echo Dependency check completed.

REM Start the main Python script
python main.py