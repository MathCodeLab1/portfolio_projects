
-- SQL Project 1
-- Employee Analytics (small dataset)

-- Business Question 1 --

SELECT Department,                  -- Which department generated the highest sales?
       SUM(Sales) AS TotalSales
FROM employees
GROUP BY Department
ORDER BY TotalSales DESC;

-- Business Insight #1: --
IT has the highest average sales per employee (190).
HR averages 120 sales per employee.

This suggests that, on average, IT employees generate 
more sales than HR employees.

--------------------------------------------------------------------------------------


-- Business Question 2 --

SELECT Department,                 -- Which department has the highest average sales?
       AVG(Sales) AS AverageSales
FROM employees
GROUP BY Department
ORDER BY AverageSales DESC;

-- Business Insight #2: --

IT has the highest average sales per employee (190).
HR averages 120 sales per employee.

This suggests that IT employees generate more sales on average than HR employees.

---------------------------------------------------------------------------------------


-- Business Question 3 --

SELECT Department,               -- How many employees work in each department? 
       COUNT(*) AS Employees
FROM employees
GROUP BY Department;

-- Business Insight #3: --

HR has 3 employees while IT has 2 employees.
Although HR has more employees. IT generated higher total sales.

---------------------------------------------------------------------------------------

-- BUsiness Question 4 --

SELECT *                       -- Who is the top-performing employee?
FROM employees
ORDER BY Sales DESC;

-- Business Insight #4 --

Ben is the top-performing employee with sales of 200.
He contributed the highest individual sales in the company.


-- Business Question 5 --

SELECT Department,            -- Which departments have average sales above 150?
       AVG(Sales) AS AverageSales
FROM employees
GROUP BY Department
HAVING AVG(Sales) > 150;


-- Business Insight #5 --

Only IT department has an average sales value above 150.
This indicates that IT consistently performs better on average than HR.

---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------

-- SQL Project 2 --
-- Employee Analytics V2 (20 Employees)

-- Business Question #1 --