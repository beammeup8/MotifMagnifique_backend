DROP Database IF Exists glowstick;

Create Database glowstick;
Use glowstick;


Drop USER IF Exists user;
GRANT ALL PRIVILEGES ON *.* TO user@localhost IDENTIFIED BY 'password';