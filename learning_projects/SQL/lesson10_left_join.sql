

-- Lesson 10: LEFT JOIN --

SELECT d.Department,
       e.Name
FROM department database
LEFT JOIN employees_join e
ON d.DepartmentID = e.DepartmentID;


-- LEFT JOIN with COALESCE --

SELECT d.Department,
       COALESCE(e.Name, 'No Employee') AS Employee
FROM department d
LEFT JOIN employees_join e
ON d.DepartmentID = e.DepartmentID;