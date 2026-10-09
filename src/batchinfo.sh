#!/usr/bin/bash

for F in data/*.fasta
do
    NAME=$(basename "$F")
    COUNT=$(grep -c "^>" "$F")
    echo "$NAME:$COUNT"
done