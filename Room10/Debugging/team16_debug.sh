#!/bin/bash

awk -F'[ =]+' '
{
  ip=$2
  action=$4

  if (action=="FAILED") failed[ip]++
  else if (action=="SUCCESS") success[ip]++   # fixed
  else if (action=="DENIED") denied[ip]++     # fixed

  ips[ip]=1   # track all IPs
}
END {
  for (i in ips) {
    printf "%s %d %d %d\n", i, failed[i]+0, success[i]+0, denied[i]+0
  }
}
' "$1" | sort -k2 -nr
