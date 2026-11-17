
lengths = [12, 3, 20, 8, 1, 15, 6]

lengths.sort(reverse=True)
total = sum(lengths)
half = total / 2

running = 0

for length in lengths:
    running += length
    if running >= half:
        print("N50:", length)
        break
