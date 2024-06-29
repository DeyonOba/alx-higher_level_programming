-- Script that creates a database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`)
-- on a MySQL server.
--  + `cities` description:
--      + `id` INT unique, auto generated, can't be null and is primary key.
--      + `state_id` INT, can't be null and must be a FOREIGN KEY that references to `id` of the `states` table
--      + `name` VARCHAR(256) can't be null
--      + If the database `htbn_0d_usa` already exists, the script does not raise an error
--      + If the `cities` table already exists, the script does not raise any error

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT FOREIGN KEY REFERENCES states(id) NOT NULL,
    `name` VARCHAR(256) NOT NULL
);
