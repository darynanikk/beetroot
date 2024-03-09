-- A Query to display the names (first_name, last_name) using alias name
-- "First Name", "Last Name" from the table of employees;
SELECT first_name AS FirstName, last_name AS LastName
from employees;

-- A query to get the unique department ID from the employee table
SELECT DISTINCT department_id
FROM employees;

-- A query to get all employee details from the employee table ordered by first name, descending
SELECT * FROM employees
ORDER BY first_name DESC;

-- A query to get the names (first_name, last_name), salary, PF of all the employees (PF is calculated as 12% of salary)
SELECT first_name, last_name, salary, 0.12 * salary AS PF
from employees;

-- A query to get the maximum and minimum salary from the employees table
SELECT MIN(salary) AS MIN_SALARY, MAX(salary) as MAX_SALARY
FROM employees;

-- A query to get a monthly salary (round 2 decimal places) of each and every employee
SELECT ROUND(salary / 12.0, 2) AS MONTHLY_SALARY, first_name, last_name
FROM employees;