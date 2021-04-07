# Endpoints
This will be supplemented with a document in an api definition language at a later time, but for now this should suffice to explain how the various endpoints work.

## User
Append `/user` to call the following endpoints.

### Get User Details
* Type = GET
* Authentication required

Returns the user details for a given username, if the authtoken matches the username, otherwise it will return not found.

#### Query Parameters:
* username
* authtoken

#### Returns :
On failure a 404 error is returned on success the following model is used:
```
{
  "username": String,
  "email": String,
  "fName": String,
  "lName": String
}
```

### Create a New User
* Type = PUT
* No authentication

Creates a new user. Requries that the username and email both do not already exist in the database.

#### Body Model:
```
{
  username: String,
  email: String
  fName: String
  lName: String
  password: String
}
```

#### Returns:
On failure a dictionary of duplicate or invalid values is returned, on success the auth token is returned

### Login to an existing user account
* Type = PUT
* Endpoint is authentication

Logs in an existing user.

#### Body Model:
```
{
  username: String,
  password: String
}
```

#### Returns:
On failure a 404 error is returned, on success the auth token is returned
