-- Generates the hbnb_test_db database with specified parameters.
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates a user in case it does not already exist.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- Assigns a password to a user.
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- Bestows privileges to a user for a specific database.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Provides the user with SELECT privileges on the performance_schema database.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;
