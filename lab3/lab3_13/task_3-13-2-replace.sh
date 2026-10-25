#!/bin/bash

newFile=$(sed "s| |\t|g" sequences.txt)
echo "$newFile"
