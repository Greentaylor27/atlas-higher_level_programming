-- Creates a database if it doesn't exsist
IF EXSIST (SELECT name FROM sys.databases WHERE name = 'hbtn_0c_0')
BEGIN
    PRINT "database exsits"
END
ELSE
BEGIN
    CREATE DATABASE 'hbtn_0c_0'
END
