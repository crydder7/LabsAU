#!/bin/bash

checkSuperUser() {
  if [ $EUID -eq 0 ]; then
    echo "nice"
    return 0
  else
    echo "u r not superUser!"
    return 67
  fi
}

result=$(checkSuperUser)
echo $result
