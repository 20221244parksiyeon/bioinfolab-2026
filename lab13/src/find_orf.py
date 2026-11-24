import sys
 
STOPS = ["TAA", "TAG", "TGA"]
 
def find_orfs(seq, frame):
    orfs = []
    start = None
 
    for i in range(frame, len(seq) - 2, 3):
        codon = seq[i:i + 3]
 
        if codon == "ATG" and start is None:
            start = i
        elif codon in STOPS and start is not None:
            orfs.append((start, i + 3))
            start = None
 
    return orfs
 
# 역상보 서열: A↔T, G↔C로 상보적 치환한 뒤 서열을 뒤집는다
COMPLEMENT = {"A": "T", "T": "A", "G": "C", "C": "G"}
 
def reverse_complement(seq):
    comp = "".join(COMPLEMENT.get(base, "N") for base in seq)
    return comp[::-1]
 
def print_orfs(label, seq):
    # 좌표는 해당 방향 서열 기준 (0-based 시작, 끝은 미포함)
    print("[" + label + "]", seq)
    for frame in [0, 1, 2]:
        orfs = find_orfs(seq, frame)
        print("틀", frame + 1, ":", orfs)
        for s, e in orfs:
            print("   ", seq[s:e], "길이", e - s)
 
seq = sys.argv[1].upper()
rc_seq = reverse_complement(seq)
 
print_orfs("정방향 (+)", seq)
print()
print_orfs("역상보 방향 (-)", rc_seq)

