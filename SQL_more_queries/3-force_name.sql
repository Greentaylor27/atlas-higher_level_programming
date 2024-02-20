-- creates a new table with a constraint
CREATE TABLE IF NOT EXISTS forced_name(
    id INT,
    name VARCHAR(256)
);
ALTER COLUMN name VARCHAR NOT NULL;
