# 181. Employees Earning More Than Their Managers Add to List
# Description
# Submissions
# Solutions
# Total Accepted: 33783 Total Submissions: 101908 Difficulty: Easy
# Contributor: LeetCode
# The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.
# 
# +----+-------+--------+-----------+
# | Id | Name  | Salary | ManagerId |
# +----+-------+--------+-----------+
# | 1  | Joe   | 70000  | 3         |
# | 2  | Henry | 80000  | 4         |
# | 3  | Sam   | 60000  | NULL      |
# | 4  | Max   | 90000  | NULL      |
# +----+-------+--------+-----------+
# Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.
# 
# +----------+
# | Employee |
# +----------+
# | Joe      |
# +----------+



-- 2018.03.07
SELECT Name AS Employee
FROM Employee e
WHERE e.Salary > (SELECT Salary FROM Employee e2 WHERE e.ManagerId = e2.id)






























-- 2017.04.01
select name as Employee
from employee e
where managerid is not null
     and e.salary > (select salary from employee e1 where id = e.managerid)


# 2017.03.31
SELECT a.name as Employee
FROM Employee a JOIN Employee b
WHERE a.ManagerId = b.Id and a.Salary > b.salary
