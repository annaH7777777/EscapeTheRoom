#!/bin/bash

# Check input
if [ -z "$1" ]; then
  echo "Usage: $0 <logfile>"
  exit 1
fi

awk -F'[ =]+' '
{
  ip=$2
  action=$4

  if (action=="FAILED") failed[ip]++
  else if (action=="SUCCESS") success[ip]++
  else if (action=="DENIED") denied[ip]++

  ips[ip]=1
}
END {
  for (i in ips) {
    printf "%s %d %d %d\n", i, failed[i]+0, success[i]+0, denied[i]+0
  }
}
' "$1" | sort -k2 -nr
