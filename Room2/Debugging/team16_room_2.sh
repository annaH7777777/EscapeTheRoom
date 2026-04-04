#!/bin/bash

# Create the file if it doesn't exist
touch "$1"

# Set owner-only read/write permissions
chmod 600 "$1"

# Print final permissions
ls -l "$1"