#!/bin/bash
d
if [ -z "$1" ]; then
  echo "Usage: $0 <logfile>"
  exit 1
fi

# Extract IPs, count occurrences, sort, and show top 3
grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' "$1" \
| sort \
| uniq -c \
| sort -nr \
| head -n 3
