Create Table user(
  id            bigint(20) Not Null AUTO_INCREMENT,
  username      VARCHAR(50),
  email         VARCHAR(50)/*check for email pattern*/,
  fName         VARCHAR(50) DEFAULT NULL,
  lName         VARCHAR(50) DEFAULT NULL,
  password      VARCHAR(60),
  front_salt    CHAR(50),
  back_salt     CHAR(50),
  PRIMARY KEY(id),
  CONSTRAINT username_unique UNIQUE (username),
  CONSTRAINT email_unique UNIQUE (email)
);

Create Table authtoken(
  userId        bigint(20)  REFERENCES user(id),
  last_accessed TIMESTAMP   DEFAULT NOW(),
  token         CHAR(50),
  timeout_len   INT DEFAULT 30,
  PRIMARY KEY(userId)
);

Create Table tag(
  id            bigint(20) Not Null AUTO_INCREMENT,
  name          VARCHAR(50),
  value         VARCHAR(50),
  PRIMARY KEY(id),
  CONSTRAINT tags_unique UNIQUE (name, value)
);

Create Table pattern(
  id            bigint(20)    Not Null AUTO_INCREMENT,
  title         VARCHAR(50),
  description   VARCHAR(5000),
  ownedBy       bigint(20)    REFERENCES user(id),
  price         DOUBLE(10,2) DEFAULT -1.0,
  link          VARCHAR(1000),
  sizing        ENUM('bra', 'cape', 'child clothing', 'clothing', 'glove', 'hat', 'other', 'quilt', 'scarf'),
  PRIMARY KEY(id),
  CONSTRAINT title_per_user_unique UNIQUE (title, ownedBy)
);

/*Create PatternImage table, should have pattern ID and link to images*/

Create Table patternTag(
  pattern       bigint(20) REFERENCES pattern(id),
  tag           bigint(20) REFERENCES tag(id),
  PRIMARY KEY(pattern, tag)
);

Create Table fabricType(
  id            bigint(20) Not Null AUTO_INCREMENT,  
  name          VARCHAR(100),
  /*
  * name must be unique
  * fabric type (non-woven, woven or knit)
  */         
  PRIMARY KEY(id)
);

Create Table fabric(
  id            bigint(20) Not Null AUTO_INCREMENT,
  name          VARCHAR(100),
  brand         VARCHAR(100) DEFAULT NULL,
  link          VARCHAR(1000) DEFAULT NULL,
  fabricType    bigint(20)  REFERENCES fabricType(id),
  /*width and width unit*/
  /*add an added by attribute linking to a user id*/
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
  /*length, and length unit*/
  PRIMARY KEY(user, fabric)
);

/*move to higher up*/
Create Table unit(
  name          VARCHAR(20),
  cmLen         DOUBLE(10,4),
  displayFrac   BOOLEAN,
  PRIMARY KEY(name)
);

Create Table patternFabricType(
  /*name for specifc use of fabric*/
  pattern       bigint(20) REFERENCES pattern(id),
  fabricType    bigint(20) REFERENCES fabricType(id),
  amount        DOUBLE(10,4),
  amountUnit    VARCHAR(20) REFERENCES unit(name),
  width         DOUBLE(10,4),
  widthUnit    VARCHAR(20) REFERENCES unit(name),
  PRIMARY KEY(pattern, fabricType)
);

/*clothing sizes*/
Create Table braSize(
  band          INT(2),
  cup           CHAR(2),
  diff          INT(2),
  PRIMARY KEY(band, cup)
);

Create Table braSizePattern(
  band          INT(2) REFERENCES braSize(band),
  cup           CHAR(2) REFERENCES braSize(cup),
  pattern       bigint(20) REFERENCES pattern(id),
  PRIMARY KEY(band, cup, pattern)
);

Create Table gloveSize(
  size          VARCHAR(20),
  palmCircum    DOUBLE(10,4),
  PRIMARY KEY(size)
);

Create Table gloveSizePattern(
  size          VARCHAR(20) REFERENCES gloveSize(size),
  pattern       bigint(20) REFERENCES pattern(id),
  PRIMARY KEY(size, pattern)
);

Create Table hatSize(
  usSize        DOUBLE(6,4),
  headSize      DOUBLE(6,4),
  PRIMARY KEY(usSize)    
);

Create Table hatSizePattern(
  size          VARCHAR(20) REFERENCES hatSize(usSize),
  pattern       bigint(20) REFERENCES pattern(id),
  PRIMARY KEY(size, pattern)
);

/* missing the user who created it and a unique constraint between name and user*/
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

/*project fabric table, links a project to a specific fabric, with a note on use*/
/*project image table*/

Create Table favoritePattern(
  userId         bigint(20)   REFERENCES user(id),
  patternId      bigint(20)   REFERENCES pattern(id),
  hasPurchased   BOOLEAN, /*remove once the purchasedPatterns is added*/
  PRIMARY KEY(userId, patternId)   
);

/*PurchasedPattern is like favorites, but has a transaction number*/
