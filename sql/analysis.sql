-- Avg Salary
SELECT department, AVG(salary)
FROM employee_cleaned
GROUP BY department;

-- Top Earners
SELECT *
FROM (
    SELECT *, RANK() OVER (PARTITION BY department ORDER BY salary DESC) rnk
    FROM employee_cleaned
) t
WHERE rnk = 1;

-- Salary Distribution
SELECT department, salary_category, COUNT(*)
FROM employee_cleaned
GROUP BY department, salary_category;
