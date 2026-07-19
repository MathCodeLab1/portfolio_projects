
-- Part1 - AND --

-- Business Question:

SELECT *              -- Which IT employees have the sales greater than 180?
FROM employees_v2
WHERE Department = 'IT'
AND Sales > 180;


-- Business Insight:

Three IT employees generated more than 180 sales.
Quinn archived the highest sales(210) among them.


----------------------------------------------------------------------------------
----------------------------------------------------------------------------------

-- Part2 - OR --

-- Business Question:

SELECT *               -- Show all employees from HR or Marketing.
FROM employees_v2
WHERE Department = 'HR'
OR Department = 'Marketing';

-- Business Insight:

HR and Marketing together have 10 employees. This query demonstrates how the 
OR operator can combine multiple conditions to retrieve data from different departments.

----------------------------------------------------------------------------------
----------------------------------------------------------------------------------

-- Part3 - IN --

-- Business Question:


SELECT *
FROM employees_v2
WHERE Department IN ('HR','Marketing');


-- Business Insight:

The IN operator provides a cleaner and more readable way to filter multiple 
values in the same column compared to using several OR conditions.

----------------------------------------------------------------------------------
----------------------------------------------------------------------------------


-- part4 - BETWEEN --

-- Business Question:


SELECT Name
       Department,
       SALES
FROM employees_v2
WHERE Sales BETWEEN 150 AND 220
ORDER BY Sales DESC;


-- Business Insight:

Eleven employees have sales between 150 and 220. This range includes high-performing 
employees from several departments, with the Sales and IT departments appearing most frequently.


--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------


-- part5 - LIKE --

-- Business Question:

SELECT *
FROM employees_v2
WHERE Name LIKE 'S%';


-- Business Insight:

Only Steve has a name that starts with the letter S.


---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------

-- part6 - LIKE --

-- Business Question:

SELECT Name
       Department,
    FROM employees_v2
    WHERE Name LIKE '%a%';
    ORDER BY Name;


-- Business Insight:

Fourteen employees have the letter “a” in their name. These employees are spread across all departments, 
demonstrating how the LIKE operator can be used to search for text patterns.