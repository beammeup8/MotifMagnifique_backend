DROP Database IF Exists motifMagnifique;

Create Database motifMagnifique;
Use motifMagnifique;


Drop USER IF Exists user;
GRANT ALL PRIVILEGES ON *.* TO user@localhost IDENTIFIED BY 'password';