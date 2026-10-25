#!/bin/bash

newpath=$(sed "s|/var/lib/mysql/data|/mnt/ssd/mysql|g" settings.php)
echo "$newpath"
