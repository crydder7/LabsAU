#!/bin/bash

allMarks=$(awk '{sum+=$2} END {print sum}' students.txt)
echo "$allMarks"


mean=$(awk '{sum+=$2; count+=1} END {print sum/count}' students.txt)
echo "$mean"


max=$(awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' students.txt)
echo "$max"
