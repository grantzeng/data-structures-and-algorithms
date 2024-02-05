#!/usr/bin/sh

for f in quicksort_*.py; do
    echo "<---------Running $f--------->"
    python3 "$f" 1>/dev/null
done