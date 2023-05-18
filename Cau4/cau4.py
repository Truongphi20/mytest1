filename = 'sample.fasta'
seqs_list = []

with open(filename, 'r') as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        if line[0] != '>':
            seqs_list.append(line.rstrip())

# print(seqs_list)
seqs = ''.join(seqs_list)
print('Sequences: ')
print(seqs)
print("\n")

subs = {"A": "T", "T": "A", "G":"C", "C":"G"}

seq_com = ""
for char in seqs:
    seq_com += subs.get(char)
# print(seq_com)

seq_com_rev = seq_com[::-1]
print('Reverse complement sequences: ')
print(seq_com_rev)

# What is the rstrip action do to the line ?
"""
Write a Python script to identify all the reverse complement sequences in a
FASTA file. Assume that the file is named "sample.fasta" and is located in the
current working directory.
"""
