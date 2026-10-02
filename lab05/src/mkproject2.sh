#!/usr/bin/bash
set -x

# mkproject2.sh - 입력받은 이름으로 새 폴더를 생성하는 스크립트
# 인자가 없거나 같은 이름의 폴더가 이미 존재하면 오류 메시지를 출력하고 종료한다.


if [ -z "$1" ]
then
    echo "사용법: $0 <폴더이름>"
    exit 1
fi

NAME=$1

if [ -d "$NAME" ]
then
    echo "오류: $NAME 폴더가 이미 존재합니다"
    exit 1
fi

NAME=$1
mkdir $NAME
echo "$NAME 폴더를 만들었습니다"
ls -l "$NAME"




