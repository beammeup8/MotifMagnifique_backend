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

#get the database name
name="test"

#get the database password with default
pass="password"

#get the database creator with default
user="root"

#execute sql commands with the user
sudo mysql -u $user -p -e "DROP DATABASE IF EXISTS $name;CREATE DATABASE $name;DROP USER IF EXISTS $name@localhost;CREATE USER $name@localhost identified by '$pass';GRANT ALL ON $name.* to $name@localhost WITH GRANT OPTION;"

#confirmation message
echo "Created database and user: $name"