/*# 185. Department Top Three Salaries Add to List
# Description
# Submissions
# Solutions
# Total Accepted: 11669 Total Submissions: 73810 Difficulty: Hard
# Contributor: LeetCode
# The Employee table holds all employees. Every employee has an Id, and there is also a column for the department Id.
# 
# +----+-------+--------+--------------+
# | Id | Name  | Salary | DepartmentId |
# +----+-------+--------+--------------+
# | 1  | Joe   | 70000  | 1            |
# | 2  | Henry | 80000  | 2            |
# | 3  | Sam   | 60000  | 2            |
# | 4  | Max   | 90000  | 1            |
# | 5  | Janet | 69000  | 1            |
# | 6  | Randy | 85000  | 1            |
# +----+-------+--------+--------------+
# The Department table holds all departments of the company.
# 
# +----+----------+
# | Id | Name     |
# +----+----------+
# | 1  | IT       |
# | 2  | Sales    |
# +----+----------+
# Write a SQL query to find employees who earn the top three salaries in each of the department. For the above tables, your SQL query should return the following rows.
# 
# +------------+----------+--------+
# | Department | Employee | Salary |
# +------------+----------+--------+
# | IT         | Max      | 90000  |
# | IT         | Randy    | 85000  |
# | IT         | Joe      | 70000  |
# | Sales      | Henry    | 80000  |
# | Sales      | Sam      | 60000  |
# +------------+----------+--------+
*/


-- 2018.03.07
# Write your MySQL query statement below

SELECT
  d.Name AS Department,
  sub.Name AS Employee,
  sub.Salary
FROM (
    SELECT 
      DepartmentId,
      Name, 
      Salary,
      @rank := IF(DepartmentId != @lastDept, 
                  1,
                  IF(Salary < @lastSalary, @rank + 1, @rank)) as Rank,
      @lastSalary := Salary,
      @lastDept := DepartmentId
    FROM 
      Employee e,
      (SELECT @rank := 1, @lastSalary := null, @lastDept := null) SQLvars
    ORDER BY DepartmentId, Salary DESC
) sub
JOIN Department d ON d.id = sub.DepartmentId
WHERE sub.rank <= 3















-- 2017.04.01
select d.name as Department, e.Name as Employee, e.Salary
from employee e
join department d on d.id = e.departmentid
where e.salary >= ifnull((select distinct salary from employee e1 where e1.departmentid = e.departmentid order by salary desc limit 2, 1), 0)
order by d.name, e.salary



-- 2017.03.31 SQL
SELECT D.Name as Department, E.Name as Employee, Salary
FROM 
    Employee E,
    ( 
        SELECT DepartmentId,
        IFNULL (( 
                    SELECT DISTINCT SALARY 
                    FROM EMPLOYEE t2 
                    WHERE t2.DepartmentId = t1.DepartmentId 
                    ORDER BY SALARY DESC LIMIT 2, 1), 0) as max3
        FROM Employee t1
        GROUP BY DepartmentId ) tmp,
    Department D
WHERE 
    E.departmentId = tmp.DepartmentId
    AND E.Salary >= tmp.max3
    AND E.DepartmentId = D.id
