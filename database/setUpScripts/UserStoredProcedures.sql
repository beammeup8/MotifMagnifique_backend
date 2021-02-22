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
    INSERT INTO authtoken (userId, last_accessed, token)
      VALUES (userID, NOW(), NULL);
  END //

Create Procedure
  CheckPassword (p_username VARCHAR(20), p_password VARCHAR(50), p_authToken CHAR(50))
  BEGIN
    DECLARE userID TYPE OF user.id;
    DECLARE correct_password TYPE of user.password;
    
    SELECT id, password INTO userID, correct_password FROM user WHERE username=p_username;
    IF correct_password = p_password THEN
      UPDATE authtoken SET last_accessed = NOW(), token = p_authToken WHERE userId = userID;
      SELECT TRUE;
    ELSE
      SELECT FALSE;
    END IF;
  END //

Create Function
  CheckAuthToken (
    p_username VARCHAR(20),
    p_authToken CHAR(50)
    )
  RETURNS BOOLEAN
  BEGIN
    DECLARE accessed_time TYPE OF authtoken.last_accessed;
    DECLARE time_out TYPE OF authtoken.timeout_len;
    DECLARE curr_time TYPE OF authtoken.last_accessed;
    DECLARE is_valid BOOLEAN;

    SELECT last_accessed, timeout_len INTO accessed_time, time_out
    FROM authtoken, user 
    WHERE user.username = p_username
    AND authtoken.token = p_authToken;
    
    SET curr_time = NOW();
    SET is_valid = (curr_time - accessed_time < (time_out * 60000));

    IF is_valid THEN
      UPDATE authtoken SET last_accessed = curr_time WHERE userId = userID;
    END IF;
    RETURN is_valid;
  END//

Create Procedure
  GetUserDetails (p_username VARCHAR(20), p_authToken CHAR(50))
  BEGIN
    DECLARE is_valid BOOLEAN;

    SET is_valid = CheckAuthToken(p_username, p_authToken);

    IF is_valid THEN
      SELECT username, email, fName, lName 
      FROM user
      WHERE username = p_username;
    ELSE
      SELECT NULL;
    END IF;
  END//