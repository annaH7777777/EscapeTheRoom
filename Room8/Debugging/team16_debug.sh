#!/bin/bash

CALC=$(sha256sum "$1" | cut -d' ' -f1)
EXPECTED="$2"

if [ "$CALC" = "$EXPECTED" ]; then
  echo "OK"
else
  echo "MISMATCH"
fi
