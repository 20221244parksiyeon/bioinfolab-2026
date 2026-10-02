#!/usr/bin/bash

FILE=$1
MIN=$2

# 인자가 정확히 2개인지 확인
if [ $# -ne 2 ]; then
    echo "사용법: $0 <FASTA파일> <최소길이>"
    exit 1
fi

# 입력한 파일이 존재하는지 확인
if [ ! -f "$FILE" ]; then
    echo "오류: 파일을 찾을 수 없습니다: $FILE"
    exit 1
fi

# 두 번째 인자가 숫자인지 확인
if ! [[ "$MIN" =~ ^[0-9]+$ ]]; then
    echo "오류: 최소길이는 숫자여야 합니다."
    exit 1
fi

# 헤더를 제외하고 최소 길이보다 짧은 서열 줄의 개수를 계산
COUNT=$(grep -v "^>" "$FILE" | awk -v min="$MIN" 'length($0) < min {count++} END {print count+0}')

echo "$MIN 보다 짧은 서열 줄은 $COUNT 개입니다."