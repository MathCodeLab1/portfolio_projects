
-- Lesson 13: Common Table Expressions(CTEs)

WITH AverageSales AS 
(
    SELECT AVG(Sales) AS AvgSales 
    FROM employees_v2
)

SELECT Name,
       Department.
       Sales
FROM employees_v2,
     AverageSales
WHERE Sales > AvgSales;