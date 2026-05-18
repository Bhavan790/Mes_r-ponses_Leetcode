# Write your MySQL query statement below
SELECT e.employee_id , e.salary AS bonus
FROM Employees e
WHERE e.name NOT LIKE "M%" 
AND e.employee_id %2 != 0 

UNION

SELECT e.employee_id , 0 AS bonus
FROM Employees e
WHERE e.name LIKE "M%" 
OR e.employee_id %2 = 0 

ORDER BY employee_id