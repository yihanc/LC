/* 176. Second Highest Salary Add to List
# Description
# Submissions
# Solutions
# Total Accepted: 34550 Total Submissions: 179981 Difficulty: Easy
# Contributor: LeetCode
# Write a SQL query to get the second highest salary from the Employee table.
# 
# +----+--------+
# | Id | Salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# For example, given the above Employee table, the second highest salary is 200. If there is no second highest salary, then the query should return null.
# 
# Subscribe to see which companies asked this question.
*/

-- 2018.04.06
Select
  IFNULL((SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1,1), NULL) as SecondHighestSalary


-- 2018.03.06
# Write your MySQL query statement below
SELECT DISTINCT Salary AS SecondHighestSalary
FROM Employee e
UNION SELECT null
ORDER BY SecondHighestSalary DESC
LIMIT 1, 1

/* 2018.02.23
*/
select max(salary) as SecondHighestSalary
from employee
where salary < (select max(salary) from employee)
