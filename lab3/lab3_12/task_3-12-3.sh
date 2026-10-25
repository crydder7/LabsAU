#!/bin/bash

names=$(grep -E "\.(jpg|png|gif)$" files.txt)
echo "$names"
