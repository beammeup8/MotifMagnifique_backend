Create Procedure 
  CreateUser
  (p_username VARCHAR(50),
  p_email VARCHAR(50),
  p_fName VARCHAR(50),
  p_lName VARCHAR(50),
  p_password VARCHAR(50),
  p_salt CHAR(50))
  MODIFIES SQL DATA
  BEGIN
  INSERT INTO user(username, email, fname, lname, password, salt) 
  VALUES (p_username, p_email, p_fname, p_lname, p_password, p_salt);
  END;

