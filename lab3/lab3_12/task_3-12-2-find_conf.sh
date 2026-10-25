#!/bin/bash
files=$(ls /etc)
names=$(echo "$files" | grep "\.conf$")
echo "$names"

