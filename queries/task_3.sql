 -- A query in SQL to display the first name, last name, department number, and department name for each employee
 SELECT emp.first_name, emp.last_name, dep.department_name, dep.department_id
FROM employees emp
INNER JOIN department dep ON
emp.department_id = dep.department_id;

-- A query in SQL to display the first and last name, department, city, and state province for each employee
 SELECT emp.first_name, emp.last_name, dep.department_name, loc.city, loc.state_province
FROM employees emp
INNER JOIN department dep ON
emp.department_id = dep.department_id
 INNER JOIN locations loc ON
dep.location_id = loc.location_id;

 --A query in SQL to display the first name, last name, department number, and department name,
 -- for all employees for departments 80 or 40
 SELECT first_name, last_name, dep.department_id, department_name
FROM employees emp
INNER JOIN department dep ON
emp.department_id = dep.department_id
 WHERE dep.department_id IN(40, 80);

-- A query in SQL to display all departments including those where does not have any employee
SELECT
    department.department_id,
    department.department_name,
    employees.first_name
FROM
    department
LEFT JOIN employees ON
    department.department_id = employees.department_id;

-- A query in SQL to display the first name of all employees including the first name of their manager (join)
SELECT emp.first_name, m.manager_name
FROM employees emp
INNER JOIN manager m ON
emp.manager_id = m.manager_id;

-- A query in SQL to display the job title, full name (first and last name ) of the employee, and the difference between the maximum salary for the job and the salary of the employee
SELECT emp.first_name, emp.last_name, j.job_title, j.max_salary - emp.salary AS salary_market_difference
FROM employees emp
INNER JOIN jobs j ON
emp.job_id = j.job_id;

-- A query in SQL to display the job title and the average salary of employees
 SELECT emp.first_name, j.job_title, (j.max_salary + j.min_salary) / 2 AS average_salary
FROM employees emp
INNER JOIN jobs j ON
emp.job_id = j.job_id;

-- A query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London
SELECT e.first_name, e.last_name, e.salary
FROM employees e, department d
WHERE e.department_id = d.department_id AND d.location_id=
(SELECT locations.location_id
FROM locations
WHERE locations.city =  'London');

-- A query in SQL to display the department name and the number of employees in each department
SELECT dep.department_name, COUNT(emp.employee_id) AS employees_number_per_department
FROM employees emp
INNER JOIN department dep ON
emp.department_id = dep.department_id
GROUP BY dep.department_name;
