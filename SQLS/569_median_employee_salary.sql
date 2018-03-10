/*
The Employee table holds all employees. The employee table has three columns: Employee Id, Company Name, and Salary.

+-----+------------+--------+
|Id   | Company    | Salary |
+-----+------------+--------+
|1    | A          | 2341   |
|2    | A          | 341    |
|3    | A          | 15     |
|4    | A          | 15314  |
|5    | A          | 451    |
|6    | A          | 513    |
|7    | B          | 15     |
|8    | B          | 13     |
|9    | B          | 1154   |
|10   | B          | 1345   |
|11   | B          | 1221   |
|12   | B          | 234    |
|13   | C          | 2345   |
|14   | C          | 2645   |
|15   | C          | 2645   |
|16   | C          | 2652   |
|17   | C          | 65     |
+-----+------------+--------+
Write a SQL query to find the median salary of each company. Bonus points if you can solve it without using any built-in SQL functions.

+-----+------------+--------+
|Id   | Company    | Salary |
+-----+------------+--------+
|5    | A          | 451    |
|6    | A          | 513    |
|12   | B          | 234    |
|9    | B          | 1154   |
|14   | C          | 2645   |
+-----+------------+--------+
*/

-- 2018.03.09

SELECT
  sub.Id,
  sub.Company,
  sub.Salary
FROM (
    SELECT 
        @rank := IF(@lastCompany = e.Company, @rank + 1, 1) as Rank,
        e.id,
        e.company,
        e.salary,
        fre.tot,
        @lastCompany := e.company
    FROM (SELECT @n1 := NULL, @n2 := NULL, @rank := 0, @lastCompany := 'A') SQLvars, Employee e
    LEFT JOIN ( SELECT e1.company, count(*) as tot FROM Employee e1 GROUP BY e1.company ) fre ON fre.company = e.company
    ORDER BY e.Company, e.Salary
) sub
WHERE sub.rank = sub.tot DIV 2 + 1 OR (sub.tot % 2 = 0 AND sub.rank = sub.tot DIV 2)

