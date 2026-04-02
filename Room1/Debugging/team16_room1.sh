#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "Error: File not found."
    exit 1
fi

cat "$1"