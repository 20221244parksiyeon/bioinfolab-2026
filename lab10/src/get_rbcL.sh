#!/bin/bash
# 식물 8종의 rbcL 서열을 NCBI E-utilities(wget)로 받는 스크립트
# 사용법: cd lab10 && bash src/get_rbcL.sh
BASE="https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
OUT="data"

while IFS='|' read -r SPECIES NAME; do
    # 검색어 URL 인코딩: 공백 -> +, " -> %22, [ ] -> %5B %5D
    Q=$(echo "$SPECIES" | sed 's/ /+/g')
    TERM="%22${Q}%22%5BOrganism%5D+AND+rbcL%5BGene%5D+AND+1300:1500%5BSLEN%5D"

    # 1) esearch: 첫 번째 ID만
    ID=$(wget -q -O - "$BASE/esearch.fcgi?db=nuccore&term=${TERM}&retmax=1" \
         | grep -o '<Id>[0-9]*</Id>' | head -1 | sed 's/<[^>]*>//g')
    sleep 1

    if [ -z "$ID" ]; then
        echo "[경고] $SPECIES: 검색 결과 없음" >&2
        continue
    fi
    echo "$SPECIES -> ID $ID -> $NAME"

    # 2) FASTA
    wget -q -O "$OUT/${NAME}.fa" "$BASE/efetch.fcgi?db=nuccore&id=${ID}&rettype=fasta&retmode=text"
    sleep 1

    # 3) GenBank
    wget -q -O "$OUT/${NAME}.gb" "$BASE/efetch.fcgi?db=nuccore&id=${ID}&rettype=gb&retmode=text"
    sleep 1
done <<'EOF'
Arabidopsis thaliana|rbcL_arabidopsis
Panax ginseng|rbcL_ginseng
Oryza sativa|rbcL_rice
Zea mays|rbcL_maize
Ginkgo biloba|rbcL_ginkgo
Pinus thunbergii|rbcL_pine
Adiantum capillus-veneris|rbcL_fern
Marchantia polymorpha|rbcL_liverwort
EOF
