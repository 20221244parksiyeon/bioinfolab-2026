#!/usr/bin/bash

FILE="$1"

echo "파일: $FILE"
echo "서열 개수: $(grep -c ">" "$FILE")"
echo "서열 이름:"
grep "^>" "$FILE" | cut -d ' ' -f 1 | tr -d '>'
echo "총 염기 수(대략): $(grep -v "^>" "$FILE" | tr -d '\n' | wc -c)"
