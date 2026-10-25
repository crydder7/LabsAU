#!/bin/bash

printf "%-15s %-7s %-7s %-7s %-7s\n" "File" "A" "T" "G" "C"

for file in *.fasta; do
  if [ ! -s "$file" ]; then
    continue
  fi
  SEQ=$(grep -v "^>" "$file" | tr -d '\n')

  A=$(echo "$SEQ" | grep -o "A" | wc -l)
  T=$(echo "$SEQ" | grep -o "T" | wc -l)
  G=$(echo "$SEQ" | grep -o "G" | wc -l)
  C=$(echo "$SEQ" | grep -o "C" | wc -l)
  printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$A" "$T" "$G" "$C"
done
