DELIMITER //

  Create Procedure 
  CreateTag
  (t_name VARCHAR(50),
  t_value VARCHAR(50))
  
  MODIFIES SQL DATA
  
  BEGIN
    INSERT INTO tag(name, value) 
    VALUES (t_name, t_value);
  
  END 
//    
Create Procedure 
CreateUnit
(u_name               VARCHAR(20),
u_cmLen               DOUBLE(10,4),
u_displayFrac         TINYINT(1) DEFAULT 1)
  
MODIFIES SQL DATA
  
BEGIN
  INSERT INTO unit(name, cmLen, displayFrac) 
  VALUES (u_name, u_cmLen, u_displayFrac);
  
END 

  
// 

  
