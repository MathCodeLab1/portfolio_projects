
-- Lesson 12: Correlated Subquery

SELECT Name,
       Department,
       Sales
FROM employees_v2 e1
WHERE Sales >
(

    SELECT AVG(Sales)
    FROM employees_v2 e2
    WHERE e2.Department = e1.Department
);