import sys

if len(sys.argv) < 3:
    print("사용법: python3 src/shortlines.py <FASTA파일> <최소길이>")
    sys.exit(1)

filename = sys.argv[1]
min_length = sys.argv[2]

if not min_length.isdigit():
    print("오류: 최소 길이는 숫자여야 합니다.")
    sys.exit(1)

min_length = int(min_length)

count = 0

with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if not line.startswith(">") and len(line) < min_length:
            count = count + 1

print("짧은 서열 줄 개수:", count)