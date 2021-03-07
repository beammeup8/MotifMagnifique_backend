# Motif Magnifique Backend

Main repository for our new sewing pattern search engine/ store website's backend

The website will be located at motifmagnifique.com

## Requirements
The following tools need to be installed to run this application:
* [python 3](https://www.python.org/)
* [pip3](https://pip.pypa.io/en/stable/installing/)
* pyyaml - install via pip3
* [mariadb](https://mariadb.com/downloads/)
* [mariadb python connector](https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/s)
* py-bcrypt install via pip3

## Running the code
```
python3 main.py
```

## Running tests
All tests should be in a file begining with `test_` and can be run using the following command:
```
python3 -m unittest discover -s ./ -p "test_*.py"
```