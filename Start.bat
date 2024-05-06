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
