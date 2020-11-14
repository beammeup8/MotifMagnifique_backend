# Database

This is a PostgreSQL database. To create a local instance please run the start.sh file on the computer you wish to run it on. 

## Requirements

The following tools need to be installed to start the database:
* [python 3](https://www.python.org/)
* [pip3](https://pip.pypa.io/en/stable/installing/)
* [postgreSQL](https://www.postgresql.org/)
* [postgreSQL connector](https://www.psycopg.org/docs/install.html#install-from-source)

## Starting the database

### Setting up the database enviroment

1. Start by switching to the default postgres user
```
sudo su postgres
```
2. Then run the PostgreSQL shell
```
psql
```
3. Create new admin user
```
CREATE USER admin WITH PASSWORD 'password';
```
4. Give the admin user admin permissions
```
ALTER USER admin WITH SUPERUSER;
```
5. Create Database
```
CREATE DATABASE Glowstick;
```
6. Quit the prompt
```
\q
```
7. Return to your standard user profile (enter your user password when prompted)
```
su <username>
```

### Running the database

The database can be started for local development work using the following command:
```
python3 setUpScripts/startDB.py
```