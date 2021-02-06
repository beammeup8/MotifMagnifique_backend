# Database

This is a PostgreSQL database. To create a local instance please run the start.sh file on the computer you wish to run it on. 

## Requirements

The following tools need to be installed to start the database:
* [python 3](https://www.python.org/)
* [pip3](https://pip.pypa.io/en/stable/installing/)
* pyyaml - install via pip3
* [mariadb](https://mariadb.com/downloads/)
* [mariadb python connector](https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/s)
* [shyaml](https://github.com/0k/shyaml) - bash yaml parser, that is installed via pip, but must be installed as the root user

## Starting the database

### Setting up the database enviroment

1. Insure you can run mariadb locally by running
```
sudo mysql
```

### Running the database

1. Start the database for local development work using the following command:
```
sudo bash database/runAllSQL.bash
```
2. Enter your root password when prompted
3. All sql scripts will be run