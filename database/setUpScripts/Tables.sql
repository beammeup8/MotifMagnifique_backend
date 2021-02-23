Create Table user(
  id            bigint(20) Not Null AUTO_INCREMENT,
  username      VARCHAR(50),
  email         VARCHAR(50),
  fName         VARCHAR(50) DEFAULT NULL,
  lName         VARCHAR(50) DEFAULT NULL,
  password      VARCHAR(50),
  front_salt    CHAR(50),
  back_salt     CHAR(50),
  PRIMARY KEY(id),
  CONSTRAINT username_unique UNIQUE (username),
  CONSTRAINT email_unique UNIQUE (email)
);

Create Table authtoken(
  userId        bigint(20)  REFERENCES user(id),
  authtoken     VARCHAR(50) DEFAULT NULL,
  last_accessed TIMESTAMP,
  setable       BOOLEAN,
  PRIMARY KEY(userId)
);

Create Table tag(
  id            bigint(20) Not Null AUTO_INCREMENT,
  name          VARCHAR(50),
  value         VARCHAR(50),
  PRIMARY KEY(id),
  CONSTRAINT tag_unique UNIQUE (name, value)
);

Create Table pattern(
  id            bigint(20)    Not Null AUTO_INCREMENT,
  title         VARCHAR(50),
  description   VARCHAR(5000),
  ownedBy       bigint(20)    REFERENCES user(id),
  price         DOUBLE(10,2) DEFAULT -1.0,
  link          VARCHAR(1000),
  PRIMARY KEY(id),
  CONSTRAINT title_per_user_unique UNIQUE (title, ownedBy)
);

Create Table patternTag(
  pattern       bigint(20) REFERENCES pattern(id),
  tag           bigint(20) REFERENCES tag(id),
  PRIMARY KEY(pattern, tag)
);

Create Table fabricType(
  id            bigint(20) Not Null AUTO_INCREMENT,  
  name          VARCHAR(100),         
  PRIMARY KEY(id)
);

Create Table fabric(
  id            bigint(20) Not Null AUTO_INCREMENT,
  name          VARCHAR(100),
  brand         VARCHAR(100) DEFAULT NULL,
  link          VARCHAR(1000) DEFAULT NULL,
  fabricType    bigint(20)  REFERENCES fabricType(id),
  PRIMARY KEY(id)
);

Create Table fabricTag(
  fabric        bigint(20) REFERENCES fabric(id),
  tag           bigint(20) REFERENCES tag(id),
  PRIMARY KEY(fabric, tag)
);

Create Table fabricStash(
  user          bigint(20) REFERENCES user(id),
  fabric        bigint(20) REFERENCES fabric(id),
  PRIMARY KEY(user, fabric)
);


Create Table unit(
  name          VARCHAR(20),
  cmLen         DOUBLE(10,4),
  displayFrac   BOOLEAN,
  PRIMARY KEY(name)
);

Create Table patternFabricType(
  pattern       bigint(20) REFERENCES pattern(id),
  fabricType    bigint(20) REFERENCES fabricType(id),
  amount        DOUBLE(10,4),
  amountUnit    VARCHAR(20) REFERENCES unit(name),
  width         DOUBLE(10,4),
  widthUnit    VARCHAR(20) REFERENCES unit(name),
  PRIMARY KEY(pattern, fabricType)
);

Create Table size(
  id            bigint(20) Not Null AUTO_INCREMENT,
  name          VARCHAR(50) DEFAULT NULL,
  sizeAuth      bigint(20)   DEFAULT NULL,
  neck          DOUBLE(10,4) DEFAULT NULL,
  shoulder      DOUBLE(10,4) DEFAULT NULL,
  armLength     DOUBLE(10,4) DEFAULT NULL,
  wrist         DOUBLE(10,4) DEFAULT NULL,
  overBust      DOUBLE(10,4) DEFAULT NULL,
  bust          DOUBLE(10,4) DEFAULT NULL,
  underBust     DOUBLE(10,4) DEFAULT NULL,
  waist         DOUBLE(10,4) DEFAULT NULL,
  hip           DOUBLE(10,4) DEFAULT NULL,
  frontWaistLength      DOUBLE(10,4) DEFAULT NULL,
  backWaistLength      DOUBLE(10,4) DEFAULT NULL,
  frontRise     DOUBLE(10,4) DEFAULT NULL,
  backRise      DOUBLE(10,4) DEFAULT NULL,
  inseam        DOUBLE(10,4) DEFAULT NULL,
  outseam       DOUBLE(10,4) DEFAULT NULL,
  unit    VARCHAR(20) REFERENCES unit(name),
  PRIMARY KEY(id)
);

Create Table patternSize(
  pattern       bigint(20) REFERENCES pattern(id),
  size          bigint(20) REFERENCES size(id),
  PRIMARY KEY(pattern, size)
);

create Table project(
  id            bigint(20) Not Null AUTO_INCREMENT,
  title         VARCHAR(50),
  creator       bigint(20) REFERENCES user(id),
  pattern       bigint(20) REFERENCES pattern(id),
  visibility    ENUM('public', 'private', 'link'),
  isCompleted   BOOLEAN,
  PRIMARY KEY(id)
);


Create Table favoritePattern(
  userId         bigint(20)   REFERENCES user(id),
  patternId      bigint(20)   REFERENCES pattern(id),
  hasPurchased   BOOLEAN,
  PRIMARY KEY(userId, patternId)   
);
