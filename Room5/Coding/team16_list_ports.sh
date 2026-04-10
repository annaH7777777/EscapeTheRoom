#!/bin/bash

ss -lntup | awk 'NR>1 {
  split($5, a, ":")
  port=a[length(a)]
  proto=$1
  # only print if port is numeric
  if (port ~ /^[0-9]+$/) {
    print port, proto
  }
}'