
import sys

def read_fastq(filename):
    records = []
    with open(filename) as f:
        lines = f.readlines()

    for i in range(0, len(lines), 4):
        name = lines[i].rstrip()[1:]
        seq = lines[i + 1].rstrip()
        qual = lines[i + 3].rstrip()
        records.append((name, seq, qual))

    return records


reads = read_fastq(sys.argv[1])

# 각 위치의 품질 점수 합계와 read 개수
quality_sums = []
quality_counts = []

for name, seq, qual in reads:
    for i, char in enumerate(qual):

        # 새로운 위치가 나오면 저장 공간 추가
        if i >= len(quality_sums):
            quality_sums.append(0)
            quality_counts.append(0)

        # Phred+33 방식으로 품질 점수 계산
        score = ord(char) - 33

        quality_sums[i] += score
        quality_counts[i] += 1

# 위치별 평균 품질 점수 출력
print("위치\t평균 품질 점수\tRead 수")

for i in range(len(quality_sums)):
    mean = quality_sums[i] / quality_counts[i]
    print(f"{i + 1}\t{mean:.2f}\t{quality_counts[i]}")
