#!/bin/bash

grep "FAILED.*user=" "$1" | cut -d= -f2 | sort | uniq -c
