#!/bin/bash
read -p "Enter your weight(kg): " WEIGHT
read -p "Enter your height(meters: " HEIGHT
echo "Your BMI is:"
RESULT=$(echo "scale=2; $WEIGHT / ($HEIGHT * $HEIGHT)" | bc)
echo $RESULT
