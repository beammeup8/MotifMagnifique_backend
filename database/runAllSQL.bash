#!/bin/bash
pwd
initialCreationScript=InitialDatabase.sql
mysql -u root -p motifMagnifique < database/setUpScripts/$initialCreationScript
echo 'Ran the initial database script'
fileContents='sudo cat database/userLoginInfo.yaml'
username=$($fileContents | shyaml get-value username)
password=$($fileContents | shyaml get-value password)

filesToRun=(
  Tables.sql
  UserStoredProcedures.sql
  MiscStoredProcedures.sql
  PatternStoredProcedures.sql
  FabricStoreProcedures.sql
  )


for filename in ${filesToRun[@]};do
  echo 'Running' $filename
  mysql -u ${username} -ppassword motifMagnifique < database/setUpScripts/$filename
done
