#!/bin/bash

best=$(awk '$2 > 80 {print $1}' students.txt)
echo "$best"

echo "__________"

worst=$(awk '$2 < 70 {print $1}' students.txt)
echo "$worst"

echo "__________"

first=$(awk 'NR == 1 {print $0}' students.txt)
echo "$first"
