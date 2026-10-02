#!/usr/bin/bash
# batchinfo.sh - 폴더 안의 FASTA 파일 정보를 출력한다

DIR="$1"

if [ ! -d "$DIR" ]
then
    echo "오류: 폴더를 찾을 수 없습니다: $DIR"
    exit 1
fi

echo -e "file\tcount"

for f in "$DIR"/*.fasta
do
    if [ ! -f "$f" ]
    then
        continue
    fi

    echo -e "$(basename "$f")\t$(grep -c ">" "$f")"
done