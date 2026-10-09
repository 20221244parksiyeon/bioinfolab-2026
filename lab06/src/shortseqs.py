import sys

if len(sys.argv) < 3:
    print("사용법: python3 src/shortseqs.py <FASTA파일> <최소길이>")
    sys.exit(1)

filename = sys.argv[1]
min_text = sys.argv[2]

if not min_text.isdigit():
    print("오류: 최소 길이는 숫자여야 합니다.")
    sys.exit(1)

min_length = int(min_text)

lengths = []
current_length = 0
has_sequence = False

with open(filename) as f:
    for line in f:
        line = line.strip()

        if line.startswith(">"):
            if has_sequence:
                lengths.append(current_length)
            current_length = 0
            has_sequence = True
        elif has_sequence:
            current_length += len(line)

if has_sequence:
    lengths.append(current_length)

count = 0
for length in lengths:
    if length < min_length:
        count += 1

print("짧은 서열 개수:", count)