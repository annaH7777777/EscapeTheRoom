#!/bin/bash

if pgrep -x "$1" > /dev/null; then
  echo "RUNNING"
else
  echo "NOT RUNNING"
fi