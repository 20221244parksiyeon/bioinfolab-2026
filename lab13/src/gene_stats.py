import sys
import io
import contextlib

# parse_gff.py는 import될 때 맨 아래 코드(주석 개수 출력)도 같이 실행된다.
# 기존 파일을 고치지 않기 위해, import하는 동안만 출력을 숨긴다.
with contextlib.redirect_stdout(io.StringIO()):
    from parse_gff import read_gff

if len(sys.argv) < 2:
    print("사용법: python3 src/gene_stats.py <GFF 파일>")
    sys.exit(1)

features = read_gff(sys.argv[1])

# 1. type이 CDS인 주석만 추출
cds_list = []
for f in features:
    if f["type"] == "CDS":
        # 2. 길이 = end - start + 1
        f["length"] = f["end"] - f["start"] + 1
        cds_list.append(f)

if len(cds_list) == 0:
    print("CDS가 없습니다.")
    sys.exit(0)

# 3. 개수, 평균, 최소, 최대 길이
lengths = [c["length"] for c in cds_list]
count = len(lengths)
mean_len = sum(lengths) / count

print("== CDS 길이 통계 ==")
print("CDS 개수:", count)
print("평균 길이: %.1f bp" % mean_len)
print("최소 길이:", min(lengths), "bp")
print("최대 길이:", max(lengths), "bp")

# 4. 방향별 개수
plus = 0
minus = 0
for c in cds_list:
    if c["strand"] == "+":
        plus = plus + 1
    elif c["strand"] == "-":
        minus = minus + 1

print()
print("== 방향별 CDS 개수 ==")
print("정방향(+):", plus)
print("역방향(-):", minus)

# 5. 가장 긴 CDS 5개
longest = sorted(cds_list, key=lambda c: c["length"], reverse=True)[:5]

print()
print("== 가장 긴 CDS 5개 ==")
print("contig", "start", "end", "length", "strand", "attributes", sep="\t")
for c in longest:
    print(c["seqid"], c["start"], c["end"], c["length"], c["strand"],
          c["attributes"], sep="\t")

# 6. 평균 아미노산 개수 (평균 길이 / 3)
mean_aa = mean_len / 3

print()
print("== 평균 아미노산 개수 ==")
print("평균 아미노산 개수: %.1f aa" % mean_aa)
# 세균 단백질의 평균 길이는 대략 300 aa 정도로 알려져 있다.
# 여기서는 ±20%(240~360 aa) 안에 들면 '약 300개에 가깝다'고 판단한다.
if 240 <= mean_aa <= 360:
    print("→ 약 300 aa에 가깝습니다 (차이: %+.1f aa)" % (mean_aa - 300))
else:
    print("→ 300 aa에서 벗어납니다 (차이: %+.1f aa)" % (mean_aa - 300))
