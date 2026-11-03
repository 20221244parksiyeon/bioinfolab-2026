#!/usr/bin/env python3
"""lab10/data/rbcL_*.gb 의 CDS를 table=11로 번역해 GenBank /translation과 비교한다.

사용법 (lab10 폴더에서):
    python3 src/check_cds.py                       # 화면에만 출력
    python3 src/check_cds.py doc/cds_check.tsv     # 화면 출력 + TSV 저장

GenBank 파일은 읽기만 하고 수정하지 않는다.
(read_fasta()는 FASTA 전용이라 GenBank 파싱에는 Biopython SeqIO를 사용한다.)
"""
import glob
import os
import sys

from Bio import SeqIO
from Bio.Data import CodonTable
from Bio.SeqFeature import AfterPosition, BeforePosition

TABLE = 11
START_CODONS = set(CodonTable.unambiguous_dna_by_id[TABLE].start_codons)
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
HEADER = ["file", "version", "organism", "cds_no", "location",
          "codon_start", "result"]


def is_5prime_partial(feature):
    """CDS의 5' 끝이 잘려 있는지(< 또는 >) 확인한다."""
    loc = feature.location
    if loc.strand == -1:
        return isinstance(loc.end, AfterPosition)
    return isinstance(loc.start, BeforePosition)


def translate_cds(feature, seq):
    """feature.extract로 CDS를 뽑아 codon_start를 반영해 번역한다."""
    cds = feature.extract(seq)
    codon_start = int(feature.qualifiers.get("codon_start", ["1"])[0])
    cds = cds[codon_start - 1:]
    cds = cds[: len(cds) // 3 * 3]          # 3의 배수가 아닌 꼬리는 버림
    protein = str(cds.translate(table=TABLE)).rstrip("*")  # 끝의 종결코돈 제거
    # 완전한 5' 끝의 시작 코돈(GTG, TTG 등)은 GenBank처럼 M으로 표기
    if (protein and not is_5prime_partial(feature)
            and str(cds[:3]).upper() in START_CODONS):
        protein = "M" + protein[1:]
    return protein, codon_start


def check_file(path):
    """한 GenBank 파일의 검사 결과 행 목록을 돌려준다."""
    rows = []
    name = os.path.basename(path)
    for rec in SeqIO.parse(path, "genbank"):
        version = rec.id
        organism = rec.annotations.get("organism", "NA")
        cds_list = [f for f in rec.features if f.type == "CDS"]
        if not cds_list:
            rows.append([name, version, organism, "-", "-", "-", "CDS 없음"])
            continue
        for i, feat in enumerate(cds_list, start=1):
            protein, codon_start = translate_cds(feat, rec.seq)
            if "translation" not in feat.qualifiers:
                result = "translation 없음"
            elif protein == feat.qualifiers["translation"][0]:
                result = "일치"
            else:
                result = "불일치"
            rows.append([name, version, organism, str(i), str(feat.location),
                         str(codon_start), result])
    return rows


def main():
    files = sorted(glob.glob(os.path.join(DATA_DIR, "rbcL_*.gb")))
    if not files:
        sys.exit("rbcL_*.gb 파일을 찾을 수 없습니다: " + DATA_DIR)

    lines = ["\t".join(HEADER)]
    for path in files:
        for row in check_file(path):
            lines.append("\t".join(row))

    text = "\n".join(lines) + "\n"
    sys.stdout.write(text)

    if len(sys.argv) > 1:                   # 출력 파일 경로가 주어지면 저장
        with open(sys.argv[1], "w", encoding="utf-8") as out:
            out.write(text)
        print(f"저장 완료: {sys.argv[1]}", file=sys.stderr)


if __name__ == "__main__":
    main()
