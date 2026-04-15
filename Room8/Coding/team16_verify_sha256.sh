#!/bin/bash

# Check if both arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <filename> <expected_sha256>"
    exit 1
fi

file="$1"
expected_hash="$2"

# Check if file exists
if [ ! -f "$file" ]; then
    echo "File not found"
    exit 1
fi

# Calculate actual SHA-256 hash
actual_hash=$(sha256sum "$file" | awk '{print $1}')

# Compare hashes
if [ "$actual_hash" = "$expected_hash" ]; then
    echo "OK"
else
    echo "MISMATCH"
fi
