#!/usr/bin/bash

declare -A COUNTS

for F in data/*.fasta
do
    NAME=$(basename "$F")
    COUNT=$(grep -c "^>" "$F")
    COUNTS["$NAME"]=$COUNT
done

echo "seqs.fasta의 서열 개수: ${COUNTS["seqs.fasta"]}"
echo "seqs2.fasta의 서열 개수: ${COUNTS["seqs2.fasta"]}"