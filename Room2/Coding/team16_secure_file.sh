#!/bin/bash

# Check if a filename was provided
if [ -z "$1" ]; then
    echo "Usage: $0 filename"
    exit 1
fi

FILE="$1"

# Create the file if it doesn't exist
if [ ! -e "$FILE" ]; then
    touch "$FILE"
fi

# Set secure permissions (owner read/write only)
chmod 600 "$FILE"

# Print final permissions
ls -l "$FILE"