
import sys
from fasta import read_fasta, length_stats

filename = sys.argv[1]

seqs = read_fasta(filename)
stats = length_stats(seqs)

print("서열 개수:", stats["count"])
print("전체 길이:", stats["total"])
print("평균 길이:", round(stats["average"], 2))
print("최소 길이:", stats["min"])
print("최대 길이:", stats["max"])
