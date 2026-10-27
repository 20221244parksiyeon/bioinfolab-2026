import sys


def count_sequences(path):
    count = 0
    with open(path) as f:
        for line in f:
            if line.startswith(">"):
                count += 1
    return count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <fasta_file>", file=sys.stderr)
        sys.exit(1)
    print(count_sequences(sys.argv[1]))
