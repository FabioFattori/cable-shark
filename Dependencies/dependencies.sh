#!/bin/bash

# Check if requirements.txt file exists
if [ ! -f requirements.txt ]; then
    echo "requirements.txt file not found."
    exit 1
fi

# check if python3-pip is installed
if ! dpkg -l | grep -q python3-pip; then
    echo "python3-pip is not installed. Installing..."
    if sudo apt-get install python3-pip; then
        echo "python3-pip installed successfully."
    else
        echo "Failed to install python3-pip. Please install it manually."
        exit 1
    fi
else
    echo "python3-pip is already installed."
fi

# Read dependencies from requirements.txt
dependencies=$(cat requirements.txt)

# Loop through each dependency
for dep in $dependencies; do
    # Check if dependency is installed
    if ! python -c "import $dep" &> /dev/null; then
        echo "$dep is not installed. Installing..."
        # Attempt to install dependency using pip
        if pip install $dep; then
            echo "$dep installed successfully."
        else
            echo "Failed to install $dep. Please install it manually."
        fi
    else
        echo "$dep is already installed."
    fi
done

echo "Dependency check completed."
