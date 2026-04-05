#!/bin/bash

grep -E "FAILED|DENIED" "$1"
grep -E "FAILED|DENIED" "$1" | wc -l > count.txt
echo "Total suspicious entries: $(cat count.txt)"