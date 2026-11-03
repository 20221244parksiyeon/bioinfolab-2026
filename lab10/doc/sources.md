# rbcL 서열 데이터 출처 및 검증 결과

| 파일 | VERSION | ORGANISM | 길이(bp) | 확인 방법 | 문제 |
|---|---|---|---:|---|---|
| rbcL_arabidopsis | OK432498.1 | Arabidopsis thaliana | 1440 | grep, fasta.py | UNVERIFIED, partial |
| rbcL_ginseng | - | - | - | Claude Code 검색 결과 | 다운로드 실패 |
| rbcL_rice | L24073.1 | Oryza sativa | 1355 | grep, fasta.py | mRNA 레코드 |
| rbcL_maize | Z11973.1 | Zea mays | 1431 | grep, fasta.py | 특이사항 없음 |
| rbcL_ginkgo | KF221173.1 | Ginkgo biloba | 1317 | grep, fasta.py | partial CDS |
| rbcL_pine | JQ512595.1 | Pinus thunbergii | 1428 | grep, fasta.py | 특이사항 없음 |
| rbcL_fern | MW620303.1 | Adiantum capillus-veneris | 1308 | grep, fasta.py | 특이사항 없음 |
| rbcL_liverwort | LC536762.1 | Marchantia polymorpha subsp. ruderalis | 1399 | grep, fasta.py | 요청 종의 아종 |

## 검증 결과

1. ORGANISM을 확인한 결과 7종 모두 요청한 종과 일치하거나 해당 종의 아종이었다.
2. 다운로드한 7개 서열은 모두 1300~1500 bp 범위에 해당하였다.
3. 각 FASTA 파일에는 서열이 1개씩 들어 있었다.
4. 인삼은 다운로드하지 못했으며, 애기장대와 벼 등 일부 레코드는 추가 검토가 필요하다.
5. FASTA 파일 7개를 합치면 총 7개의 서열이 된다.