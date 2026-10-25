#!/bin/bash

names=$(awk -F "," '{print($2)}' data.csv)
echo "$names"
echo "__________"
exp=$(awk -F "," '$3>20{print $2}' data.csv)
echo "$exp"
echo "__________"
allPrice=$(awk -F "," '{sum+=$3} END {print sum}' data.csv)
echo "$allPrice"
