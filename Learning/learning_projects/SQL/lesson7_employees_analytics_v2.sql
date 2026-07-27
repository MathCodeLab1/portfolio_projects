
-- SQL Project 2 --
-- Employee Analytics v2 (20 dataset)

-- Business Question 1 --

SELECT Department,            -- Which department generated the highest total sales?
       SUM(Sales) AS TotalSales
FROM employees_v2
GROUP BY Department
ORDER BY TotalSales DESC;


-- Business Insight #1

Sales generated the highest total sales with 1150.
IT followed with 940.
HR generated 700.
Marketing generated the lowest total sales with 650.


----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

-- Business Question 2 --

SELECT Name,              -- Top-performing employees.
       Department,
       Sales
FROM employees_v2
ORDER BY Sales DESC;

-- Business Insight #2

Steve is the highest-performing employee with sales of 250.
he contributed the highest individual sales in the company.


-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------


-- Business Question 3 --

SELECT Region,                -- Which Region generated the highest total sales?
       SUM(Sales) AS TotalSales
FROM employees_v2
GROUP BY Region
ORDER BY TotalSales DESC;


-- Business Insight #3

East generated the highest sales with 1310.

South ranked second with 950.

North generated the lowest total sales.


----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

-- Business Question 4 --

SELECT Department,           -- Show only departments whose average sales are above 170
       AVG(Sales) AS AverageSales
FROM employees_v2
GROUP BY Department
ORDER BY AverageSales DESC;


-- Business Insight #4

The Sales department achieved the highest average sales per employee (230.0), indicating consistently strong individual performance.

IT ranked second with an average of 188.0, followed by Marketing (162.5). HR had the lowest average sales (116.67).


--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------


-- Business Question 5 --

SELECT Department,
       AVG(Sales) AS AverageSales 
FROM employees_v2
GROUP BY Department
HAVING AVG(Sales) > 170
ORDER BY AverageSales DESC;

-- Business Insight #5

Only the Sales and IT departments have an average sales value above 170.

These departments consistently outperform HR and Marketing in terms of average employee sales.
       
