
-- Step 1 Create Departments table --

CREATE TABLE department (
    DepartmentID INTEGER,
    Department text
);


-- Step 2 Insert departments --

INSERT INTO department VALUES
(1,'HR'),
(2,'IT'),
(3,'Sales'),
(4,'Marketing');


-- Verify:
   SELECT * FROM department;


-- Step 3 - Create a new Employees table --

CREATE TABLE employees_join (
    EmployeeID INTEGER,
    Name TEXT,
    DepartmentID INTEGER,
    Sales INTEGER
);


-- Step 4 - Insert employees --

INSERT INTO employees_join VALUES
(1,'Anna',1,120),

(2,'Ben',2,200),

(3,'Cara',1,150),

(4,'David',2,180),

(5,'Steve',3,250),

(6,'Jane',4,170);


-- Step 5 - Look at the table --

SELECT *

FROM employees_join;


-- Step 6 - The magic(JOIN)

SELECT e.Name,
       d.Department,
       e.Sales
FROM employees_join e
JOIN department d
ON e.DepartmentID = d.DepartmentID;


-- Business Insight:

The JOIN operation combines employee information with department information by matching the DepartmentID.
This allows us to display meaningful department names while keeping the database organized and avoiding duplicated information.



