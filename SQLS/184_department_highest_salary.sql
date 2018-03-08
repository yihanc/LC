/*# 184. Department Highest Salary Add to List
# Description
# Submissions
# Solutions
# Total Accepted: 18713 Total Submissions: 99441 Difficulty: Medium
# Contributor: LeetCode
# The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.
# 
# +----+-------+--------+--------------+
# | Id | Name  | Salary | DepartmentId |
# +----+-------+--------+--------------+
# | 1  | Joe   | 70000  | 1            |
# | 2  | Henry | 80000  | 2            |
# | 3  | Sam   | 60000  | 2            |
# | 4  | Max   | 90000  | 1            |
# +----+-------+--------+--------------+
# The Department table holds all departments of the company.
# 
# +----+----------+
# | Id | Name     |
# +----+----------+
# | 1  | IT       |
# | 2  | Sales    |
# +----+----------+
# Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, Max has the highest salary in the IT department and Henry has the highest salary in the Sales department.
# 
# +------------+----------+--------+
# | Department | Employee | Salary |
# +------------+----------+--------+
# | IT         | Max      | 90000  |
# | Sales      | Henry    | 80000  |
# +------------+----------+--------+
# Subscribe to see which companies asked this question. */


-- 2018.03.07
SELECT 
  d.Name AS Department,
  e.Name AS Employee,
  e.Salary
FROM Employee e
JOIN ( 
    SELECT 
        DepartmentId AS Id,
        MAX(salary) AS maxSalary
    From Employee e
    GROUP BY DepartmentId ) sub ON e.DepartmentId = sub.id    
JOIN Department d ON e.DepartmentId = d.id
WHERE e.Salary = sub.maxSalary
































-- 2017.04.01
select d.name as Department, e1.Name as Employee, e1.Salary
from employee e1
join ( select departmentid, max(salary) salary from employee e group by departmentid ) tmp 
    on e1.departmentid = tmp.departmentid and tmp.salary = e1.salary
join department d on d.id = e1.departmentid


-- 2017.03.3
SELECT D.Name as Department, E.Name as Employee, Salary
FROM 
    Employee E,
    ( 
        SELECT DepartmentId,
                ( 
                    SELECT MAX(SALARY)
                    FROM EMPLOYEE t2 
                    WHERE t2.DepartmentId = t1.DepartmentId ) as max3
        FROM Employee t1
        GROUP BY DepartmentId ) tmp,
    Department D
WHERE 
    E.departmentId = tmp.DepartmentId
    AND E.Salary = tmp.max3
    AND E.DepartmentId = D.id
