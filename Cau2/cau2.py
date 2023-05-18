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

# You should print the seqid along with the length
"""
Write a Python script to extract the sequence length of each record in a FASTA
file. Assume that the file is named "sample.fasta" and is located in the current
working directory.
"""
