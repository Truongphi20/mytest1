filename = 'sample.fasta'
seq_lengths = []

with open(filename, 'r') as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        if line[0] != '>':
            seq_lengths.append(len(line.rstrip()))

print('List of length:')
print(seq_lengths)