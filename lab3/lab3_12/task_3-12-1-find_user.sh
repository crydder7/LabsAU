#!/bin/bash

passwd=$(grep "root" /etc/passwd)
echo "$passwd"
