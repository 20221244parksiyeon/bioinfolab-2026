"""유전체 길이 대비 CDS 개수(유전자 밀도)와 코딩 밀도를 계산한다.

사용법: python3 src/gene_density.py data/contigs.fa doc/prokka_out/sample.gff
"""
import sys
import io
import os
import contextlib

# 랩 규칙: FASTA는 lab07/src/fasta.py의 read_fasta()를 재사용한다.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "lab07", "src"))
from fasta import read_fasta

if len(sys.argv) < 3:
    print("사용법: python3 src/gene_density.py <contigs.fa> <GFF 파일>")
    sys.exit(1)

fasta_file = sys.argv[1]
gff_file = sys.argv[2]

# parse_gff.py는 import될 때 맨 아래 코드(read_gff(sys.argv[1]) 후 출력)도 실행된다.
# 기존 파일을 고치지 않기 위해, import하는 동안만 sys.argv[1]을 GFF로 바꾸고 출력을 숨긴다.
saved_argv = sys.argv
sys.argv = [saved_argv[0], gff_file]
with contextlib.redirect_stdout(io.StringIO()):
    from parse_gff import read_gff
sys.argv = saved_argv

# 1. 전체 서열 길이
seqs = read_fasta(fasta_file)
genome_len = sum(len(s) for s in seqs.values())

# 2. CDS만 추출
features = read_gff(gff_file)
cds_list = [f for f in features if f["type"] == "CDS"]
cds_count = len(cds_list)

# 3. 1,000 bp당 CDS 개수
cds_per_kb = cds_count / genome_len * 1000

# 4. CDS 길이(end - start + 1) 총합
total_cds_len = sum(f["end"] - f["start"] + 1 for f in cds_list)

# 5. 코딩 밀도(%)
coding_density = total_cds_len / genome_len * 100

print("컨티그 수:", len(seqs))
print("전체 유전체 길이:", genome_len, "bp")
print("CDS 개수:", cds_count)
print("1,000 bp당 CDS 개수: %.3f" % cds_per_kb)
print("CDS 길이 총합:", total_cds_len, "bp")
print("평균 CDS 길이: %.1f bp" % (total_cds_len / cds_count if cds_count else 0))
print("코딩 밀도: %.2f %%" % coding_density)

# 6. 세균의 일반적인 범위(85~90%)와 비교
if 85 <= coding_density <= 90:
    print("판정: 세균의 일반적인 코딩 밀도 범위(85~90%) 안에 있다.")
elif coding_density < 85:
    print("판정: 일반적인 범위(85~90%)보다 낮다.")
else:
    print("판정: 일반적인 범위(85~90%)보다 높다.")
