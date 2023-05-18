filename = 'sample.fastq'
id_list = []
sequence_list = []
qc_list = []

with open(filename, 'r') as f:
    while True:
        line = f.readline().rstrip()
        if len(line) == 0:
            break
        else: 
            id_list.append(line)
            sequence_list.append(f.readline().rstrip())
            f.readline()
            qc_list.append(f.readline().rstrip())

# print(id_list)
# print(sequence_list)

length_seqs = list(map(lambda x: len(x),sequence_list))
# print(length_seqs)

average = sum(length_seqs)/len(length_seqs)
print("Average read length: ")
print(average)

#Cong: There are many shorter ways, think about it. Some inessential variables such as qc_list or id_list should be excluded in order to increase the pace
