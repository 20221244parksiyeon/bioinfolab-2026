
import sys

def read_fastq(filename):
    records = []
    with open(filename) as f:
        lines = f.readlines()

    for i in range(0, len(lines), 4):
        name = lines[i].rstrip()[1:]
        seq = lines[i + 1].rstrip().upper()
        qual = lines[i + 3].rstrip()
        records.append((name, seq, qual))

    return records


def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    atgc = sum(seq.count(base) for base in "ATGC")
    if atgc == 0:
        return 0
    return gc / atgc * 100


def mean_quality(qual):
    scores = [ord(ch) - 33 for ch in qual]
    return sum(scores) / len(scores)


reads = read_fastq(sys.argv[1])

high_gc = []
low_gc = []

for name, seq, qual in reads:
    gc = gc_content(seq)
    q = mean_quality(qual)

    if gc >= 50:
        high_gc.append(q)
    else:
        low_gc.append(q)


print("전체 read 개수:", len(reads))

print("GC 비율 높은 read 수:", len(high_gc))
print("GC 비율 낮은 read 수:", len(low_gc))

if high_gc:
    print("GC 높은 그룹 평균 품질:",
          sum(high_gc) / len(high_gc))

if low_gc:
    print("GC 낮은 그룹 평균 품질:",
          sum(low_gc) / len(low_gc))

if high_gc and low_gc:
    diff = (sum(high_gc) / len(high_gc)
            - sum(low_gc) / len(low_gc))
    print("평균 품질 차이 (높음 - 낮음):", diff)
