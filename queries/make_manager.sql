CREATE TABLE manager (
    manager_id INTEGER PRIMARY KEY AUTOINCREMENT,
    manager_name TEXT
);

INSERT INTO manager (manager_name)
VALUES ('John'), ('Alice'), ('Michael'), ('Emma');

SELECT * FROM manager;

UPDATE employees
SET manager_id = 1
WHERE manager_id = 100;

UPDATE employees
SET manager_id = 2
WHERE manager_id = 108;

UPDATE employees
SET manager_id = 3
WHERE manager_id = 123;


UPDATE employees
SET manager_id = 4
WHERE manager_id = 147;