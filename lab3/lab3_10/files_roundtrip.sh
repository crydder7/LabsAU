#!/bin/bash

for i in {1..10}; do
  touch "file"$i".txt"
done

itter=10
while [ $itter -ge 1 ]; do
  rm "file"$itter".txt"
  let "itter-=1"
done
