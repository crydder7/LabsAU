#!/bin/bash

passwd=$(grep "$USER" /etc/passwd)
echo "$passwd"
