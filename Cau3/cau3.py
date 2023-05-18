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

# This code is good, however, I expect you can also print each sequence with format: `seqid: length` before calculate the average
"""
Write a Bash/Python script to calculate the average read length of a FASTQ file.
Assume that the file is named "sample.fastq" and is located in the current
working directory.
"""
