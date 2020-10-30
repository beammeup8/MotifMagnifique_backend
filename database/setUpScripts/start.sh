#!/bin/bash

# installs the server library if not currently installed
if ! command -v "mysql" >/dev/null 2>&1; 
then
  sudo apt update
  sudo apt install mariadb-server
  echo "mariadb installed"
else
  echo "mariadb was previously installed"
fi
