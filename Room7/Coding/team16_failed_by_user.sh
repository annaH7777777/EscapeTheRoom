#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <directory_path>"
  exit 1
fi

if [ ! -d "$1" ]; then
  echo "Error: Directory does not exist"
  exit 1
fi

find "$1" -type f -perm -o=w -print
