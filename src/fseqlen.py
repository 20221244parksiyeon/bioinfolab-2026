
def gc_content(seq):
    if len(seq) == 0:
        return 0.0
    gc = seq.count("G") + seq.count("C")
    return gc / len(seq)

a = gc_content("ATGC")
b = gc_content("")

print("a =", a)
print("b =", b)
