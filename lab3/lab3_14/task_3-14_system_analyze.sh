#!/bin/bash

df -h >> text.txt

result=$(awk '{
  if (NR>1)
    percent=$5
    sub(/%/,"",percent)
    if (percent>90)
      print $1,$5,"mala"
    else 
      print $1,$5
}' text.txt)
echo "$result"
