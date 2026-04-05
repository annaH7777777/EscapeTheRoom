#!/bin/bash

# Check input
if [ -z "$1" ]; then
    echo "Usage: $0 log.txt"
    exit 1
fi

logfile="$1"

# Print matching lines
grep -E "FAILED|DENIED" "$logfile"

# Count and print total
count=$(grep -E "FAILED|DENIED" "$logfile" | wc -l)
echo "Total suspicious entries: $count"