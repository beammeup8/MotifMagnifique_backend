DELIMITER //

/*create patternFabricType*/
/*create patternSize*/
/*create patternTag*/

  Create Procedure 
  CreatePattern
  (p_title      VARCHAR(50),
  p_desc        VARCHAR(1000),
  p_price       DOUBLE(10,2),
  p_link        VARCHAR(1000)
  )
  /*needs:
  * list of tags
  * list of patternFabricType
  * list of sizes
  * output variable for the id to be returned
  */
  
  MODIFIES SQL DATA
  
  BEGIN
  /* authentication */
    INSERT INTO pattern(title, description, price, link) 
    VALUES (p_title, p_desc, p_price, p_link);
  
  END // 

/*get pattern file returns the file link, authenticate*/

/*updatePattern, takes all fields create does and can update all but id, authenticate*/

/*add pattern tag, authenticate*/

/*delete pattern tag, authenticate*/

/*add pattern size, authenticate*/

/*delete pattern size, authenticate*/

/*add patternFabricType, authenticate*/

/*delete patternFabricType, authenticate*/

/* add favorite pattern: takes user and pattern, authenticate*/

/* remove favorite pattern: takes user and pattern, authenticate*/

/* purchase pattern handles all database changes on purchase, authenticate*/

/* delete pattern, hard delete if no one has purchased, otherwise soft delete, authenticate*/

/*add and delete image procedures*/