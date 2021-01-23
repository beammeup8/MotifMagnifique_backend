# Database

This is a PostgreSQL database. To create a local instance please run the start.sh file on the computer you wish to run it on. 

## Requirements

The following tools need to be installed to start the database:
* [python 3](https://www.python.org/)
* [pip3](https://pip.pypa.io/en/stable/installing/)
* pyyaml - install via pip3
* [mariadb](https://mariadb.com/downloads/)
* [mariadb python connector](https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/s)

## Starting the database

### Setting up the database enviroment

1. Insure you can run mariadb locally by running
```
sudo mysql
```

2. create a yaml file named `loginInfo.yaml` with the following format:
```
username: "root"
password: "<your root password>"
```

### Running the database

The database can be started for local development work using the following command:
```
sudo python3 startDB.py
```