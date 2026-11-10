
import sys

def normalize_name(header):
    name = header.strip().split()[0]
    name = name.lstrip("@")

    # 끝의 /1, /2 또는 _1, _2 제거
    if name.endswith(("/1", "/2", "_1", "_2")):
        name = name[:-2]

    return name


def check_paired(file1, file2):
    count = 0
    mismatch = 0

    with open(file1) as f1, open(file2) as f2:
        while True:
            h1 = f1.readline()
            h2 = f2.readline()

            if not h1 and not h2:
                break

            if not h1 or not h2:
                print("두 파일의 read 개수가 다릅니다.")
                return

            # 각 read의 나머지 3줄 건너뛰기
            for _ in range(3):
                if not f1.readline() or not f2.readline():
                    print("불완전한 FASTQ 레코드가 있습니다.")
                    return

            count += 1

            name1 = normalize_name(h1)
            name2 = normalize_name(h2)

            if name1 != name2:
                mismatch += 1
                if mismatch <= 5:
                    print("불일치:", name1, name2)

    print("확인한 read pair 수:", count)
    print("이름 불일치 수:", mismatch)

    if mismatch == 0:
        print("모든 read가 같은 순서로 짝을 이룹니다.")
    else:
        print("일부 read의 짝이 일치하지 않습니다.")


check_paired(sys.argv[1], sys.argv[2])
