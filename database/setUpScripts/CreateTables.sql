Create Table user(
  id            bigint(20) Not Null AUTO_INCREMENT,
  username      VARCHAR(50),
  email         VARCHAR(50),
  PRIMARY KEY(id)
);

Create Table portfolio(
  id            bigint(20) Not Null AUTO_INCREMENT,
  title         VARCHAR(50),
  description   VARCHAR(1000),
  PRIMARY KEY(id)
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
  tag            VARCHAR(50)  REFERENCES tag(name)
);

Create Table owns(
  userId    bigint(20)        REFERENCES user(id),
  portfolioId    bigint(20)   REFERENCES portfolio(id)
);
