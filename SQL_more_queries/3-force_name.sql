-- Task 3: Create table force_name with id and name (name cannot be null)
CREATE TABLE IF NOT EXISTS force_name (
    id INT DEFAULT 0,
    name VARCHAR(256) NOT NULL
);
