-- Generates the hbnb_dev_db database with defined parameters.
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates a user in case it does not already exist.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- Assigns a password to a user.
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- Bestows privileges to a user for a specific database.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Provides the user with SELECT privileges on the performance_schema database.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;
