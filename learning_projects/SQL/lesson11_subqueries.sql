-- Lesson 11: Subqueries

SELECT Name,
       Department,
       Sales
FROM employees_v2
WHERE Sales > (
    SELECT AVG(Sales)
    FROM employees_v2
);


------------------------------------------------------------------------

SELECT Name,
       Department,      -- Employee with the highest Sales. --
       Sales
FROM employees_v2
WHERE Sales = (
    SELECT MAX(Sales)
    FROM employees_v2
);


-------------------------------------------------------------------------

SELECT Name,
       Department,  -- Employees whose Bonus is less than the average bonus. --
       Sales
FROM employees_v2
WHERE Bonus < (
    SELECT AVG(Bonus)
    FROM employees_v2
);


