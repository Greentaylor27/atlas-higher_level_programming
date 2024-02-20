-- Creates a new table in current database
IF EXISTS first_table
BEGIN
    CREATE TABLES first_table(
        id int
        name VARCHAR(256)
    )
END
ELSE
PRINT 'TABLE EXISTS'
