DELIMITER ;
  Create Procedure 
  CreateTag
  (t_name VARCHAR(50),
  t_value VARCHAR(50))
  MODIFIES SQL DATA
  BEGIN
  INSERT INTO tag(t_name, t_value) 
  VALUES (t_name, t_value)
  END; 

