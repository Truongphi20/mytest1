#!/usr/bin/bash

access_file="sample.fastq"
number=0

while IFS= read -r line
do 
	first_char=${line:0:1}
	#echo $first_char
	if [[ $first_char == "A" ]] || [[ $first_char == "G" ]] || [[ $first_char == "C" ]] || [[ $first_char == "T" ]]
	then
		((number+=1))
		#echo $first_char
	fi
done < ${access_file}

echo "Number of reads: "$number

#Cong: Because this is fastq file, you can count the number of sequences in 2 different ways, easier and quicker than what did you done above
## 1. Count the number of lines, then divide it by four
## 2. Count the number lines started with the "@" sign
