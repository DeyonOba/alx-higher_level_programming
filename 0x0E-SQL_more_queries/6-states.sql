-- Script that create a database `htbn_0d_usa` and a table `states` in the database in your MYSQL server.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS `states` (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
