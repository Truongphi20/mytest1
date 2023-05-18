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

# You can only need to run `grep @ sample.fastq | wc -l`
