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
* py-bcrypt - install via pip3
* [flask](https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)
* flask-restful - install via pip3
* flask_httpauth - install via pip3
* [database instance](api/api/database/README.md)

## API
### Hitting Endpoints
Please use the workspace in [Postman](https://app.getpostman.com/join-team?invite_code=d3d85558fa8ed29d473ce52984dc53e7) to hit the exisiting endpoints.

### Starting the API Locally
Run the following commands:
```
export FLASK_APP=MotifMagnifique_backend/api
export FLASK_ENV=development
pip3 install -e api
flask run
```

## Running tests
All tests should be in a file begining with `test_` and can be run using the following command:
```
python3 -m unittest discover -s ./api/api/tests -p "test_*.py"
```