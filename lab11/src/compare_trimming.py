
import sys

def analyze_fastq(filename):
    lengths = []
    quality_sum = 0
    read_count = 0

    with open(filename) as f:
        while True:
            name = f.readline()
            if not name:
                break

            seq = f.readline().strip()
            plus = f.readline()
            qual = f.readline().strip()

            lengths.append(len(seq))
            scores = [ord(c) - 33 for c in qual]
            quality_sum += sum(scores) / len(scores)
            read_count += 1

    return {
        "count": read_count,
        "mean_length": sum(lengths) / read_count,
        "mean_quality": quality_sum / read_count,
        "min_length": min(lengths),
        "max_length": max(lengths)
    }

before = analyze_fastq(sys.argv[1])
after = analyze_fastq(sys.argv[2])

print("항목\t트리밍 전\t트리밍 후")

for key in before:
    print(f"{key}\t{before[key]:.2f}\t{after[key]:.2f}")
