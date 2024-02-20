-- Creates a database and table for states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    name VARCHAR(256),
    PRIMARY KEY (id)
);
