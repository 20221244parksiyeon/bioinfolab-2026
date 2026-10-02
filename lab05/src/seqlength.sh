#!/usr/bin/bash

CURRENT=""
LENGTH=0

while read LINE
do
    if [[ "$LINE" == ">"* ]]; then
        if [ -n "$CURRENT" ]; then
            echo "$CURRENT : $LENGTH"
        fi

        CURRENT="$LINE"
        LENGTH=0
    else
        LENGTH=$((LENGTH + ${#LINE}))
    fi
done < "$1"

if [ -n "$CURRENT" ]; then
    echo "$CURRENT : $LENGTH"
fi