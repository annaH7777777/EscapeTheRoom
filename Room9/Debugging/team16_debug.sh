#!/bin/bash

grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' "$1" | \
sort | uniq -c | sort -nr | head -3
