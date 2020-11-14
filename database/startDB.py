#!/usr/bin/python 
import mariadb 
import yaml

login_info = {}

with open('loginInfo.yaml') as file:
  login_info = yaml.load(file, Loader=yaml.FullLoader)

print(login_info)

conn = mariadb.connect(
    user=login_info['username'],
    password=login_info['password'],
    host="localhost")

cur = conn.cursor() 

cur.execute("SHOW DATABASES")

for x in cur:
  print(x)
    
conn.close()