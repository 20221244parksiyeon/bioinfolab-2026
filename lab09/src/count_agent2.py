"""FASTA 파일 이름을 받아 서열 개수를 출력한다.

사용법: python3 src/count_agent2.py <fasta_file>
"""
import os
import sys

# lab07/src/fasta.py의 read_fasta()를 재사용하기 위해 import 경로에 추가
LAB07_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "lab07", "src")
sys.path.insert(0, LAB07_SRC)

from fasta import read_fasta


def count_sequences(path):
    """FASTA 파일에 들어 있는 서열 개수를 돌려준다."""
    return len(read_fasta(path))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <fasta_file>", file=sys.stderr)
        sys.exit(1)
    print(count_sequences(sys.argv[1]))
