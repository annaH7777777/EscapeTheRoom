#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <logfile>"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "File not found: $1"
    exit 1
fi

grep "FAILED" "$1" | \
sed -E 's/.*user=([^ ]+).*/\1/' | \
sort | uniq -c | \
awk '{print $2, $1}'
