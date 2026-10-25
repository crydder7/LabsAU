#!/bin/bash

names=$(awk '{print $1}' students.txt)
echo "$names"


marks=$(awk '{print $2}' students.txt)
echo "$marks"

namesNumbers=$(awk '{print NR, $1}' students.txt)
echo "$namesNumbers"
