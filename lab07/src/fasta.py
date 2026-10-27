
"""FASTA 파일을 다루는 함수 모음"""

def read_fasta(filename):
    """FASTA 파일을 읽어 {이름: 서열} 딕셔너리로 돌려준다."""
    seqs = {}
    name = None
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            if line.startswith(">"):
                name = line[1:].split()[0]
                seqs[name] = ""
            else:
                seqs[name] = seqs[name] + line.upper()
    return seqs


def gc_content(seq):
    """서열의 GC 비율을 0과 1 사이의 수로 돌려준다."""
    if len(seq) == 0:
        return 0.0
    gc = seq.count("G") + seq.count("C")
    return gc / len(seq)

def write_fasta(seqs, filename):
    """{이름: 서열} 딕셔너리를 FASTA 파일로 저장한다."""
    with open(filename, "w") as out:
        for name in seqs:
            out.write(">" + name + "\n")
            out.write(seqs[name] + "\n")


def reverse_complement(seq):
    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    seq = seq.upper()
    reversed_seq = seq[::-1]

    result = ""
    for base in reversed_seq:
        result += complement[base]

    return result

def length_stats(seqs):
    lengths = [len(seq) for seq in seqs.values()]

    if len(lengths) == 0:
        return {
            "count": 0,
            "total": 0,
            "average": 0.0,
            "min": 0,
            "max": 0
        }

    return {
        "count": len(lengths),
        "total": sum(lengths),
        "average": sum(lengths) / len(lengths),
        "min": min(lengths),
        "max": max(lengths)
    }


if __name__ == "__main__":
    import sys

    seqs = read_fasta(sys.argv[1])
    for name in seqs:
        print(name, len(seqs[name]), round(gc_content(seqs[name]), 3))

    seq = "ATGC"
    rc = reverse_complement(seq)

    print("원래 서열:", seq)
    print("역상보 서열:", rc)
    print("두 번 적용:", reverse_complement(rc))
    print("원래 서열과 같은가?", reverse_complement(rc) == seq)

