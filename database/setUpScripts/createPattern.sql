DELIMITER //

  Create Procedure 
  CreatePattern
  (p_title      VARCHAR(50),
  p_desc        VARCHAR(1000),
  p_price       DOUBLE(10,2),
  p_link        VARCHAR(1000)
  )
  
  MODIFIES SQL DATA
  
  BEGIN
    INSERT INTO pattern(title, description, price, link) 
    VALUES (p_title, p_desc, p_price, p_link);
  
  END 
  
  
  // 