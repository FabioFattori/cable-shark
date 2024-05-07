#!/bin/bash

# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo "Python is already installed."
else
    echo "Python is not installed. Installing Python 3.11..."
    # Install Python 3.11 using your package manager
    # Example for apt package manager (Ubuntu/Debian):
    sudo apt update
    sudo apt install python3.11
    echo "Python 3.11 installed successfully."
fi

# Get the current version of Python
PYTHON_VERSION=$(python3 --version | awk '{print $2}')

# Extract major and minor version numbers
MAJOR_VERSION=$(echo $PYTHON_VERSION | cut -d '.' -f 1)
MINOR_VERSION=$(echo $PYTHON_VERSION | cut -d '.' -f 2)

# Check if the major version is 3 and minor version is 11 or greater
if [ "$MAJOR_VERSION" -gt 3 ] || ([ "$MAJOR_VERSION" -eq 3 ] && [ "$MINOR_VERSION" -ge 11 ]); then
    echo "Python version is 3.11 or greater."
else
    echo "Updating Python to version 3.11..."
    # Install or update Python 3.11 using your package manager
    # Example for apt package manager (Ubuntu/Debian):
    sudo apt update
    sudo apt install python3.11
    echo "Python updated to version 3.11."
fi

cd Dependencies/
./dependencies.sh
cd ..

python3 main.py;