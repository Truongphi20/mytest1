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

#Cong: If there are more than one sequence provided in a fasta file, your script will generate the false result. Because the code line: "seqs = ''.join(seqs_list)"
