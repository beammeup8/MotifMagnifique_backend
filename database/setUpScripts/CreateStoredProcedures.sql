DELIMITER //

Create Procedure 
  CreateUser
  (p_username VARCHAR(50),
  p_email VARCHAR(50),
  p_fName VARCHAR(50),
  p_lName VARCHAR(50),
  p_password VARCHAR(50),
  p_front_salt CHAR(50),
  p_back_salt CHAR(50))
  MODIFIES SQL DATA
  BEGIN
    INSERT INTO user (username, email, fName, lName, password, front_salt, back_salt)
    VALUES (p_username, p_email, p_fName, p_lName, p_password, p_front_salt, p_back_salt);
  END //