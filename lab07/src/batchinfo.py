import sys
from pathlib import Path
from fasta import read_fasta, gc_content, length_stats

folder = Path(sys.argv[1])
output = sys.argv[2]

with open(output, "w") as out:
    out.write("filename\tcount\ttotal\tmean_gc\n")

    for path in sorted(folder.iterdir()):
        if not path.is_file():
            continue
        if path.suffix.lower() not in (".fasta", ".fa", ".fna"):
            continue

        seqs = read_fasta(path)
        stats = length_stats(seqs)

        if stats["count"] > 0:
            mean_gc = sum(gc_content(seq) for seq in seqs.values()) / stats["count"]
        else:
            mean_gc = 0.0

        out.write(
            f"{path.name}\t{stats['count']}\t"
            f"{stats['total']}\t{mean_gc:.4f}\n"
        )