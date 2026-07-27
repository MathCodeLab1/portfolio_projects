

SELECT Department,
       SUM(Sales)
FROM employees
GROUP BY Department;

SELECT Department,
       AVG(Sales)
FROM employees
GROUP BY Department;

SELECT Department,
       count(*)
FROM employees
GROUP BY Department;