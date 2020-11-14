Create Table user(
  id            bigint(20) Not Null AUTO_INCREMENT,
  username      VARCHAR(50),
  email         VARCHAR(50),
  PRIMARY KEY(id),
  CONSTRAINT username_unique UNIQUE (username),
  CONSTRAINT email_unique UNIQUE (email)
);

Create Table portfolio(
  id            bigint(20)    Not Null AUTO_INCREMENT,
  title         VARCHAR(50),
  description   VARCHAR(1000),
  ownedBy       bigint(20)    REFERENCES user(id),
  PRIMARY KEY(id),
  CONSTRAINT title_per_user_unique UNIQUE (title, ownedBy)
);

Create Table tag(
  name          VARCHAR(50),
  PRIMARY KEY(name)
);

Create Table stock(
  ticker        VARCHAR(5),
  name          VARCHAR(50),
  marketClose   DOUBLE(20,2),
  PRIMARY KEY(ticker)
);

Create Table porfolioTags(
  portfolioId    bigint(20)   REFERENCES portfolio(id),
  tag            VARCHAR(50)  REFERENCES tag(name),
  PRIMARY KEY(portfolioId, tag)
);

Create Table tracks(
  userId         bigint(20)   REFERENCES user(id),
  portfolioId    bigint(20)   REFERENCES portfolio(id),
  hasPurchased   BOOLEAN,
  PRIMARY KEY(userId, portfolioId)   
);
