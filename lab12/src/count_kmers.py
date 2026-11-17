
def count_kmers(L, k):
    if k > L:
        return 0
    return L - k + 1

# 여러 (L, k) 조합 확인
tests = [(10, 5), (100, 5), (20, 3), (5, 5), (5, 8)]

for L, k in tests:
    result = count_kmers(L, k)
    print(f"L={L}, k={k} → k-mer 개수: {result}")
