--Create database
--CREATE DATABASE Employee;

--Create table
CREATE TABLE IF NOT EXISTS Employee_Info
(
    EmployeeID int,
    EmployeeName varchar(255),
    EmergencyContactName varchar(255),
    PhoneNumber varchar(20),
    Address varchar(255),
    City varchar(255),
    Country varchar(255)
);

-- Renaming table
ALTER TABLE Employee_Info RENAME TO Employee_Data;

-- Adding new column
ALTER TABLE Employee_Data ADD COLUMN salary numeric;


-- Inserting data
INSERT INTO Employee_Data (EmployeeID, EmployeeName, EmergencyContactName, PhoneNumber, Address, City, Country) VALUES
(1, 'John Doe', 'Jane Doe', 1234567890, '123 Main St', 'Anytown', 'USA'),
(2, 'Alice Smith', 'Bob Smith', 9876543210, '456 Elm St', 'Otherville', 'Canada'),
(3, 'Eva Johnson', 'Michael Johnson', 5551234567, '789 Oak St', 'Somewhere', 'Australia');

-- Update salaries
UPDATE Employee_Data
SET Salary = 120000
WHERE EmployeeID = 1;

UPDATE Employee_Data
SET Salary = 160000
WHERE EmployeeID = 2;

UPDATE Employee_Data
SET Salary = 200000
WHERE EmployeeID = 3;

SELECT * FROM employee_data;

-- Delete where clause

DELETE FROM Employee_Data
WHERE Country = 'Canada';

SELECT * FROM employee_data;
