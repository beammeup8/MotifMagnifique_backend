#!/bin/bash
initialCreationScript=InitialDatabase.sql
mysql -u root -p motifMagnifique < database/setUpScripts/$initialCreationScript
echo 'Created initial database'
fileContents='sudo cat database/userLoginInfo.yaml'
username=$($fileContents | shyaml get-value username)
password=$($fileContents | shyaml get-value password)

for filename in Tables.sql CreateStoredProcedures.sql
do
  echo 'Running' $filename
  mysql -u ${username} -ppassword motifMagnifique < database/setUpScripts/$filename
done
