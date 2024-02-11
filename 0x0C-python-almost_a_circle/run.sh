#!/bin/bash

# Run all Python files in the current directory
for file in ./*.py; do
    if [ -f "$file" ]; then
	echo "*****************************"
	echo "*********** $file ***********"
	echo "*****************************"
        chmod +x "$file"  # Make the script executable if not already
        "$file"
    fi
done