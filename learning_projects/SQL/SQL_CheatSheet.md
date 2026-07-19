# SQL Cheat Sheet

## Show all rows

SELECT * FROM employees;

## Filter rows

SELECT *

FROM employees

WHERE Department = 'IT';

## Sort rows

SELECT *

FROM employees

ORDER BY Sales DESC;

## Total sales per department

SELECT Department,

       SUM(Sales)

FROM employees

GROUP BY Department;

## Average sales per department

SELECT Department,

       AVG(Sales)

FROM employees

GROUP BY Department;